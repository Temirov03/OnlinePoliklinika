from django.db import models
from ckeditor.fields import RichTextField

class User(models.Model):
    USER_TYPE = (
        ('sector_leader', 'Sektor bosh shifokori'),
        ('add_leader', 'Bosh shifokori'),
        ('app_leader', 'Hamshira'),

    )
    user_type = models.CharField(verbose_name="Shiforkorlar lavozimi", max_length=255, choices= USER_TYPE, default="Ishtixon tumani 1-sonli poliklinika", help_text ='Shifokor lavozimini kiriting')
    name = models.CharField(verbose_name='F.I.O', max_length=25)
    photo = models.ImageField(upload_to='MAHALLA/images/')
    short_discription = models.TextField()
    discription = RichTextField(null=True, blank=True)




    class Meta:
        verbose_name = 'Shifokor'
        verbose_name_plural = 'Shifokorlar'