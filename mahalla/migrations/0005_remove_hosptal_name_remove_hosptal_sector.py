# Generated by Django 4.1.7 on 2023-04-02 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mahalla", "0004_hosptal_alter_sector_options_delete_citizin_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hosptal",
            name="name",
        ),
        migrations.RemoveField(
            model_name="hosptal",
            name="sector",
        ),
    ]
