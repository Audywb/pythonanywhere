from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.question_text}'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question.question_text} - {self.choice_text} - {self.votes}'

class Sell(models.Model):
    name = models.CharField(max_length=100)
    p_number = models.CharField(max_length=10)
    e_mail = models.CharField(max_length=50)
    address = models.TextField()
    postcode = models.CharField(max_length=10)
    number_slip = models.IntegerField()
    

    def __str__(self):
        return f'{self.name} - {self.p_number} - {self.address}- {self.p_number} - {self.postcode}- {self. number_slip}'

class Comment(models.Model):
     
    Name = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=10)
    Email = models.CharField(max_length=100)
 
    def __str__(self):   # __unicode__ on Python 2
        return self.Name

class Comment2(models.Model):
     
    id = models.AutoField(primary_key=True)
    User_Name = models.CharField(max_length=100)
    Phone = models.IntegerField()
    E_mail = models.CharField(max_length=100)
    A_ddess = models.CharField(max_length=500)
    P_code = models.IntegerField()
    N_slip = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):   # __unicode__ on Python 2
        return self.User_Name