from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

# def index(request):
#     return render(request,template_name="index.html")
def index(request):
    #查找后5个ID
    question_list = Question.objects.order_by('-pub_date')[:5]
    #把查到的数据生成字典
    context = {"question_list":question_list}
    #将字典作为参数传递给模版
    return render(request,"index.html",context)


def detail(request,question_id):
    # return HttpResponse("you see id is %s"%question_id)
    return render(request,"detail.html")

def vote(request,question_id):
    # return HttpResponse("you vote is %s"%question_id)
    return render(request,"vote.html")

def result(request,question_id):
    # return HttpResponse("result value is %s"%question_id)
    return render(request,"result.html")


