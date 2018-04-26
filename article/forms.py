from django import forms
from django.contrib.auth.models import User
from django.utils.timezone import now
from .models import *

class LoginForm(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'id': 'userName'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password'}), min_length=8, max_length=20)
    email = forms.CharField(widget=forms.TextInput(attrs={'id': 'email'}))

    class Meta:
        model = User
        fields = ("username","password","email")


class IdenCodeForm(forms.Form):
    iden_code = forms.CharField(label="验证码", max_length=6,min_length=6,widget=forms.TextInput(attrs={"id":"code"}))


class EmailLoginForm(forms.Form):
    user_name = forms.CharField(label="用户名",max_length=16, widget=forms.TextInput(attrs={"id":"loginuser"}))
    code = forms.CharField(label="验证码",max_length=6,min_length=6,widget=forms.TextInput)


class AriclesForm(forms.ModelForm):
    category = forms.ModelChoiceField(required=True, queryset=Category.objects.all(),empty_label="请选择分类")
    body = forms.CharField(widget=forms.Textarea(attrs={"id":"text1","class":"hidden"}))

    class Meta:
        model = Articles
        fields = ("title", "abstract", "attachment", "body",)


class PersonalInfoForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"readonly": "true"}))
    email = forms.CharField(widget=forms.TextInput)
    born = forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    college = forms.ModelChoiceField(required=True, queryset=College.objects.all(), empty_label="请选择学院")
    intro = forms.CharField(widget=forms.TextInput)
    sex = forms.ChoiceField(label="性别",widget=forms.RadioSelect(), choices=PersonalInfo.sex_choice)

    class Meta:
        model = PersonalInfo
        fields = ("sex",)


class ResetPwdForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"readonly":"true"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"id":"pwd1"}))
    cpassword = forms.CharField(widget=forms.PasswordInput(attrs={"id":"pwd2"}))

    def clean_cpassword(self):
        cd = self.cleaned_data
        if cd['password'] != cd['cpassword']:
            raise forms.ValidationError("passwords do not match")
        return cd['cpassword']