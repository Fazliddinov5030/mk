import uuid
import logging
from io import BytesIO
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from .models import Certificate
from enrollments.models import Enrollment

logger = logging.getLogger(__name__)

class CertificateService:

    @staticmethod
    def get_or_create_certificate(enrollment: Enrollment) -> Certificate:
        """Sertifikat yaratish yoki mavjudini qaytarish"""

        # Kurs 100% tugatilganmi?
        if enrollment.progress_percent < 100:
            raise ValueError("Kurs hali tugatilmagan")

        cert, created = Certificate.objects.get_or_create(
            student=enrollment.student,
            course=enrollment.course,
            defaults={'certificate_id': str(uuid.uuid4())[:8].upper()}
        )

        if created:
            logger.info(
                'Yangi sertifikat yaratildi',
                extra={
                    'user_id': enrollment.student.id,
                    'course_id': enrollment.course.id
                }
            )

        return cert

    @staticmethod
    def generate_pdf(certificate: Certificate) -> HttpResponse:
        """PDF sertifikat yaratish"""

        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4

        # --- Fon rangi ---
        p.setFillColor(colors.HexColor('#1a1a2e'))
        p.rect(0, 0, width, height, fill=True, stroke=False)

        # --- Sariq chiziq (yuqori) ---
        p.setStrokeColor(colors.HexColor('#f0c040'))
        p.setLineWidth(4)
        p.line(40, height - 40, width - 40, height - 40)

        # --- BilimHub sarlavha ---
        p.setFillColor(colors.HexColor('#f0c040'))
        p.setFont("Helvetica-Bold", 36)
        p.drawCentredString(width / 2, height - 100, "BilimHub")

        # --- Sertifikat matni ---
        p.setFillColor(colors.white)
        p.setFont("Helvetica", 16)
        p.drawCentredString(width / 2, height - 150, "SERTIFIKAT")

        # --- Talaba ismi ---
        p.setFont("Helvetica-Bold", 28)
        p.setFillColor(colors.HexColor('#f0c040'))
        p.drawCentredString(
            width / 2, height - 230,
            certificate.student.get_full_name() or certificate.student.username
        )

        # --- Kurs nomi ---
        p.setFillColor(colors.white)
        p.setFont("Helvetica", 18)
        p.drawCentredString(
            width / 2, height - 290,
            f'"{certificate.course.title}"'
        )
        p.drawCentredString(
            width / 2, height - 320,
            "kursini muvaffaqiyatli tugatdi"
        )

        # --- Sana ---
        p.setFont("Helvetica", 12)
        p.setFillColor(colors.HexColor('#aaaaaa'))
        date_str = certificate.issued_at.strftime("%d.%m.%Y")
        p.drawCentredString(width / 2, height - 400, f"Sana: {date_str}")

        # --- Sertifikat ID ---
        p.setFont("Helvetica", 10)
        p.drawCentredString(
            width / 2, 50,
            f"Sertifikat ID: {certificate.certificate_id}"
        )

        # --- Pastki chiziq ---
        p.setStrokeColor(colors.HexColor('#f0c040'))
        p.line(40, 40, width - 40, 40)

        p.showPage()
        p.save()

        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = (
            f'attachment; filename="certificate_{certificate.certificate_id}.pdf"'
        )
        return response