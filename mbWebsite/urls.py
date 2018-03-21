"""mbWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from myProfile import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'', include('myProfile.urls'), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^about/', views.about, name="about"),
    url(r'^projects/', views.projects, name="projects"),
    url(r'^contact/', views.contact, name="contact"),
    url(r'^blog/view/(?P<slug>[^\.]+).html', views.view_post, name='view_blog_post'),
    url(r'^blog/category/(?P<slug>[^\.]+).html',views.view_category, name='view_blog_category'),
    url(r'^blog/', views.blog, name="blog"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
