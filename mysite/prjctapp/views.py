# -*- coding: cp1252 -*-
from django.shortcuts import *
from django.http import QueryDict
from django.http import HttpResponse,HttpResponseRedirect
from models import Upload,User
from django.template import RequestContext, loader
from forms import MessageForm,SignupForm,PicuploadForm
import time

def home(request):
    str="my home page"
    return HttpResponse(str)

def index(request):
    return render(request,'hello.html')

def message(request):
    return render(request, 'messages.html', {})

def signup(request):
    if request.method == 'GET':        
        form = SignupForm()        
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            user_entry = form.save()
            print '-----fffffffff---------'
            request.session["current_name"] = user_entry.user_name
            print request.session.get("current_name")
            request.session["current_password"] = user_entry.password
            print request.session.get("current_password")

        return render(request,'profile.html')    
##            request.session["current_password"] = user_entry.password
##            print request.session.get("current_password")
    
##            signup_entry = form.save()
##              return render(request,'profile.html', {'success':True})
    
##def profile(request):
##    form = ProfileForm(request.POST)
##    if form.is_valid():
##        profile_entry = form.save()
##        return render(request,'profile.html',)
##
def savemessage(request):
    form = MessageForm(request.POST)
    if form.is_valid():
        entry = form.save()
        return render(request, 'messages.html', {'success':True})
    
    return render(request, 'messages.html', {'success':True})	
    
def files(request):
    file_list = Upload.objects.all()
    print file_list 
    #template = loader.get_template('prjctapp/files.html')

    #context = RequestContext(request, {'file_list': file_list,})
    #return HttpResponse(template.render(context))
    context={'file_list':file_list}
    return render(request,'prjctapp/files.html',context)

def handle_uploaded_file(f):
    name = str(int(time.time()))+".jpg"
    with open(name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return name

def logout(request):
    print '-logging out-'
    request.session.flush()
    message="You Successfully Logged out!!!!"
    print 'Writing message ->'
    print message
    return HttpResponse(message)

def userprofile(request):
    
    context = {'success':True}
    
    if request.method == 'GET':
        form = SignupForm()
        pic = User.objects.get(id=1).user_photo.url
        print '---we got pic-----'
        print pic
        if(pic != "null"):
            print '----pic is null---'
            context['pic'] = pic
        
    else:
        print '--------------userprofp--------------------'
        Userface = User.objects.get(user_name=request.session.get("current_name"))
        userInstance = User.objects.get(pk=Userface)
        #user_name=request.session.get('current_name')
        form = PicuploadForm(request.POST,request.FILES, instance=userInstance)
##        form = SignupForm(request.POST,request.FILES)
        print form
        
        
        if form.is_valid():
            updateUser = form.save()
            print handle_uploaded_file(request.FILES['user_photo'])           
            print '-------------form validated---------------'
            
            
        else:
            print form.errors
            
    return render(request,'profile.html',{'success':True,'url':updateUser.user_photo.url})
    
            
