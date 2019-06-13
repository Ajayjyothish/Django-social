from django.db import models
from django.urls import reverse


# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	summary = models.TextField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
    		return reverse("book", kwargs={"book_no": self.id})
			# return f"/book/{self.id}"

class Post(models.Model):
	subject = models.TextField( max_length=50)
	last_updated = models.DateTimeField( auto_now_add=True)
	views = models.PositiveIntegerField(default = 0)

	def __str__(self):
		return self.subject