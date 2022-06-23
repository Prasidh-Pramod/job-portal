from django.db import models

# Create your models here.

class Jobs(models.Model):
    job_title=models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    location = models.CharField(null=True,max_length=150)
    experience=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.job_title