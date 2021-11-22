from django.db import models
import uuid 
from django.contrib.auth.models import User

class Quiz(models.Model):
    quiz_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True) 
    topic = models.CharField(max_length=100)
    desc = models.CharField(max_length=250)
    number_of_questions = models.PositiveIntegerField()
    
    def __str__(self):
        return self.topic


Types = (
    ('MCQ','Multiple Choice Question'),
    ('FIB','Fill In the Blank Question')
)

class Questions(models.Model):
    
    question_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True) 
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name="questions")
    question_name = models.CharField(max_length=100)
    type = models.CharField(max_length=3,choices=Types)
    marks = models.PositiveIntegerField()
    time = models.FloatField()

    def __str__(self):
        return f"{self.question_name}\t:\t{self.quiz.topic}"

class MCQ(models.Model):
    #id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True) 
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.question.question_name} \t:\t {self.answer}"

class FIB(models.Model):
    #id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return str(self.question.question_name)+"\t:\t"+str(self.answer) 


class UserAnswers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.question.question_name}\t:\t{self.answer}"