from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tables_index/', views.tables_index, name='tables_index'),
    path('tables/<int:table_id>/', views.table_detail, name='table_detail'),
    path('tables/new', views.table_new, name='table_new'),
    path('tables/<int:table_id>/close', views.table_close, name='table_close')
]
# Account URLS
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']