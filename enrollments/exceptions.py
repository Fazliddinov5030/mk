class EnrollmentError(Exception):
    """Enrollment bilan bog'liq base exception"""

class AlreadyEnrolledError(EnrollmentError):
    """Talaba allaqachon bu kursga yozilgan"""
    pass

class CourseNotPublishedError(EnrollmentError):
    """Kurs hali nashr qilinmagan"""
    pass