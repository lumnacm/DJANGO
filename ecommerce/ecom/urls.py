from django.urls import path,include
from.import views
urlpatterns = [
     path('',views.index,name='home'),
     path('about',views.about,name='about'),
     path('department',views.department_view,name='department'),
     path('registration',views.registration_view,name='registration'),
     path('login',views.login_view,name='login'),
     path('dashboard',views.dashboard_view,name='dashboard'),
     path('student',views.student,name='student'),
     path('add-student/',views.add_student,name='add-student'),
]
