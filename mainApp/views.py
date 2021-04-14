from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

def signin(request):
     if request.method == "POST":
         uname=request.POST.get('uname')
         pwd=request.POST.get('password')
         user = auth.authenticate(username=uname, password=pwd)
         if user is not None:
             auth.login(request, user)
             if user.is_superuser:
                 return HttpResponseRedirect('/admin/')
             else:
                 auth.login(request,user)
                 return HttpResponseRedirect('/')
         else:
             return render(request,'signin.html')
     else:
         return render(request, 'signin.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def Jobsearch(request):
    if request.method == "POST":
        loc = request.POST.get("location")
        jsearch = request.POST.get("search")
        if loc=="" :
            job = Job.objects.filter(Q(title__icontains=jsearch))
        elif loc=="" and jsearch=="":
            job = Job.objects.all()
        elif jsearch=="" :
            job = Job.objects.filter(Q(location__icontains=loc))
        else:
            job = Job.objects.filter(Q(title__icontains=jsearch)&Q(location__icontains=loc))
        return render(request, "jobsearch.html",
                      {
                          "Job": job,
                          "count": len(job),
                      })
    else:
        job = Job.objects.all()
        return render(request,"jobsearch.html",
                {
                    "Job":job,
                    "count":len(job),
                })
@login_required(login_url='/signin/')
def myjobs(request):
    hr=Hruser.objects.get(uname=request.user)
    job=Job.objects.filter(hr=hr)
    company=hr.company
    return render(request,"myjobs.html",
    {
        "Job":job,
        "company":company,
    })
@login_required(login_url='/signin/')
def deletejob(request,num):
    user = User.objects.get(username=request.user)
    if user.is_superuser:
        return HttpResponseRedirect('/admin/')
    job=Job.objects.filter(id=num)
    job.delete()
    return HttpResponseRedirect("/job/")


@login_required(login_url='/signin/')
def profile(request):
    user = User.objects.get(username=request.user)
    if user.is_superuser:
        return HttpResponseRedirect('/admin/')
    else:
        hr = Hruser.objects.get(uname=request.user)
        if request.method=="POST":
            hr.name=request.POST.get("name")
            hr.email=request.POST.get("email")
            hr.company=request.POST.get("company")
            hr.uname=request.POST.get("uname")
            hr.phone=request.POST.get("name")
            hr.save()
            return HttpResponseRedirect('/')
        else:
            return render(request,"profile.html",
                          {
                              "HR":hr,
                          })

@login_required(login_url='/signin/')
def addjob(request):
    user=User.objects.get(username=request.user)
    if user.is_superuser :
        return HttpResponseRedirect("/admin/")
    else:
        if request.method=="POST":
            job=Job()
            job.title=request.POST.get("title")
            job.profile=request.POST.get("profile")
            job.type=request.POST.get("jobtype")
            job.location=request.POST.get("location")
            job.desc=request.POST.get("desc")
            pay=request.POST.get('payoutper')
            if pay=='month':
                job.payout =request.POST.get('payout')+" /month"
            elif pay=='hr':
                job.payout =request.POST.get('payout')+" /hr"
            else :
                job.payout =request.POST.get('payout')+" /year"
            c=Hruser.objects.get(uname=request.user)
            job.company=c.company
            job.hr=c
            job.save()
            return HttpResponseRedirect("/")
        else:
            return render(request,"addjob.html")

@login_required(login_url='/signin/')
def editjob(request,num):
    user=User.objects.get(username=request.user)
    if user.is_superuser :
        return HttpResponseRedirect("/admin/")
    else:
        job = Job.objects.get(id=num)
        if request.method=="POST":
            job.title=request.POST.get("title")
            job.profile=request.POST.get("profile")
            job.type=request.POST.get("jobtype")
            job.location=request.POST.get("location")
            job.desc=request.POST.get("desc")

            job.payout =request.POST.get('payout')

            hr=Hruser.objects.get(uname=request.user)
            hr.company=request.POST.get('company')
            job.company=hr.company
            job.hr=hr
            job.save()
            return HttpResponseRedirect("/")
        else:
            return render(request,"editjob.html",
                          {
                              "Job":job,
                          })

def signup(request):
    if request.method=="POST":
        hr=Hruser()
        hr.uname=request.POST.get('uname')
        hr.name=request.POST.get('name')
        hr.email=request.POST.get('email')
        hr.phone=request.POST.get('phone')
        hr.company=request.POST.get('company')
        pwd=request.POST.get('password')

        try:
            usr=User.objects.create_user(username=hr.uname,email=hr.email,password=pwd)
            hr.save()
            return HttpResponseRedirect('/job/')
        except:
            return render(request,"signup.html")

    else:
        return render(request, "signup.html")
