from django.urls import path
from employer import views

urlpatterns = [
 path("home",views.EmployerHomeView.as_view(),name="emp-home"),
 path('jobs/add',views.AddJobView.as_view(),name="emp-addjob"),
 path('jobs/all',views.ListJobView.as_view(),name="emp-listjob"),
 path('jobs/details/<int:id>',views.Jobdetail.as_view(),name="job-details"),
 path('jobs/change/<int:id>',views.JobEditView.as_view(),name="job-edit"),
 path('jobs/remove/<int:id>',views.JobDeleteView.as_view(),name="emp-deletejob"),
 path('users/accounts/signup',views.SignUpView.as_view(),name="signup"),
 path('users/accounts/signin',views.SignInView.as_view(),name="signin"),
 path('users/accounts/signout',views.signout_view,name="signout"),
 path('users/passwords/change',views.ChangePasswordView.as_view(),name="changepwd"),
 path('users/passwords/reset',views.PasswordResetView.as_view(),name="password-reset")
 ]