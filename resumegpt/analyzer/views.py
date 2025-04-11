from django.shortcuts import render

# Create your views here.
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.core.files.storage import default_storage

class ResumeUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        resume_file = request.FILES.get('resume')
        job_desc = request.data.get('job_description', '')

        if not resume_file:
            return Response({"error": "No file uploaded."}, status=400)

        file_path = default_storage.save(f"resumes/{resume_file.name}", resume_file)

        return Response({
            "message": "Resume uploaded successfully.",
            "file_path": file_path,
            "job_description": job_desc
        })
