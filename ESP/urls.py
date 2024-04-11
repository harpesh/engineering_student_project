
from django.contrib import admin
from django.urls import path,include
from API import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

router = DefaultRouter()

router.register('StudentAPI', views.StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('exportstudents/', views.export_students_to_excel, name='export-students'),
]
