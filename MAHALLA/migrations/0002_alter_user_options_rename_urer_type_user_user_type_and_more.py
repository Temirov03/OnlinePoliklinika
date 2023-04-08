# Generated by Django 4.1.7 on 2023-04-01 18:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("MAHALLA", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "Fuqoro", "verbose_name_plural": "Fuqorolar"},
        ),
        migrations.RenameField(
            model_name="user",
            old_name="urer_type",
            new_name="user_type",
        ),
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(default=django.utils.timezone.now, max_length=25),
            preserve_default=False,
        ),
    ]
