from django.db import models
from django.db.models.fields import DateField

# Create your models here.

class Home(models.Model):
  
      name = models.CharField(max_length=50)
      gretings_1 = models.CharField(max_length=50)
      gretings_2 = models.CharField(max_length=50)
      pictures = models.ImageField( upload_to='pictures/')
      update = models.DateTimeField( auto_now=True)

      def __str__(self):
          return self.name

class About(models.Model):
      heading = models.CharField(max_length=50)
      career = models.CharField(max_length=50)
      description = models.TextField()
      profile_img = models.ImageField( upload_to='profile/')
      update = models.DateTimeField( auto_now=True)


      def __str__(self):
          return self.career

class Profile(models.Model):
    about= models.ForeignKey(About, on_delete=models.CASCADE)
    social_name= models.CharField(max_length=50)
    link = models.URLField(max_length=200)


class Category(models.Model):
    name = models.CharField(max_length=50)
    update = models.DateTimeField( auto_now=True)

    class Meta:
        verbose_name ='Skill'
        verbose_name_plural ='Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)


class Portfolio(models.Model):
    image =models.ImageField(upload_to='portfolio/')
    link = models.URLField( max_length=200)


    def __str__(self):
        return f'Portfolio {self.id}'




        

    



          
  

  

