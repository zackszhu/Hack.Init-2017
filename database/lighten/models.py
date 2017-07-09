from django.db import models

# Create your models here.
class Lighten(models.Model):
	direction1 = models.FloatField()
	direction2 = models.FloatField()
	direction3 = models.FloatField()
	username = models.CharField(max_length = 20)
	furniture_id = models.CharField(max_length = 20)
	furniture_type = models.CharField(max_length = 20)
	furniture_on = models.CharField(max_length = 20)
	furniture_off = models.CharField(max_length = 20)

	class Meta:
		ordering = ('direction1', 'direction2', 'direction3',)


class User(models.Model):
	username = models.CharField(max_length = 80)
	password = models.CharField(max_length = 40)
