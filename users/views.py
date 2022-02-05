from contextlib import redirect_stderr
import csv
from itertools import count
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .models import Result10Count, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import After10, After12Arts, After12Commerce, After12Science ,After10colleges, After12engcolleges, After12medicolleges,After12commcolleges,After12artscolleges,result,result12arts,result12comm,result12sci
from .forms import SignUpForm, LoginForm
from django.db.models.query_utils import DeferredAttribute
# Create your views here.

def home(request):
    count=User.objects.count()
    context={
        'count':count,
    }
    return render(request,'home.html',context)

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email= form.cleaned_data.get("email")
            password= form.cleaned_data.get("password")
            try:
                user= User.objects.get(email=email, password=password)
                print(user.email)
                print(user.password)
                messages.info(request, "You are now logged in as {user.email}.")
                # messages.INFO(request, f"You are now logged in as {email}.")
                return redirect("home")
            except User.DoesNotExist:
                print("Invalid user!!")
        messages.error(request,"Invalid username or password.")
        return redirect('signup')
    else:
        print("method != POST")
        form=  LoginForm()
        context = {
            'form':form,

        }
        return render(request, 'registration/login.html', context)
    
def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful." )
            return redirect('login')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form=  SignUpForm()
    context = {
        'form':form,
    }
    return render(request,'registration/signup.html',context)

def get_questions():
    questions=After10.objects.all();
    return questions
def after10(request):
    questions=After10.objects.all();
    # for question in questions:
    #     print(question.id);
    context={
        'questions':questions
    }
    return render(request, 'after10.html',context)



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression

def after10result(request):
    if request.method == "POST":
        flag=False
        questions=get_questions();
        form=request.POST.get("after10form")
        username = User.email
        count_arts=0
        count_science=0
        count_comm=0

        # response = HttpResponse(content_type='text/csv')  
        # response['Content-Disposition'] = 'attachment; filename="file.csv"'  
        results = pd.DataFrame()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=file.csv'
        results.to_csv(path_or_buf=response,sep=';',float_format='%.2f',index=False,decimal=",")
        writer = csv.writer(response)  
        writer.writerow(['question', 'answer', 'username', 'question_type'])

        for question in questions:
            #print(question.id)
            # user_id = result.objects.get(user_id = user_id)
            # ip = User.objects.get() # query the InsertIp object
            # user = User.user # get the user using a . operator
            q_id=question.id
            option_selected=request.POST.get(str(q_id))
            type=question.question_type
            print(q_id, option_selected,type)
            
            if(q_id != None and option_selected!= None):
                ans = result(question = q_id,answer = option_selected,username = username,question_type=type )
                writer.writerow([q_id, option_selected, username, type])
                option_selected=int(option_selected)
                if(type=='C'):
                    count_comm=count_comm+option_selected
                if(type=='A'):
                    count_arts=count_arts+option_selected
                if(type=='S'):
                    count_science=count_science+option_selected
                ans.save()
                flag=True
        # email= form.cleaned_data.get("email")
        # password= form.cleaned_data.get("password")
    
        # user= User.objects.get(email=email, password=password)
        # print(user.email)
        # print(user.password)
        countResult=Result10Count(username=username,count_science=count_science,count_arts=count_arts,count_commerce=count_comm)   
        countResult.save()
        print(count_arts,count_comm,count_science)
        print(username)
        print(User.email) 

        # def getfile(request):  
        # response = HttpResponse(content_type='text/csv')  
        # response['Content-Disposition'] = 'attachment; filename="file.csv"'  
        # writer = csv.writer(response)  
        # writer.writerow(['Username', 'Science', 'Commerce', 'Arts'])  
        # writer.writerow([username, count_science, count_comm, count_arts]) 
        foo = response.content.decode('utf-8')
        import io
        reader = csv.reader(io.StringIO(foo))
        dataset = pd.read_csv(io.StringIO(foo))
        X = dataset.iloc[:, :1].values #get a copy of dataset exclude last column
        y = dataset.iloc[:, 1].values #get array of dataset in column 1st
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)
        viz_train = plt
        plt.xticks([1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])  
        plt.yticks([0,1,2])  
        # categories = np.array([0, 2, 1, 1, 1, 2, 0, 0])
        # colormap = np.array(['r', 'g', 'b'])
        # ax[0].scatter(op_table.index,op_table['num_orders'],color='pink') 
        viz_train.scatter(X_train, y_train, color='red')
        # viz_train.bar(center_table.index,center_table['num_orders'],alpha=0.7,color='orange',width=0.5) 
        viz_train.plot(X_train, regressor.predict(X_train), color='blue')
        viz_train.title('Marks VS Question No')
        viz_train.xlabel('Question No')
        viz_train.ylabel('Marks')
        viz_train.show()

        # return response  
           
    return render(request, "after10result.html", {'flag': flag,'science':count_science,'comm':count_comm,'arts':count_arts,})
    
    


def get_questions12arts():
    questions=After12Arts.objects.all();
    return questions
def after12arts(request):
    questions=After12Arts.objects.all()
    context={
        'questions':questions
    }
    return render(request, 'after12arts.html',context)
def after12artsresult(request):
    if request.method == "POST":
        flag=False
        questions=get_questions12arts();
        form=request.POST.get("after12form")
        username = User.email
        for question in questions:
            #print(question.id)
            # user_id = result.objects.get(user_id = user_id)
            # ip = User.objects.get() # query the InsertIp object
            # user = User.user # get the user using a . operator
            q_id=question.id
            option_selected=request.POST.get(str(q_id))
            print(q_id, option_selected)
            if(q_id != None and option_selected!= None):
                ans = result12arts(question = q_id,answer = option_selected,username = username )
                ans.save()
                flag=True   
        print(username)      
    return render(request, "after12artsresult.html", {'flag': flag})
    
def get_questions12comm():
    questions=After12Commerce.objects.all();
    return questions
def after12commerce(request):
    questions=After12Commerce.objects.all()
    context={
        'questions':questions
    }
    return render(request, 'after12comm.html',context)
def after12commresult(request):
    if request.method == "POST":
        flag=False
        questions=get_questions12comm();
        form=request.POST.get("after12form")
        username = User.email
        for question in questions:
            #print(question.id)
            # user_id = result.objects.get(user_id = user_id)
            # ip = User.objects.get() # query the InsertIp object
            # user = User.user # get the user using a . operator
            q_id=question.id
            option_selected=request.POST.get(str(q_id))
            print(q_id, option_selected)
            if(q_id != None and option_selected!= None):
                ans = result12comm(question = q_id,answer = option_selected,username = username )
                ans.save()
                flag=True   
        print(username)      
    return render(request, "after12commresult.html", {'flag': flag})
    
def get_questions12sci():
    questions=After12Science.objects.all();
    return questions
def after12science(request):
    questions=After12Science.objects.all()
    context={
        'questions':questions
    }
    return render(request, 'after12sci.html',context)
def after12sciresult(request):
    if request.method == "POST":
        flag=False
        questions=get_questions12sci();
        form=request.POST.get("after12form")
        username = User.email
        for question in questions:
            #print(question.id)
            # user_id = result.objects.get(user_id = user_id)
            # ip = User.objects.get() # query the InsertIp object
            # user = User.user # get the user using a . operator
            q_id=question.id
            option_selected=request.POST.get(str(q_id))
            print(q_id, option_selected)
            if(q_id != None and option_selected!= None):
                ans = result12sci(question = q_id,answer = option_selected,username = username )
                ans.save()
                flag=True   
        print(username)      
    return render(request, "after12sciresult.html", {'flag': flag})
    
def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def logout(request):
    messages.info(request, "You have successfully logged out.") 
    redirect("login")
  
def after10colleges(request):
    colleges = After10colleges.objects.all()
    context={
        'colleges':colleges
    }
    return render(request, 'after10colleges.html',context)

def after12engcolleges(request):
    colleges = After12engcolleges.objects.all()
    context={
        'colleges':colleges
    }
    return render(request, 'after12engcolleges.html',context)

def after12medicolleges(request):
    colleges = After12medicolleges.objects.all()
    context={
        'colleges':colleges
    }
    return render(request, 'after12medicolleges.html',context)


def after12commcolleges(request):
    colleges = After12commcolleges.objects.all()
    context={
        'colleges':colleges
    }
    return render(request, 'after12commcolleges.html',context)


def after12artscolleges(request):
    colleges = After12artscolleges.objects.all()
    context={
        'colleges':colleges
    }
    return render(request, 'after12artscolleges.html',context)

