from django.urls import path

from . import views

app_name = 'onlinerating'
urlpatterns = [
    path('', views.index, name='index'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('feedback/employee/', views.employee_feedback_view, name='employee_feedback'),
    path('feedback/manager/', views.manager_feedback_view, name='manager_feedback'),
    path('feedback/self/', views.self_feedback_view, name='self_feedback'),
    path('feedback/colleague/', views.colleague_feedback_view, name='colleague_feedback'),
]
