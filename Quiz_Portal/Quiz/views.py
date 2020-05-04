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
    wrng_ans={}
    cmnt={10:'Not bad',20:"One more time and you'll have it",30:"You're doing a good job",40:"You've got your brain in gear today",50:'I knew you could do it'}
    for m in m_ans:
        score=0
        wrng_ans={}
        for q in c_ans:
            answers.append((q.ques,q.ca))
        if m.ans1==answers[0][1]:
            score+=10
        else:
            wrng_ans[m.ans1]=answers[0]
        if m.ans2==answers[1][1]:
            score+=10
        else:
            wrng_ans[m.ans2]=answers[1]
        if m.ans3==answers[2][1]:
            score+=10
        else:
            wrng_ans[m.ans3]=answers[2]
        if m.ans4==answers[3][1]:
            score+=10
        else:
            wrng_ans[m.ans4]=answers[3]
        if m.ans5==answers[4][1]:
            score+=10
        else:
            wrng_ans[m.ans5]=answers[4]
        Mentee.objects.filter(phn_num=m.phn_num).update(
            score=score,
        )
    return render(req,'Quiz/success.html',{'score':score,'max_score':max_score,'wrng_ans':wrng_ans,'cmnt':cmnt})
def result(req):
    m=Mentee.objects.all().order_by('-score')
    return render(req,'Quiz/result.html',{'res':m})
