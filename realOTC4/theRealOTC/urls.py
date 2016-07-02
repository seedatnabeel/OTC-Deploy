from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^symptoms/', include('symptoms.urls')),
    url(r'^causes/', include('causes.urls')),
    url(r'^meds/', include('meds.urls')),
    url(r'^contact/', include('contact.urls')),
]