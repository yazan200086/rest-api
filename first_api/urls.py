from django.urls import path
from first_api import views
urlpatterns=[

 path('hello-view/',views.hello.as_view())
]
