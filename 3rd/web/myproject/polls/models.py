from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class User(models.Model):
    user_name = models.CharField(max_length=200)
    pass_word = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.user_name