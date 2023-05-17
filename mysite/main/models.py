from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField('Home name', max_length=255)
    about = models.TextField('Home text')
    button_name = models.CharField('Home button name', max_length=60)
    img = models.ImageField('Home image', upload_to='home_images')
    logo = models.ImageField('Home logo', upload_to='home_images', blank=True)

    def __str__(self):
        return self.name
    

class Project(models.Model):

    name = models.CharField('Project name', max_length=100)
    img1 = models.ImageField('Project image1', upload_to='projects_images')
    img2 = models.ImageField('Project image2', upload_to='projects_images')
    img3 = models.ImageField('Project image3', upload_to='projects_images')

    def __str__(self):
        return self.name