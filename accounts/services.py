from django.contrib.auth import get_user_model
from .exceptions import UserAlreadyExistsError

User = get_user_model()

class UserService:
    @staticmethod
    def register_user(username, email, password, role='student'):
        if role == 'teacher':
            role = 'instructor'
        allowed_roles = {'student', 'instructor', 'admin'}
        if role not in allowed_roles:
            role = 'student'

        if not username:
            username = email

        if User.objects.filter(username=username).exists():
            raise UserAlreadyExistsError("Bu login bilan ro'yxatdan o'tgan foydalanuvchi mavjud")

        user = User.objects.create_user(username=username, email=email, password=password)
        if hasattr(user, 'role'):
            user.role = role
        user.save()
        return user