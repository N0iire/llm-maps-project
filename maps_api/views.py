# maps_api/views.py

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from celery.result import AsyncResult
from .tasks import process_find_place_request

def home_view(request):
    """View sederhana untuk me-render halaman index.html."""
    return render(request, 'index.html')

class FindPlaceAPIView(APIView):
    """
    API view untuk MEMULAI tugas pencarian lokasi secara asinkron.
    """
    def post(self, request, *args, **kwargs):
        prompt = request.data.get('prompt')
        lat = request.data.get('latitude')
        lon = request.data.get('longitude')

        if not prompt:
            return Response({"error": "Prompt tidak boleh kosong."}, status=status.HTTP_400_BAD_REQUEST)

        task = process_find_place_request.delay(prompt, lat, lon)

        return Response({'task_id': task.id}, status=status.HTTP_202_ACCEPTED)

class TaskStatusAPIView(APIView):
    """
    API view untuk mengecek status dan hasil dari sebuah task Celery.
    """
    def get(self, request, task_id, *args, **kwargs):
        task_result = AsyncResult(task_id)

        result = {
            "task_id": task_id,
            "status": task_result.status,
            "result": task_result.result if task_result.ready() else None
        }
        
        return Response(result, status=status.HTTP_200_OK)