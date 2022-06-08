from django.db import models
from django.utils.text import slugify

# Create your models here.

class BaseModel(models.Model):

    class Meta:
        abstract = True  
        app_label = 'qa'

class Questions(BaseModel):
      question_id=models.AutoField(primary_key=True)
      question_title=models.CharField(max_length=50)
      question_body=models.TextField()
      date_posted=models.DateTimeField(auto_now_add=True)
      posted_by= models.TextField(max_length=50)
      slug=models.SlugField(max_length=50) # For URL

      def save(self, *args, **kwargs):
            self.slug = slugify(self.question_title)
            super(Questions, self).save(*args, **kwargs)

class Answers(BaseModel):
      answer_id=models.AutoField(primary_key=True)
      question_id=models.ForeignKey(Questions, on_delete=models.CASCADE)
      answer_body=models.TextField()
      date_posted=models.DateTimeField(auto_now_add=True)
      posted_by=models.CharField(max_length=50)