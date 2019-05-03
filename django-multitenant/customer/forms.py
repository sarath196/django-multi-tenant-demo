from django import forms
from customer.models import Client

from project_setting.settings import Tenant_Host_URL

class RegisterForm(forms.Form):
    username = forms.CharField()
    businessname = forms.CharField()
    domain_url = forms.CharField(help_text=Tenant_Host_URL)
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    re_type_password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    
    class Meta:
        fields = ['username', 'businessname', 'domain_url', 'email', 'password', 're_type_password']
        
    def clean_re_type_password(self):
        password = self.cleaned_data.get('password')
        repassword = self.cleaned_data.get('re_type_password')
        if password != repassword :
            raise forms.ValidationError("Incorrect Password")
        
        return password