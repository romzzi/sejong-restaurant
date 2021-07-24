from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    address = models.CharField(max_length=100)
    price = models.IntegerField(null=False)
    open_time = models.CharField(max_length=50)
    emotion = models.BooleanField(null=False)
    who = models.CharField(max_length=50)
    drink = models.BooleanField(null=False)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
    number = models.IntegerField(unique=True)
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.number}. {self.content}'

class Choice(models.Model):
    select = models.CharField(max_length=100)
    question = models.ForeignKey(to='main.Question', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(to='main.Restaurant', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.select} {self.restaurant}'