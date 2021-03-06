"""reading_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'books.views.home', name='home'),
    url(r'^25/$', 'books.views.top25', name='top25'),
    url(r'^(?P<book_id>\d+)/$', 'books.views.detail', name='detail'),
    url(r'^register/$', 'books.views.register', name='register'),
    url(r'^register/success/$', 'books.views.register_success', name='register_success'),
    url(r'^login/$', 'books.views.user_login', name='user_login'),
    url(r'^logout/$', 'books.views.user_logout', name='user_logout'),
    url(r'^account/success/$', 'books.views.set_account_success', name='set_account_success'),
    url(r'^account/(?P<username_slug>[\w\@\.\+\-\_]+)/$', 'books.views.set_account', name='set_account'),
    url(r'^(?P<laber_title>.*)/$', 'books.views.laber_detail', name='laber'),
]
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('books.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)