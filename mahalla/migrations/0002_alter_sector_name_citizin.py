# Generated by Django 4.1.7 on 2023-04-01 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mahalla", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sector",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Sektor nomi"),
        ),
        migrations.CreateModel(
            name="Citizin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Poliklinika nomi"),
                ),
                (
                    "sector",
                    models.ForeignKey(
                        help_text="Poliklinika qaysi sektorga tegishliekanligini tanlang",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="mahalla.sector",
                    ),
                ),
            ],
        ),
    ]
