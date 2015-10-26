from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.

class Contact(models.Model):
  Name = models.CharField(max_length=300)
  EMail = models.TextField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  def __unicode__(self):
    return self.title
  def get_absolute_url(self):
    return reverse("contact_detail", args=[self.id])

