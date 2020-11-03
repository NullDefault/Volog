from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from api.logistics.serializers import HourSerializer
from api.models import Student, HourInstance


class CurrentStudentHoursView(generics.ListAPIView):
    """
    API endpoint to retrieve hours for the current (session) student.
    """
    serializer_class = HourSerializer

    def get_queryset(self):
        user = self.request.user
        student = Student.objects.filter(user=user)[0]
        hours = HourInstance.objects.filter(student=student)
        return hours.all()


class PostHourSubmissionView(generics.CreateAPIView):
    """
    API endpoint for students to post hours.
    """
    serializer_class = HourSerializer

    def post(self, request, *args, **kwargs):
        def parse_hour_type(oval):
            if oval == "Required":
                return 'REQ'
            elif oval == "Pre-Approved":
                return 'PRE'
            elif oval == "Active":
                return 'ACT'
            elif oval == "Receptive":
                return 'REC'

        data = request.data
        if 'student' not in data:
            user = self.request.user
            student = Student.objects.filter(user=user)[0].pk
            data['student'] = student
            data['type_of_hour'] = parse_hour_type(data['type_of_hour'])
            data['learning_goal'] = data['learning_goal'].upper()

        serializer = HourSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)