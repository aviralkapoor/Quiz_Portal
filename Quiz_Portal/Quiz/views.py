from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(req):
    if req.method=='POST':
        form=mentee_form(req.POST)
        if form.is_valid():
            form.save()
            phn_num=form.cleaned_data['phn_num']
            return HttpResponseRedirect(reverse('success',kwargs={'phn_num':phn_num}))
    else:
        form=mentee_form()
    return render(req,'Quiz/index.html',{'contact_form':form})

def success(req,phn_num):
    c_ans=Question.objects.all()
    m_ans=Mentee_2.objects.all()
    answers=[]
    score=0
    max_score=0
    wrng_ans={}
    cmnt={0:'I believe in you',10:'Not bad',20:"One more time and you'll have it",30:"You're doing a good job",40:"You've got your brain in gear today",50:'I knew you could do it'}
    for m in m_ans:
        if m.phn_num == phn_num :
            score=0
            wrng_ans={}
            for q in c_ans:
                if int(q.id) > 6:     
                    answers.append((q.ques,q.ca))
                    max_score+=10 #Each Ques carries 10 marks.
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
            Mentee_2.objects.filter(phn_num=m.phn_num).update(
            score=score,
            )
    return render(req,'Quiz/success.html',{'score':score,'max_score':max_score,'wrng_ans':wrng_ans,'cmnt':cmnt})
def result(req):
    m=Mentee_2.objects.all().order_by('-score')
    return render(req,'Quiz/result.html',{'res':m})
