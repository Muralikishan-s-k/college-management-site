from django.urls import path,include
from .import views
urlpatterns = [
   path('',views.loginhome,name='loginhome'),
   path('admin_login',views.admin_login,name='admin_login'),
   path('admin_home',views.admin_home,name='admin_home'),
   path('user_home',views.user_home,name='user_home'),
   path('logout',views.logout,name='logout'),
   path('showteacher',views.showteacher,name='showteacher'),
   path('addcourse',views.addcourse,name='addcourse'),
   path('addstudent',views.addstudent,name='addstudent'),
   path('addteacher',views.addteacher,name='addteacher'),
   path('showstudent',views.showstudent,name='showstudent'),
   path('add_course',views.add_course,name='add_course'),
   path('add_coursedb',views.add_coursedb,name='add_coursedb'),
   path('add_student',views.add_student,name='add_student'),
   path('add_studentdb',views.add_studentdb,name='add_studentdb'),
   path('show_details',views.show_details,name="show_details"),
   path('user_register',views.user_register,name="user_register"),
   path('edit/<int:pk>',views.edit,name='edit'),
   path('editdb/<int:pk>',views.editdb,name='editdb'),
   path('showprofile/<int:pk>',views.showprofile,name='showprofile'),
   path('goback',views.goback,name='goback'),
   path('signup',views.signup,name='signup'),
   path('edit_teacher/<int:pk>',views.edit_teacher,name='edit_teacher'),
   path('editteacher/<int:pk>',views.editteacher,name='editteacher'),
   path('delete/<int:pk>',views.delete,name='delete'),
   path('delete1/<int:pk>',views.delete1,name='delete1')
]