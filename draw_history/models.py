from django.db import models

# Create your models here.
class DrawHistory(models.Model):
    draw_no = models.IntegerField(primary_key=True)
    draw_no_1 = models.IntegerField()
    draw_no_2 = models.IntegerField()
    draw_no_3 = models.IntegerField()
    draw_no_4 = models.IntegerField()
    draw_no_5 = models.IntegerField()
    draw_no_6 = models.IntegerField()
    draw_date = models.DateField()
    registration_date = models.DateTimeField(auto_now=True)
    
    def __int__(self):
        return self.draw_no
        