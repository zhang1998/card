from django.shortcuts import render
from .models import *
# Create your views here.
def homeCo(request):
    showAr=article.objects.all()
    return render(request,"home.html",{"columns":showAr})
#    return render(request,"newGroup/test.html",{"columns":columns})
def returnText(request):
    q = request.POST['input']
    showBr=article.objects.get(id=q)
    # 按照获取的data值 进行部分处理
    '''
    1. 按照id  获取对应的 column
    2. 按照column 渲染text
    '''
    return render(request,"shText.html",{"column":showBr})
def testReturnText(request):

    showBr=article.objects.get(id="3")
    # 按照获取的data值 进行部分处理
    '''
    1. 按照id  获取对应的 column
    2. 按照column 渲染text
    '''
    print(showBr.title)
    return render(request,"shText.html",{"column":showBr})
def getQuestions(request):
    showAr=saQuestions.objects.all()
    return render(request,"question.html",{"columns":showAr})
#    return render(request,"newGroup/test.html",{"columns":columns})
def returnQue(request):
    q = request.POST['input']
    showBr=saQuestions.objects.get(id=q)
    # 按照获取的data值 进行部分处理
    '''
    1. 按照id  获取对应的 column
    2. 按照column 渲染text
    '''
    return render(request,"shQue.html",{"column":showBr})
