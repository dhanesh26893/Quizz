from django.db import models
import uuid 
from user.models import User

class Quiz(models.Model):
    quiz_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True) 
    topic = models.CharField(max_length=100)
    desc = models.CharField(max_length=250)
    
    def __str__(self):
        return self.topic


Types = (
    ('MCQ','Multiple Choice Question'),
    ('FIB','Fill In the Blank Question')
)

class Questions(models.Model):    
    question_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True) 
    quiz_id = models.ForeignKey(Quiz,on_delete=models.PROTECT)
    question_text = models.CharField(max_length=100)
    type = models.CharField(max_length=3,choices=Types)
    marks = models.PositiveIntegerField()
    time = models.FloatField()

    def __str__(self):
        return f"{self.question_text}\t:\t{self.quiz_id.topic}"


class Answer(models.Model):
    question_id = models.ForeignKey(Questions,on_delete=models.PROTECT)
    answer_text = models.CharField(max_length=100)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question_id}\t:\t{self.answer_text}\t:\t{self.correct}"

class QuizTaken(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.PROTECT)
    question_id = models.ForeignKey(Questions,on_delete=models.PROTECT)
    answer_id = models.CharField(max_length=1,blank=True,null=True)
    answer_text = models.CharField(max_length=100,blank=True,null=True)
