"""csrt URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from record_data import views
from record_data import api

urlpatterns = [
    # Homepage
	url(r'^$', views.home),

    # Exporting Data
	url(r'^export/$', views.data),
    url(r'^export/compiled/$', views.data_compiled),
    url(r'^export/time/$', views.data_time),
    url(r'^export/errors/$', views.data_errors),

    # Editing data
	url(r'^data/$', views.data_list),
	url(r'^data/edit/(?P<id>[0-9]+)/$', views.data_edit),

    # API
	url(r'^add/trial$', api.add_trial),
	url(r'^edit/data', api.edit_data),

    # Admin page
    url(r'^admin/', admin.site.urls),
]
