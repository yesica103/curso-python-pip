from django.db import models

# Create your models here.
class Car(models.Model):
    title =models.TextField(max_length=250)
    year=models.TextField(max_length=4, null=True)
    color=models.TextField(max_length=50, null=True)

    def __str__(self):
        return f"{self.title} - {self.year} - {self.color}"
    
class Publisher(models.Model):
    name = models.TextField(max_length=250)
    address = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.TextField(max_length=250)
    birth_date = models.DateField()
    
    def __str__(self):
        return self.name, self.birth_date

class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    website = models.URLField()
    biography = models.TextField(max_length=500)

    
    
    
class Book(models.Model):
    title = models.TextField(max_length=250)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return f"{self.title} - {self.publication_date} - {self.publisher.name}"

    

