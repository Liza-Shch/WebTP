from django.shortcuts import render, redirect, reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import auth
from django.contrib.auth.decorators import login_required
#from questions.forms import LoginForm, QuestionForm
from questions import models


def base_view(request):
    return render(request, 'base.html')

def paginate(objects_list, request):
    paginator = Paginator(objects_list, 5)
    page = request.GET.get('page')
    objects_page = paginator.get_page(page)
    return objects_page

def index_view(request):
    questions_list = models.Question.objects.new_questions()
    questions = paginate(questions_list, request)
    return render(request, 'index.html', {
        'objects': questions
    })

def question_view(request, question_id):
    question = models.Question.objects.get(pk=question_id)
    answers = paginate(question.answers(), request)
    return render(request, 'question.html', {
        'question' : question,
        'objects' : answers
    })

def ask_view(request):
    return render(request, 'ask.html')

def login_view(request):
    form_items = [
        {"label": "Login", "type_item": "text"},
        {"label": "Password", "type_item": "password"}
    ]
    return render(request, 'login.html', {
        'form_items' : form_items
    })

def signup_view(request):
    form_items = [
        {"label": "Login", "type_item": "text"},
        {"label": "Email", "type_item": "email"}, 
        {"label": "Nickname", "type_item": "text"},
        {"label": "Password", "type_item": "password"},
        {"label": "Repeat password", "type_item": "password"}
    ]
    return render(request, 'signup.html', {
        'form_items' : form_items
    })

def settings_view(request):
    form_items = [
        {"label": "Login", "type_item": "text"},
        {"label": "Email", "type_item": "email"}, 
        {"label": "Nickname", "type_item": "text"}
    ]
    return render(request, 'settings.html', {
        'form_items' : form_items
    })

def hot_view(request):
    question_list = models.Question.objects.hot_questions()
    questions = paginate(questions_list, request)
    return render(request, 'hot.html', {
        'objects': questions
    })

def tag_view(request, tag):
    questions_list = []
    for i in range(1,30):
        questions_list.append({
            "title": "title " + str(i),
            "id": i,
            "text": tag
    })
    tags_list = []
    for i in range(1, 4):
        tags_list.append(
            "tag" + str(i)
        )
    questions = paginate(questions_list, request)
    return render(request, 'tag.html', {
        'objects': questions,
        'tags' : tags_list,
        'tag' : tag
    })

def logout(request):
    return redirect(reverse('index'))

def login1(request):
    if request.PoST:
        form = LoginForm(request.POST)
        if form.is_valid():
            cdata = form.clean_data
            user = auth.authenticate(
                username = cdata['username'],
                password = cdata['password'],
            )
            if user is not None:
                auth.login1(request, user)
    else:
        form = LoginForm()
    return render(request, 'login1.html', {
        'form' : form
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