from django.db import models
import uuid 
# from django.contrib.auth.models import User
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

class Quiz_Taken(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.PROTECT)
    question_id = models.ForeignKey(Questions,on_delete=models.PROTECT)
    answer_id = models.CharField(max_length=1)
    answer_text = models.CharField(max_length=100)
    # def __str__(self):
    #     return f"{self.question_id.question_text}\t:\t{self.answer_}"

# class MCQ(models.Model):
#     #id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True) 
#     question = models.ForeignKey(Questions,on_delete=models.CASCADE)
#     option1 = models.CharField(max_length=100)
#     option2 = models.CharField(max_length=100)
#     option3 = models.CharField(max_length=100)
#     option4 = models.CharField(max_length=100)
#     answer = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.question.question_name} \t:\t {self.answer}"

# class FIB(models.Model):
#     #id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
#     question = models.ForeignKey(Questions,on_delete=models.CASCADE)
#     answer = models.CharField(max_length=100)

#     def __str__(self):
#         return str(self.question.question_name)+"\t:\t"+str(self.answer) 

