from django.db import models
from django.utils import timezone


now = timezone.now
# Create your models here.
class SingleRoom(models.Model):
	name = models.CharField(max_length=50, blank=False)
	surname = models.CharField(max_length=50, blank=True)
	email = models.EmailField()
	description = models.TextField(blank=True)
	arrival_date = models.DateField(default=now)
	departure_date = models.DateField(blank=True)
	num_of_rooms = 4	
	




