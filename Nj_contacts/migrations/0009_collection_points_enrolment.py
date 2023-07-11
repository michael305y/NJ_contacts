# Generated by Django 4.2.2 on 2023-07-09 15:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nj_contacts', '0008_remove_contact_location_alter_contact_school_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection_points',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_code', models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_school_code', message='School code should have 8 digits', regex='^20409\\d{3}$')])),
                ('school_name', models.CharField(max_length=200)),
                ('entry', models.IntegerField()),
                ('collection_point', models.CharField(choices=[], max_length=30)),
                ('route', models.IntegerField(default=90, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Enrolment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]