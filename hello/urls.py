import view as view
from django.urls import path
from hello import views


from . import views

urlpatterns = [

    path("show",views.display,name="display"),
    path('display',views.form,name="form"),




]