import uuid
from django.db import models

# Create your models here.
class Provider(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  providerName = models.CharField(max_length = 200)
  providerUrl = models.URLField(max_length = 500)
  Email = models.EmailField()
  Password = models.CharField(max_length = 200)

class Course(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  providerID = models.ForeignKey(Provider, on_delete = models.SET_DEFAULT, default = uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')) #6fa459ea-ee8a-3ca4-894e-db77e160355e
  courseProviderID = models.CharField(max_length = 50)
  courseName = models.CharField(max_length = 200)
  authorName = models.CharField(max_length = 200)
  courseUrl = models.URLField(max_length = 500)
  courseSummary = models.TextField()
  courseCategory = models.CharField(max_length = 200)
  isDownloaded = models.BooleanField(default = False)