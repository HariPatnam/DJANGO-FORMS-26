from django import forms

g=[('male','MALE'),('female', 'FEMALE')]
c=(['python','python'],['java','java'])

class studentform(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    date=forms.DateField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=100,widget=forms.Textarea)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.ChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)



