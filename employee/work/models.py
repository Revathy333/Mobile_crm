from django.db import models

# Create your models here.
#models: which is used to perform certain actions using data. eg: CRUD (create,read/retrive,update,delete)

class Mobiles(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    model = models.CharField(max_length=30)
    launch_year = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} -  {self.price}  {self.model} ({self.launch_year})"
        
class Mobiles(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    model = models.CharField(max_length=30)
    launch_year = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.model} ({self.launch_year})"


    
class Empoloyee(models.Model):
    uname = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    place = models.CharField(max_length=30)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.uname

class Student(models.Model):
    name = models.CharField(max_length=40)
    place = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)    
    email = models.EmailField(unique=False,null=True)

    def name_all(self):
        return self.name
    
    def gender_all(self):
        return self.gender
    
    def place_all(self):
        return self.place
    
class Emp(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    salary = models.PositiveIntegerField()
    contact = models.CharField(max_length=30)    

class Book(models.Model):
    title = models.CharField(max_length=30)
    author =models.CharField(max_length=50)
    publication_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=50)    

class Movies(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    category = models.CharField(max_length=30)
    review = models.CharField(max_length=100)  

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=30) 
    email = models.EmailField(unique=False,null=True)
    course = models.CharField(max_length=50)     

class StudentNew(models.Model):
    name = models.CharField(max_length=40)
    age = models.PositiveIntegerField() 
    course = models.CharField(max_length=40)
    gender = models.CharField(max_length=20)
    place = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} - {self.age} {self.course} {self.gender} ({self.place})"