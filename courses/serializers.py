from rest_framework import serializers
from .models import Category, Course, Module, Lesson

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'content', 'order')


class ModuleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ('id', 'title', 'order', 'lessons')


class CourseSerializer(serializers.ModelSerializer):
    instructor = serializers.StringRelatedField(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True,
        allow_null=True,
        required=False
    )
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = (
            'id', 'title', 'slug', 'description',
            'price', 'status', 'instructor',
            'category', 'category_id', 'modules',
            'created_at', 'updated_at'
        )
        read_only_fields = ('slug', 'instructor', 'created_at', 'updated_at')