from django.contrib.auth.models import User
from django import forms


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label = 'Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repeat Password', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        # clean_필드명 형태의 메서드로 각 필드의 cleam 메서드가 호출된 후에 호출되는 메서드들이며 유효성 검사나 조작을 하고 싶을 때 만들어서 사용한다.
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password']