from django.conf.urls import url
from test_app import views

# Template name
app_name = 'test_app'

urlpatterns = [
    url(r'^relative/', views.relative_url, name='relative_url'),
    url(r'^other/', views.other, name='other')
]
