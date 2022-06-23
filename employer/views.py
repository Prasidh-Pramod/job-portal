from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,ListView,CreateView,DetailView,UpdateView,DeleteView,FormView,TemplateView
from employer.forms import JobForm
from employer.models import Jobs
from employer.forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from employer.forms import LoginForm
from employer.forms import PasswordResetForm

from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class EmployerHomeView(View):
    def get(self,request):
        return render(request,"emp-home.html")

class AddJobView(CreateView):
    model=Jobs
    form_class=JobForm
    template_name="emp-addjob.html"
    success_url=reverse_lazy("emp-listjob")
    # def get(self,request):
    #     form=JobForm()
    #     return render(request,"emp-addjob.html",{"form":form})
    # def post(self,request):
    #     form=JobForm(request.POST)
    #     if form.is_valid():
    #         form.save()
            # jobname=form.cleaned_data.get("job_title")
            # cname=form.cleaned_data.get("company_name")
            # location=form.cleaned_data.get("location")
            # exp=form.cleaned_data.get("experience")
            # Jobs.objects.create(
            #     job_title=jobname,
            #     company_name=cname,
            #     location=location,
            #     experience=exp
            # )
        #     return render(request,"emp-home.html")
        # else:
        #     return render(request,"emp-addjob.html",{"form":form})

class ListJobView(ListView):
    model=Jobs
    context_object_name="jobs"
    template_name="emp-joblist.html"
    # def get(self,request):
    #     qs=Jobs.objects.all()
    #     return render(request,"emp-joblist.html",{"jobs":qs})

class Jobdetail(DetailView):
    model=Jobs
    context_object_name = "job"
    template_name = "emp-jobdetail.html"
    pk_url_kwarg = "id"
    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     return render(request,"emp-jobdetail.html",{"job":qs})

class JobEditView(UpdateView):
    model=Jobs
    form_class = JobForm
    template_name = "emp-jobedit.html"
    success_url = reverse_lazy("emp-listjob")
    pk_url_kwarg = "id"
    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     form=JobForm(instance=qs)
    #     return render(request,"emp-jobedit.html",{"form":form})
    # def post(self,request,id):
    #     qs = Jobs.objects.get(id=id)
    #     form=JobForm(request.POST,instance=qs)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("emp-listjob")
    #     else:
    #         return render(request,"emp-jobedit.html",{"form":form})
class JobDeleteView(DeleteView):
    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     qs.delete()
    #     return redirect("emp-listjob")
    model=Jobs
    template_name = "emp-jobdelete.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("emp-listjob")

class SignUpView(CreateView):
    model=User
    form_class= SignUpForm
    template_name= "usersignup.html"
    success_url = reverse_lazy("emp-listjob")

class SignInView(FormView):
    form_class=LoginForm
    template_name = "Login.html"

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)

            if user:
                login(request,user)
                return redirect("emp-listjob")
            else:
                return render(request,"login.html",{"form":form})

def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

class ChangePasswordView(TemplateView):
    template_name = "changepassword.html"
    def post(self,request,*args,**kwargs):
        pwd=request.POST.get("pwd")
        uname=request.user
        user=authenticate(request,username=uname,password=pwd)
        if user:
            return redirect("password-reset")
        else:
            return render(request,self.template_name)

class PasswordResetView(TemplateView):
    # form_class= PasswordResetForm
    template_name= "passwordreset.html"
    def post(self,request,*args,**kwargs):
        pwd1=request.POST.get("pwd1")
        pwd2 = request.POST.get("pwd2")
        if pwd1!=pwd2:
            return render(request,self.template_name,{'msg':"incorrect password"})
        else:
            u=User.objects.get(username=request.user)
            u.set_password(pwd1)
            u.save()
            return redirect("signin")

