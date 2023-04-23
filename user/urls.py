from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'rest/v1/calendar/init/', views.GoogleCalendarInitView.as_view(), basename='google_permission')

urlpatterns = [
    path('rest/v1/calendar/init/', views.GoogleCalendarInitView.as_view(), name='google_permission'),
    path('rest/v1/calendar/redirect/', views.GoogleCalendarRedirectView.as_view(), name='google_redirect')
]