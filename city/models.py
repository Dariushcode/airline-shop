from django.db import models

class Ostan(models.Model):
    title = models.CharField(max_length=350,blank=False, verbose_name='نام استان')

    def __str__(self):
        return f"{self.title}"

class Cities(models.Model):
    title = models.CharField(max_length=350,blank=False, verbose_name='نام شهر')
    Ostan = models.ForeignKey(Ostan, null=True, blank=True, related_name='cities', on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title} - {self.Ostan.title}"
