from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def base_view(request):
    return render(request, 'base.html')

def paginate(objects_list, request):
    paginator = Paginator(objects_list, 5)
    page = request.GET.get('page')
    objects_page = paginator.get_page(page)
    return objects_page

def index_view(request):
    questions_list = []
    for i in range(1,30):
        questions_list.append({
            "title": "title " + str(i),
            "id": i,
            "text": "text" + str(i)
        })
    tags_list = []
    for i in range(1, 4):
        tags_list.append(
            "tag" + str(i)
        )
    questions = paginate(questions_list, request)
    return render(request, 'index.html', {
        'objects': questions,
        'tags' : tags_list
    })

def question_view(request, question_id):
    questions = []
    for i in range(1,30):
        questions.append({
            "title": "title " + str(i),
            "id": i,
            "text": "text" + str(i)
    })
    answers_list = []
    for i in range(1, 30):
        answers_list.append({
            "text" : "answer" + str(i),
            "id" : i,
            "text" : "answer" + str(i)
        })
    question = questions[question_id - 1]
    answers = paginate(answers_list, request)
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
    questions_list = []
    for i in range(1,30):
        questions_list.append({
            "title": "Hottitle " + str(i),
            "id": i,
            "text": "text" + str(i)
        })
    tags_list = []
    for i in range(1, 4):
        tags_list.append(
            "tag" + str(i)
        )
    questions = paginate(questions_list, request)
    return render(request, 'hot.html', {
        'objects': questions,
        'tags' : tags_list
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
