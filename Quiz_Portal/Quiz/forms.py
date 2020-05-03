from django import forms
from .models import *

QuesList=[]
AnsList={}
choices_ans=[]
for q in Question.objects.all():
    QuesList.append(q.ques)
    choices_ans.append((q.opt1,q.opt1))
    choices_ans.append((q.opt2,q.opt2))
    choices_ans.append((q.opt3,q.opt3))
    choices_ans.append((q.opt4,q.opt4))
    AnsList[q.ques]=choices_ans
    choices_ans=[]


class mentee_form(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),required=True,max_length=50,label=False)
    phn_num=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobile Number'}),required=True,max_length=10,label=False)
    batch_num=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Batch Number'}),required=True,max_length=1,label=False)
    ans1= forms.CharField(label=QuesList[0], widget=forms.RadioSelect(choices=AnsList[QuesList[0]]))
    ans2= forms.CharField(label=QuesList[1], widget=forms.RadioSelect(choices=AnsList[QuesList[1]]))
    ans3= forms.CharField(label=QuesList[2], widget=forms.RadioSelect(choices=AnsList[QuesList[2]]))
    ans4= forms.CharField(label=QuesList[3], widget=forms.RadioSelect(choices=AnsList[QuesList[3]]))
    ans5= forms.CharField(label=QuesList[4], widget=forms.RadioSelect(choices=AnsList[QuesList[4]]))

    class Meta():
        model=Mentee
        fields=['name','phn_num','batch_num','ans1','ans2','ans3','ans4','ans5']