from django.db import models
from ckeditor.fields import RichTextField

class Sector(models.Model):
    add = models.CharField(verbose_name="Viloyat nomi", help_text="Ushbu sektor qaysi viloyatga tegishli ekanligini belgilang", max_length=255)
    app = models.CharField(verbose_name="Tuman(Rayon) nomi", help_text="Ushbu sektor qaysi tumanga(rayonga) tegishli ekanligini belgilang", max_length=255)
    name = models.CharField(verbose_name="Sektor nomi", max_length=255)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sektor"
        verbose_name_plural = "Sektorlar"
        ordering = ["id"]

class Hosptal(models.Model):
    GENDER = (
        ('yes', "Ha"),
        ('no', "Yo'q"),
    )

    sector = models.ForeignKey('Sector', on_delete=models.PROTECT,
                               help_text = "Poliklinika qaysi sektorga tegishli ekanligini tanlang", null=True, blank=True)
    name = models.CharField(verbose_name='Poliklinika nomi',max_length=255)

    gender = models.CharField(
        max_length=255,
        choices = GENDER,
        verbose_name='Yetakchi poliklinikami',
        help_text= "Ilg'or poliklinikami yo'qmi"
    )

    def __str__(self):
        return self.sector


    class Meta:
        verbose_name = 'Poliklinika'
        verbose_name_plural = 'Poliklinikalar'




