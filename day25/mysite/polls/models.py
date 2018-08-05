from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    """
    Question类定义了投票应用中问题的模型
    """
    #定义问题的题目
    question_text = models.CharField(max_length=200,)
    #定义发表时间
    pub_date = models.DateTimeField()
    def __str__(self):
        return "%s.%s"%(self.id,self.question_text)

    #自定义方法,判断发布时间是不是一天内的
    def was_published_recently(self):
        #timezone.now() - datetime.timedelta(days=1) 获取一天前的当前时间
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        # retrun True or Flase



class Choice(models.Model):
    """
    Choice类定义了投票应用中选项的模型
    """
    #定义选项的内容
    choice_test = models.CharField(max_length=200)
    #定义得票数
    votes = models.IntegerField(default=0)
    #定义选项对应的问题
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    def __str__(self):
        return "%s.%d"%(self.choice_test,self.votes)
