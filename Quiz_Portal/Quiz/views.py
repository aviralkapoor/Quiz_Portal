from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse, HttpResponseRedirect

def index(req):
    if req.method=='POST':
        form=mentee_form(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
    else:
        form=mentee_form()
    return render(req,'Quiz/index.html',{'contact_form':form})

def success(req):
    c_ans=Question.objects.all()
    m_ans=Mentee.objects.all()
    max_score=Question.objects.count()*10 #Each Ques carries 10 marks.
    answers=[]
    score=0
    for m in m_ans:
        for q in c_ans:
            answers.append(q.ca)
        if m.ans1==answers[0]:
            score+=10
        if m.ans2==answers[1]:
            score+=10
        if m.ans3==answers[2]:
            score+=10
        if m.ans4==answers[3]:
            score+=10
        if m.ans5==answers[4]:
            score+=10
    return render(req,'Quiz/success.html',{'score':score,'max_score':max_score})