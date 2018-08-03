from django.conf.urls import url
from . import views

urlpatterns = [
url(r'add_book$', views.add_book),
url(r'show_books$', views.show_books),
url(r'del_book$', views.del_book),
url(r'search_books$', views.search_books),
url(r'edit_book$', views.edit_book),
]