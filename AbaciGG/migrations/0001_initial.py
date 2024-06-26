# Generated by Django 3.2.25 on 2024-04-25 09:44

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(max_length=500)),
                ('page_description', models.TextField(blank=True, null=True)),
                ('block_1_icon', models.ImageField(blank=True, null=True, upload_to='images/about')),
                ('block_1_title', models.CharField(max_length=500)),
                ('block_1_description', models.TextField(blank=True, null=True)),
                ('block_2_icon', models.ImageField(blank=True, null=True, upload_to='images/about')),
                ('block_2_title', models.CharField(max_length=500)),
                ('block_2_description', models.TextField(blank=True, null=True)),
                ('block_3_icon', models.ImageField(blank=True, null=True, upload_to='images/about')),
                ('block_3_title', models.CharField(max_length=500)),
                ('block_3_description', models.TextField(blank=True, null=True)),
                ('block_4_icon', models.ImageField(blank=True, null=True, upload_to='images/about')),
                ('block_4_title', models.CharField(max_length=500)),
                ('block_4_description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'About us Page',
                'verbose_name_plural': 'About us Page',
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, max_length=500, null=True)),
                ('client_logo', models.ImageField(blank=True, null=True, upload_to='images/clients')),
            ],
            options={
                'verbose_name': 'Clients',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(max_length=500)),
                ('page_description', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name': 'Contact Page',
                'verbose_name_plural': 'Contact Page',
            },
        ),
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Privacy Policy',
                'verbose_name_plural': 'Privacy Policy',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_icon', models.ImageField(blank=True, null=True, upload_to='images/services')),
                ('service_name', models.CharField(max_length=500)),
                ('service_description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Services',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='ServicesPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(max_length=500)),
                ('page_description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Services Page',
                'verbose_name_plural': 'Services Page',
            },
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=500)),
                ('site_header_logo', models.ImageField(upload_to='images/site')),
                ('site_footer_logo', models.ImageField(upload_to='images/site')),
                ('site_favicon', models.ImageField(upload_to='images/site')),
                ('site_tag_line', models.CharField(blank=True, max_length=500, null=True)),
                ('site_description', models.TextField()),
                ('hero_tag_line', models.TextField()),
                ('client_section_title', models.TextField(blank=True, null=True)),
                ('services_title', models.CharField(blank=True, max_length=500, null=True)),
                ('services_description', models.TextField(blank=True, null=True)),
                ('cta_heading', models.CharField(blank=True, max_length=500, null=True)),
                ('cta_description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Site Settings',
                'verbose_name_plural': 'Site Settings',
            },
        ),
        migrations.CreateModel(
            name='TermsConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Terms Conditions',
                'verbose_name_plural': 'Terms Conditions',
            },
        ),
    ]
