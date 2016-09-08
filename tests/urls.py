from django.conf.urls import include

urlpatterns = [
    (r'^markdown/', include('django_markdown.urls')),
]
