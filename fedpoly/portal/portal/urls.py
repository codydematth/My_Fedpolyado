"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from teachers.views import SignUp
from portal.views import index, blog
from students.views import blog_details, soon
from django.contrib.staticfiles.templatetags.staticfiles import static as staticfiles
from django.urls import path, include
from django.utils.translation import ugettext_lazy as _
from material.admin.sites import site

site.site_header =_("The Federal Polytechnic Ado")
site.site_title=_("The Federal Polytechnic Ado")
site.index_title=_("The Federal Polytechnic Ado Administration")
site.users_name_color = 'purple'
site.favicon = staticfiles('img/favicon.png')
site.profile_picture = staticfiles('img/mathias.jpg')
site.profile_bg = staticfiles('img/image_bk.jpg')

urlpatterns = [
    path('', index, name= 'index'),
    #path('admin/', admin.site.urls, name = 'admin'),
    path('admin/', include('material.admin.urls')),
    path('info/', blog, name='info'),
    path('blog/', blog_details, name='blog'),
    path('soon/', soon, name='soon'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('api/students/', include('students.api.urls')),
]

 # Static Files URLS
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
