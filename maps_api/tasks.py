# maps_api/tasks.py

import os
import json
import ollama
import googlemaps
from celery import shared_task

@shared_task
def process_find_place_request(user_prompt, user_lat=None, user_lon=None):
    """
    Task Celery untuk memproses permintaan pencarian lokasi secara asinkron.
    """
    gmaps_api_key = os.environ.get('GOOGLE_MAPS_API_KEY')
    if not gmaps_api_key:
        raise ValueError("Google Maps API Key tidak ditemukan.")
    gmaps = googlemaps.Client(key=gmaps_api_key)

    system_prompt = """
    Dari prompt pengguna, identifikasi 'apa' yang sedang dicari (query)
    dan 'di mana' lokasinya (location).
    Hanya kembalikan respons dalam format JSON yang valid dengan key "query" dan "location".
    """
    
    try:
        response_llm = ollama.chat(
            model='deepseek-r1:7b',
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_prompt},
            ],
            format='json',
            options={'temperature': 0}
        )
        llm_output_text = response_llm['message']['content']
        extracted_info = json.loads(llm_output_text)
        search_query = f"{extracted_info.get('query')} in {extracted_info.get('location')}"
    except Exception as e:
        return {'error': f"Gagal saat berkomunikasi dengan Ollama: {str(e)}"}

    try:
        places_result = gmaps.places(query=search_query)

        if places_result.get('status') == 'OK':
            results = []
            for place in places_result.get('results', [])[:5]:
                place_id = place.get('place_id')
                embed_url = f"https://www.google.com/maps/embed/v1/place?key={gmaps_api_key}&q=place_id:{place_id}"

                if user_lat is not None and user_lon is not None:
                    directions_url = f"https://www.google.com/maps/dir/?api=1&origin={user_lat},{user_lon}&destination_place_id={place_id}"
                else:
                    directions_url = f"https://www.google.com/maps/dir/?api=1&destination_place_id={place_id}"

                results.append({
                    "name": place.get('name'),
                    "address": place.get('formatted_address'),
                    "rating": place.get('rating', 'N/A'),
                    "place_id": place_id,
                    "embed_url": embed_url,
                    "directions_url": directions_url,
                })
            return {'data': results}
        else:
            return {'error': 'Tidak ada hasil yang ditemukan di Google Maps.'}
    except Exception as e:
        return {'error': f"Gagal saat berkomunikasi dengan Google Maps: {str(e)}"}