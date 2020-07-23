from django import forms
class MyRegForm(forms.Form):
    username=forms.CharField(label='用户名')
    password=forms.CharField(label='密码')
    password2=forms.CharField(label='重复密码')
    # age=forms.IntegerField(label='年龄')
    def clean_username(self):
        uname=self.cleaned_data['username']
        if len(uname)<6:
            raise forms.ValidationError('message')
        return uname
    def clean(self):
        pw1=self.cleaned_data['password']
        pw2=self.cleaned_data['password2']
        if pw1!=pw2:
            raise forms.ValidationError('密码不相同')