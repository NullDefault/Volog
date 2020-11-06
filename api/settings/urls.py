"""
File Name: Urls
Purpose: Url paths for the API app.
Comments:
"""

from django.urls import include, path
from rest_framework import routers

import api.views.hour_views
import api.views.mentor_views
import api.views.student_views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
from api.views.user_views import UserListView, GetRequestUserData
from api.views.group_views import GroupView, StudentGroupView


router = routers.SimpleRouter()
router.register('api/groups', GroupView, basename='group')
router.register(
    'api/groups/(?P<group_id>\d+)/members', StudentGroupView, basename='group-student'
)

urlpatterns = [
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/students/', api.views.student_views.StudentListView.as_view()),
    path('api/students/current/', api.views.student_views.CurrentStudentView.as_view()),
    path('api/students/current/hours/', api.views.hour_views.CurrentStudentHoursView.as_view()),
    path('api/students/current/hourReport/', api.views.hour_views.PostHourSubmissionView.as_view()),
    path('api/mentors/', api.views.mentor_views.MentorListView.as_view()),
    path('api/users/', UserListView.as_view()),
    path('api/users/current', GetRequestUserData.as_view()),
    path('api/details/', GetRequestUserData.as_view()),
    path('api/activity_categories/', api.views.hour_views.ActivityCategoriesView.as_view())
]

urlpatterns += router.urls
