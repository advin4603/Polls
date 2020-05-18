from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('logout/',views.logout, name='logout'),
    path('signIn/',views.signIn, name='signIn'),
    path('register/',views.register, name='register'),
    path('create/',views.create, name='create'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/<int:user_choice_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('account/<int:user_id>/',views.otherAccount,name='otherAccount')
]

