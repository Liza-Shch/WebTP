from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import auth
from django.contrib.auth.decorators import login_required
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
    return render(request, 'question.html', {
        'question' : question,
        'objects' : answers
    })

def ask_view(request):
    return render(request, 'ask.html')

def tag_view(request, tag_text):
    tag = get_object_or_404(models.Tag.objects, tag=tag_text)
    questions = paginate(tag.questions(), request)
    return render(request, 'tag.html', {
        'objects': questions,
        'tag' : tag_text
    })

def logout(request):
    auth.logout(request)

def login_view(request):
    if request.POST:
        error = ""
        form = LoginForm(request.POST)
        if form.is_valid():
            cdata = form.cleaned_data
            user = auth.authenticate(request, username=cdata['username'], password=cdata['password'])
            if user is not None:
                auth.login(request, user)
                return redirect(request.GET.get('next') if request.GET.get('next') else 'index')
        else:
            error = "Uncorrect data"
    else:
        form = LoginForm()
    return render(request, 'login1.html', {
        'form' : form,
        'error' : error
    })

def signup_view(request):
    if request.POST:
        error = ""
        form = SignUp(request.POST)
        if form.is_valid():
            cdata = form.clean
            user = User.create_user(username=cdata['username'], email=cdata['email'], password=cdata['password'])
            auth.login(request, user)
            profile = Profile.create_user(user=user, avatar=cdata['avatar'], nickname=cdata['nickname'])
            redirect(reverse('index'))
        else:
            error = "Username or nickname already exists"
    else:
        form = SignUpForm()
    return render(request, 'sighup1.html', {
        'form' : form,
        'error' : error
    })

@login_required
def settings_view(request):
    user = request.user
    form = SettingsForm(instance=user)
    if request.POST:
        form = SettingsForm(instance=user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('settings')
    return render(request, 'settings.html', {
        'form' : form,
    })


# dgango-widget-twix
#@login_required (login_url )
#def ask1(request):
#    if request.POST:
#        form = QuestionForm(request.user, data = request.POST)
#        if form.is_valid():
#            question = form.save()
#            return redirect(
#                reverse('question', kwargs=[pk: question.pk])
#            )