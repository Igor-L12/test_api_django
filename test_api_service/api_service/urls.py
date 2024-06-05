from django.urls import path, include

from api_service.views import AdDetailView

urlpatterns = [
    path('api_services/<int:ad_id>/', AdDetailView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
