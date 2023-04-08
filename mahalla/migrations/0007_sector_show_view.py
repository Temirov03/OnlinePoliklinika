# Generated by Django 4.1.7 on 2023-04-02 05:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("mahalla", "0006_hosptal_name_hosptal_sector"),
    ]

    operations = [
        migrations.AddField(
            model_name="sector",
            name="show_view",
            field=models.CharField(
                default=django.utils.timezone.now,
                help_text="Qaysi tumanga tegishli ekanligini kiriting",
                max_length=255,
                verbose_name="Tuman nomi",
            ),
            preserve_default=False,
        ),
    ]
