from django.shortcuts import render
from customer.forms import RegisterForm
from customer.models import Client
from django.contrib.auth.models import User
from project_setting.settings import Tenant_Host_URL
from tenant_schemas.utils import schema_context

# Create your views here.

def register_customer(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            businessname = form.cleaned_data.get('businessname')
            domainurl = form.cleaned_data.get('domain_url')           
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            paiduntil = '2019-12-01'
            ontrial=False
            schemaname = domainurl
            domainurl = domainurl+"."+Tenant_Host_URL
            
            customer_set = {
            'domain_url': domainurl,
            'schema_name': schemaname,
            'name': businessname,
            'paid_until': paiduntil,
            'on_trial': ontrial
            }
        
            user_set = {
            'username' : username,
            'first_name' : username,
            'email' : email,
            'is_active' : True,
            'is_staff' : True,
            'is_superuser' : True
            }
            
            client = Client(**customer_set) 
            client_set = client.save()
          
            with schema_context(schemaname):
                  user_instance = User(**user_set)
                  user_instance.set_password(password)
                  user_instance.save()

            
            return render(request, 'customer/re_direct.html', {'url_data': domainurl})
        else:
            return render(request, 'customer/customer_register_form.html', {'form': form})
    else:
        form = RegisterForm
        return render(request, 'customer/customer_register_form.html', {'form': form})  