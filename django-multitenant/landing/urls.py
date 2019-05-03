from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static 

from landing.views import RenderLanding
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
                url(r'^$', login_required(RenderLanding.as_view()), name='render_landing'),
                 ]