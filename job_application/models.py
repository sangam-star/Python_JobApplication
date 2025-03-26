from django.db import models

# Create your models here.
 
class JobApplication(models.Model):
    job_title = models.CharField(max_length=100)
    applicant_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    resume = models.FileField(upload_to='resumes/')
    application_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.applicant_name} - {self.job_title}'
