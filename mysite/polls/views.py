from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout as lgOut
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login
# Create your views here.



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list,'logged':request.user.is_authenticated}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {"question":question,'logged':request.user.is_authenticated})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question,'error_message':'You Didn\'t select a choice','logged':request.user.is_authenticated})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, selected_choice.id)))

def account(request):
    currentUser = request.user
    logged = currentUser.is_authenticated
    if logged:
        return render(request, 'polls/account.html', {'logged':logged, 'user':currentUser})
    else:
        return HttpResponseRedirect(reverse('polls:index'))


def results(request, question_id, user_choice_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question,'user_choice':user_choice_id,'logged':request.user.is_authenticated})

def logout(request):
    lgOut(request)
    return render(request, 'polls/logout.html', {'logged':False})

def signIn(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('polls:index'))
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Success logging in
                return HttpResponseRedirect(reverse('polls:index'))
            else:
                # Error logging in
                return render(request,'polls/signIn.html', {'logged':False,'form':form})
        else:
            # Error logging in
            return render(request,'polls/signIn.html', {'logged':False,'form':form})
    form = AuthenticationForm()
    return render(request,'polls/signIn.html', {'logged':False,'form':form})