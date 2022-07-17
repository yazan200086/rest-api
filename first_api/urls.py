from django.urls import path,include
from first_api import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('hello-viewset',views.helloViewsets,base_name='hello-viewset')
urlpatterns=[

 path('hello-view/',views.hello.as_view()),
 path('',include(router.urls))
]
