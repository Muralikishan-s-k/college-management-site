# Generated by Django 5.0 on 2023-12-31 05:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fkeyapp', '0002_student_joining_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usermember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('number', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fkeyapp.course')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]