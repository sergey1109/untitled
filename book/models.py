from django.db import models
from django.conf import settings
# Create your models here.

class H_book(models.Model):
    HOTEL_RANK_STARS = (
        ('1*' , 'One star hotel '),
        ('2*' , 'Two stars hotel '),
        ('3*' , 'Three stars hotel '),
        ('4*' , 'Four stars hotel '),
        ('5*' , 'Five stars hotel '),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1500)
    price = models.FloatField()
    hot_price = models.BooleanField(default=False)
    new_price = models.FloatField(blank=True,null=True)
    ranks = models.CharField(choices=HOTEL_RANK_STARS,max_length=255 )


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    h_ranks = models.ForeignKey(H_book, on_delete=models.CASCADE)
    chek_in = models.DateTimeField()
    chek_out = models.DateTimeField()

    def  __str__(self):
        return f'{self.user} has booked {self.h_ranks} from {self.chek_in} to {self.chek_out}'