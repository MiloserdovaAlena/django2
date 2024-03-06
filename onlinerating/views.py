from django.shortcuts import render
from .models import ColleagueFeedback, EmployeeFeedback
from django.shortcuts import render, redirect
from .models import EmployeeFeedback, ManagerFeedback, SelfFeedback, ColleagueFeedback
from .forms import EmployeeFeedbackForm, ManagerFeedbackForm, SelfFeedbackForm, ColleagueFeedbackForm


def index(request):
    return render(request, 'onlinerating/index.html')


def feedback_view(request):
    colleague_feedback = ColleagueFeedback.objects.all()
    employee_feedback = EmployeeFeedback.objects.all()
    return render(request, 'onlinerating/feedback.html',
                  {'colleague_feedback': colleague_feedback, 'employee_feedback': employee_feedback})


def employee_feedback_view(request):
    if request.method == 'POST':
        form = EmployeeFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('onlinerating:employee_feedback')

    else:
        form = EmployeeFeedbackForm()

    feedbacks = EmployeeFeedback.objects.all()
    return render(request, 'onlinerating/employee_feedback.html', {'form': form, 'feedbacks': feedbacks})


def manager_feedback_view(request):
    if request.method == 'POST':
        form = ManagerFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('onlinerating:manager_feedback')

    else:
        form = ManagerFeedbackForm()

    feedbacks = ManagerFeedback.objects.all()
    return render(request, 'onlinerating/manager_feedback.html', {'form': form, 'feedbacks': feedbacks})


def self_feedback_view(request):
    if request.method == 'POST':
        form = SelfFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('onlinerating:self_feedback')

    else:
        form = SelfFeedbackForm()

    feedbacks = SelfFeedback.objects.all()
    return render(request, 'onlinerating/self_feedback.html', {'form': form, 'feedbacks': feedbacks})


def colleague_feedback_view(request):
    if request.method == 'POST':
        form = ColleagueFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('onlinerating:colleague_feedback')

    else:
        form = ColleagueFeedbackForm()

    feedbacks = ColleagueFeedback.objects.all()
    return render(request, 'onlinerating/colleague_feedback.html', {'form': form, 'feedbacks': feedbacks})
