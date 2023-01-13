from django.urls import path

from MasterApp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('slogin',views.stulog,name='stulog'),
    path('mlogin',views.masterlog,name='maslog'),
    path('s_register',views.sturegis,name='sr'),
    path('m_register',views.masregis,name='mr'),
    path('viewtask',views.task_view,name='viewtask'),
    path('taskassign',views.task_assign,name='givetask'),

    path('readstudent',views.read_student_login),
    path('readmaster',views.read_master_login),
    path('read_s_reg',views.read_student_register),
    path('read_m_reg',views.read_master_register),
    path('givetask',views.create_task),
    path('logout',views.log_out,name='logout'),
    path('solve/<int:id>',views.solve,name='solve')
]