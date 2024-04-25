from ckeditor.fields import RichTextField
from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=500, )
    site_header_logo = models.FileField(upload_to="images/site")
    site_footer_logo = models.FileField(upload_to="images/site")
    site_favicon = models.FileField(upload_to="images/site")
    site_tag_line = models.CharField(max_length=500, null=True, blank=True)
    site_description = models.TextField()
    hero_tag_line = models.TextField()
    hero_image = models.FileField(upload_to="images/site", null=True,blank=True)
    client_section_title = models.TextField(null=True, blank=True)
    services_title = models.CharField(max_length=500, null=True, blank=True)
    services_description = models.TextField(null=True, blank=True)
    cta_heading = models.CharField(max_length=500, null=True, blank=True)
    cta_description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name


class Clients(models.Model):
    client_name = models.CharField(max_length=500, null=True, blank=True)
    client_logo = models.FileField(upload_to="images/clients", null=True, blank=True)

    class Meta:
        verbose_name = "Clients"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.client_name


class Services(models.Model):
    service_icon = models.FileField(upload_to="images/services", null=True, blank=True)
    service_name = models.CharField(max_length=500)
    service_description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Services"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.service_name


class AboutUsPage(models.Model):
    page_title = models.CharField(max_length=500)
    page_description = models.TextField(null=True, blank=True)
    block_1_icon = models.FileField(upload_to="images/about", null=True, blank=True)
    block_1_title = models.CharField(max_length=500)
    block_1_description = models.TextField(null=True, blank=True)

    block_2_icon = models.FileField(upload_to="images/about", null=True, blank=True)
    block_2_title = models.CharField(max_length=500)
    block_2_description = models.TextField(null=True, blank=True)

    block_3_icon = models.FileField(upload_to="images/about", null=True, blank=True)
    block_3_title = models.CharField(max_length=500)
    block_3_description = models.TextField(null=True, blank=True)

    block_4_icon = models.FileField(upload_to="images/about", null=True, blank=True)
    block_4_title = models.CharField(max_length=500)
    block_4_description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "About us Page"
        verbose_name_plural = "About us Page"

    def __str__(self):
        return self.page_title


class ServicesPage(models.Model):
    page_title = models.CharField(max_length=500)
    page_description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Services Page"
        verbose_name_plural = "Services Page"

    def __str__(self):
        return self.page_title


class ContactPage(models.Model):
    page_title = models.CharField(max_length=500)
    page_description = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)

    class Meta:
        verbose_name = "Contact Page"
        verbose_name_plural = "Contact Page"

    def __str__(self):
        return self.page_title


class TermsConditions(models.Model):
    page_title = models.CharField(max_length=100)
    content = RichTextField()

    class Meta:
        verbose_name = "Terms Conditions"
        verbose_name_plural = "Terms Conditions"

    def __str__(self):
        return self.page_title


class PrivacyPolicy(models.Model):
    page_title = models.CharField(max_length=100)
    content = RichTextField()

    class Meta:
        verbose_name = "Privacy Policy"
        verbose_name_plural = "Privacy Policy"

    def __str__(self):
        return self.page_title
