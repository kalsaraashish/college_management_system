# Generated by Django 3.0.6 on 2025-02-26 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_management_app', '0006_auto_20250226_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='student_pics/'),
        ),
    ]
