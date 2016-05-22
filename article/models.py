from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Topic(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)	
	text = RichTextUploadingField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Article(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	UNARIAN = 'UN'
	DECENARIAN = 'DE'
	CENTENARIAN = 'CE'
	LEVEL_CHOICES = (
		(UNARIAN, 'Unarian'),
		(DECENARIAN, 'Decenarian'),
		(CENTENARIAN, 'Centenarian'),
	)
	level = models.CharField(
		max_length=2,
		choices = LEVEL_CHOICES,
		default = UNARIAN
	)
	topic = models.ForeignKey(
		Topic,
		on_delete = models.CASCADE,
		blank = True,
		null = True,
		default = None
	)
	text = RichTextUploadingField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title