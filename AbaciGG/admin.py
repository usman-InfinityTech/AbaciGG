from django.contrib import admin

from AbaciGG.models import SiteSettings, AboutUsPage, ServicesPage, PrivacyPolicy, TermsConditions, ContactPage, \
    Clients, Services

admin.site.index_title = "Abaci GG"
admin.site.site_title = "Abaci GG"
admin.site.site_header = "Abaci GG"


class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'site_header_logo', 'site_footer_logo', 'site_favicon', 'site_tag_line',
                    'hero_tag_line', 'client_section_title']

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()


class AboutUsPageAdmin(admin.ModelAdmin):
    list_display = ['page_title']

    def has_add_permission(self, request):
        return not AboutUsPage.objects.exists()


class ServicesPageAdmin(admin.ModelAdmin):
    list_display = ['page_title', ]

    def has_add_permission(self, request):
        return not ServicesPage.objects.exists()


class ContactPageAdmin(admin.ModelAdmin):
    list_display = ['page_title', 'location', 'phone_number', 'email_address', ]

    def has_add_permission(self, request):
        return not ContactPage.objects.exists()


class TermsConditionsAdmin(admin.ModelAdmin):
    list_display = ['page_title', ]

    def has_add_permission(self, request):
        return not TermsConditions.objects.exists()


class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ['page_title', ]

    def has_add_permission(self, request):
        return not PrivacyPolicy.objects.exists()


class ClientsAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_logo', ]


class ServicesAdmin(admin.ModelAdmin):
    list_display = ['service_icon', 'service_name', ]


admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(AboutUsPage, AboutUsPageAdmin)
admin.site.register(ServicesPage, ServicesPageAdmin)
admin.site.register(ContactPage, ContactPageAdmin)
admin.site.register(TermsConditions, TermsConditionsAdmin)
admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)
admin.site.register(Clients)
admin.site.register(Services)
