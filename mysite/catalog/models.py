from django.db import models
from django import forms
import os 
# Create your models here.
# LEN_DESC = 50

class Image(models.Model):
	name = models.CharField(max_length = 200)
	image = models.ImageField(upload_to = "images")
	desc = models.TextField() 
	date = models.DateField()

	def __str__(self):
		return self.name

	# def get_short_desc(self):
	# 	if len(self.desc) > LEN_DESC:
	# 		return self.desc[:LEN_DESC]
	# 	else:
	# 		return self.desc

class DateForm(forms.Form):
   myDate = forms.DateField()