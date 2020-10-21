from rest_framework import serializers

from api.models import Student, Mentor


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ('first_name', 'last_name', 'email')


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_id', 'email', 'class_standing', 'DAS_mentor', 'hour_sheet']
