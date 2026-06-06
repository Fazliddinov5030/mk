from django.urls import path
from .views import CertificateView

urlpatterns = [
    path(
        'enrollments/<int:enrollment_id>/certificate/',
        CertificateView.as_view(),
        name='certificate'
    ),
]