
from django.contrib import admin
from django.urls import path, include
from books import views as books_views

urlpatterns = [
    path('', books_views.homepage, name='home'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('books/', books_views.book_list, name='book_list'),
    path("categ/<slug:slug>", books_views.show_categ, name="show_categ"),
    path("admin/", admin.site.urls),
]
