from django.shortcuts import render, redirect
from .models import Question, Choice
from .forms import formQuestion, formChoice
from django.core.paginator import Paginator

def index(request):
    return render(request, 'app/index.html')

def startQuiz(request, pk):
    questions = Question.objects.all()
    questions = Paginator(questions, 1)
    cur_page = questions.page(pk)
    q = Question.objects.get(question_text=cur_page.object_list[0])
    choices = Choice.objects.filter(question=q)
    context = {
        'questions': cur_page.object_list[0],
        'choices': choices,
        'pageRange': questions.page_range
    }
    return render(request, 'app/quiz.html', context)

def updateQuestion(request):
    form = formQuestion()
    if request.method == 'POST':
        form = formQuestion(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'app/update_question.html', {'form': form})

def updateChoice(request):
    form = formChoice()
    if request.method == 'POST':
        question = request.POST['question']
        question = Question.objects.get(pk=question)
        print(question.choice_set.count())
        if(question.choice_set.count() > 3):        # chi duoc update 4 choices
            return redirect('update-choice')
        else:
            form = formChoice(request.POST)
            if form.is_valid():
                form.save()
    return render(request, 'app/update_choice.html', {'form': form})