from django.shortcuts import render

from AbaciGG.models import SiteSettings, Clients, Services, AboutUsPage, TermsConditions, PrivacyPolicy, ContactPage, \
    ServicesPage


def index(request):
    site_settings = SiteSettings.objects.first()
    clients = Clients.objects.all()
    services = Services.objects.all()[:3]
    context = {
        "site_settings": site_settings,
        "clients": clients,
        "services": services
    }
    return render(request, template_name="website/index.html", context=context)


def about_us(request):
    site_settings = SiteSettings.objects.first()
    about = AboutUsPage.objects.first()
    context = {
        "site_settings": site_settings,
        "about": about
    }
    return render(request, template_name="website/about_us.html", context=context)


def our_services(request):
    site_settings = SiteSettings.objects.first()
    service_page = ServicesPage.objects.first()
    services = Services.objects.all()
    context = {
        "site_settings": site_settings,
        "services": services,
        "service_page": service_page,
    }
    return render(request, template_name="website/services.html", context=context)


def term_and_conditions(request):
    site_settings = SiteSettings.objects.first()
    terms = TermsConditions.objects.first()
    context = {
        "site_settings": site_settings,
        "terms": terms
    }
    return render(request, template_name="website/terms.html", context=context)


def privacy_policy(request):
    site_settings = SiteSettings.objects.first()
    privacy = PrivacyPolicy.objects.first()
    context = {
        "site_settings": site_settings,
        "privacy": privacy
    }
    return render(request, template_name="website/privacy_policy.html", context=context)


def contact_us(request):
    site_settings = SiteSettings.objects.first()
    contact = ContactPage.objects.first()
    context = {
        "site_settings": site_settings,
        "contact": contact
    }
    return render(request, template_name="website/contact_us.html", context=context)


def lunacapital(request):
    site_settings = SiteSettings.objects.first()
    service_page = ServicesPage.objects.first()
    services = Services.objects.all()
    context = {
        "site_settings": site_settings,
        "services": services,
        "service_page": service_page,
    }
    return render(request, template_name="website/lunacapital.html", context=context)
