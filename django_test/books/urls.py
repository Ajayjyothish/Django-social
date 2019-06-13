from django.contrib import admin
from django.urls import path

from .views import all_book_view,raw_form_view,thank_view

app_name= 'books'
urlpatterns = [
    path('',all_book_view,name="allBook"),
    path('form/',raw_form_view,name='form'),
    path('thanks/', thank_view)
]
