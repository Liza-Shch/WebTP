from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from questions.forms import *
from questions import models


def base_view(request):
    return render(request, 'base.html', {
        'user': request.user,
    })

def paginate(objects_list, request):
    paginator = Paginator(objects_list, 30)
    page = request.GET.get('page')
    objects_page = paginator.get_page(page)
    return objects_page

def index_view(request):
    questions_list = models.Question.objects.new_questions()
    questions = paginate(questions_list, request)
    return render(request, 'index.html', {
        'objects': questions
    })

def hot_view(request):
    questions_list = models.Question.objects.hot_questions()
    questions = paginate(questions_list, request)
    return render(request, 'hot.html', {
        'objects': questions
    })

def question_view(request, question_id):
    question = get_object_or_404(models.Question.objects, pk=question_id)
    answers = paginate(question.answers(), request)
    error = ""
    if request.POST:
        form = AnswerForm(author=request.user.profile, question=question, data = request.POST)
        if form.is_valid():
            answer = form.save()
            return redirect(
               reverse('question', args=[question.pk])
            )
        else:
            error = "Incorrect data"
    else:
        #if request.user.is_authenticated:
        form = AnswerForm(author=request.user.profile, question=question)
        #else:
        #    form = None
    return render(request, 'question.html', {
        'question' : question,
        'objects' : answers,
        'form' : form,
        'error' : error
    })

def tag_view(request, tag_text):
    tag = get_object_or_404(models.Tag.objects, tag=tag_text)
    questions = paginate(tag.questions(), request)
    return render(request, 'tag.html', {
        'objects': questions,
        'tag' : tag_text
    })

def logout(request, next):
    auth.logout(request)
    return redirect(next)

def login_view(request, next):
    error = ""
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            cdata = form.cleaned_data
            user = auth.authenticate(request, username=cdata['username'], password=cdata['password'])
            if user is not None:
                auth.login(request, user)
                return redirect(next)
        error = "Incorrect data"
    else:
        form = LoginForm()
    return render(request, 'login1.html', {
        'title' : "Login",
        'form' : form,
        'error' : error,
    })

def signup_view(request):
    error = ""
    if request.POST:
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            cdata_user = user_form.clean()
            cdata_profile = profile_form.clean()  
            user = User.objects.create_user(cdata_user['username'], cdata_user['email'], cdata_user['password'])
            auth.login(request, user)
            Profile.objects.create(user=user, nickname=cdata_profile['nickname'])
            redirect(reverse('index'))
        else:
            error = "Incorrect data"
    else:
        user_form = SignUpForm()
        profile_form = ProfileForm(instance=User.objects.all()[0])
    return render(request, 'signup1.html', {
        'title' : "SignUp",
        'form' : user_form,
        'profile_form' : profile_form,
        'error' : error
    })

@login_required(redirect_field_name='/login')
def settings_view(request):
    error = ""
    user = request.user
    if request.POST:
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('settings')
        else:
            error = "Incorrect data"
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=user.profile)
    return render(request, 'settings.html', {
        'form' : user_form,
        'profile_form' : profile_form,
        'error' : error
    })

@login_required
def ask_view(request):
    error = ""
    if request.POST:
        form = QuestionForm(request.user.profile, data = request.POST)
        if form.is_valid():
            try:
                question = form.save()
                return redirect(
                    reverse('question', args=[question.pk])
                )
            except:
                error = "Tag does not exist"
        else:
            error = "Incorrect data"
    else:
        form = QuestionForm(request.user.profile)
    return render(request, 'ask.html', {
        'form' : form,
        'error' : error,
    })
