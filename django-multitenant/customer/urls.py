from django.conf.urls import url, include

from django.conf.urls.static import static 

from .import views

urlpatterns = [
            url(r'^register/', views.register_customer, name='registercustomer'),
            ]