from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from enrollments.models import Enrollment
from .services import CertificateService

class CertificateView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, enrollment_id):
        try:
            enrollment = Enrollment.objects.select_related(
                'student', 'course'
            ).get(id=enrollment_id, student=request.user)
        except Enrollment.DoesNotExist:
            return Response({'error': 'Topilmadi'}, status=404)

        try:
            cert = CertificateService.get_or_create_certificate(enrollment)
        except ValueError as e:
            return Response({'error': str(e)}, status=400)

        return CertificateService.generate_pdf(cert)