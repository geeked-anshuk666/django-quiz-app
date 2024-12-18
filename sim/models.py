from django.db import models


class Quiz(models.Model):
  name = models.CharField(max_length=300)
  topic = models.CharField(max_length=300, default='General')


class Question(models.Model):
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
  text = models.CharField(max_length=300)
  topic = models.CharField(max_length=300,default='General')


class Answer(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  text = models.CharField(max_length=300)
  # topic = models.CharField(max_length=300)
  is_correct = models.BooleanField(default=False)


