from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib import admin

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('apps.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]
