from celery import shared_task
from django.core.mail import EmailMessage
from enrollments.models import Enrollment
from .services import CertificateService
import logging

logger = logging.getLogger(__name__)

@shared_task
def generate_and_send_certificate(enrollment_id):
    try:
        enrollment = Enrollment.objects.get(id=enrollment_id)
        
        # Xizmatingizdan foydalanib cert va pdf HttpResponse yaratamiz
        cert = CertificateService.get_or_create_certificate(enrollment)
        pdf_response = CertificateService.generate_pdf(cert)
        
        # Email jo'natish
        email = EmailMessage(
            subject=f"Tabriklaymiz! {enrollment.course.title} kursini yakunladingiz",
            body="Sizning elektron sertifikatingiz xatga ilova qilindi. Kelgusi ishlaringizda zafarlar tilaymiz!",
            from_email="noreply@bilimhub.uz",
            to=[enrollment.student.email],
        )
        email.attach(f'certificate_{cert.certificate_id}.pdf', pdf_response.content, 'application/pdf')
        email.send()
        logger.info(f"Sertifikat yuborildi: {enrollment.student.email}")
    except Exception as e:
        logger.error(f"Sertifikat generatsiyasi/yuborilishida xatolik: {e}")