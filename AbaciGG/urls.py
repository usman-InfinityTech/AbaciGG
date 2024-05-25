"""AbaciGG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from AbaciGG import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('lunacapital/', views.lunacapital, name="lunacapital"),
    path('about-us/', views.about_us, name="about_us"),
    path('services/', views.our_services, name="our_services"),
    path('terms-conditions/', views.term_and_conditions, name="term_and_conditions"),
    path('privacy-policy/', views.privacy_policy, name="privacy_policy"),
    path('contact-us/', views.contact_us, name="contact_us"),
    path('service-detail-bi/', views.services_detail_bi, name="services_detail-bi"),
    path('service-detail-forecasting/', views.services_detail_forecasting, name="services_detail-forecasting"),
    path('service-detail-reporting/', views.services_detail_reporting, name="services_detail-reporting"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)