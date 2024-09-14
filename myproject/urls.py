"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="BookMania API",
      default_version='v1',
      description="API for managing books",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kalejaiyemayowa3@gmail.com"),
      license=openapi.License(name="This API is licensed under the following terms:\n1. You are free to use this API for personal and non-commercial purposes.\n2. Any commercial use, redistribution, or modification requires prior written permission from the author.\n3. Attribution is required for any use of this API. You must give appropriate credit by mentioning the author, provide a link to the API repository, and indicate if any changes were made.\n4. If these terms are violated, legal action may be taken by the author.\nFor permissions beyond the scope of this license, please contact: mayowa.kalejaiye@example.com.\nAuthor: Mayowa Kalejaiye"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),  # Include your app's URLs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

