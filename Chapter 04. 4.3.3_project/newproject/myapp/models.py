from django.db import models

# Create your models here.		
class Food(models.Model):
	name = models.CharField(max_length = 64)
	price = models.IntegerField(default = 1000)
	calorie = models.FloatField()
	is_fruit = models.BooleanField(default = True)
	memo = models.TextField(blank = True)
	store = models.ForeignKey("Store")
	
	def __unicode__(self):
		return "food: %s" % (self.name, )

class Store(models.Model):
	name = models.CharField(max_length = 128)
	
	def __unicode__(self):
		return "store: %s" % (self.name, )
	
class Recipe(models.Model):
	name = models.CharField(max_length = 128)
	ingredients = models.ManyToManyField("Food")
	
	def __unicode__(self):
		return "recipe: %s" % (self.name, )