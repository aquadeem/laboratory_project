from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from laboratory.forms import IndexForm
from laboratory.models import Student
from django.urls import reverse_lazy


class IndexView(View):

    def get(self, request):
        return render(request, 'index.html', {
            'form': IndexForm(),
        })


    def post(self, request):
        form = IndexForm(request.POST)
        if form.is_valid():
            student = Student()
            student.first_name = form.cleaned_data['first_name']

            student.save()

            return HttpResponse('Saved')

        return HttpResponse('Not Saved')


class StudentListView(ListView):

    model = Student
    template_name = 'student/list_student.html'


class StudentListDetail(DetailView):

    model = Student
    template_name = 'student/info_student.html'


class StudentListUpdate(UpdateView):

    model = Student
    fields = ['first_name']
    template_name = 'student/update_student.html'
    success_url = reverse_lazy('list_student')


class StudentListDelete(DeleteView):

    model = Student
    template_name = 'student/delete_student.html'
    success_url = reverse_lazy('list_student')

class StudentListAdd(CreateView):

    model = Student
    fields = ['first_name']
    template_name = 'student/add_student.html'
    success_url = reverse_lazy('list_student')


def base_template(request):
    return render(request, 'base.html')


def get_reset_password(request):
    return render(request, 'email/reset_password.html')


def get_welcome_email(request):
    return render(request, 'email/welcome_email.html')


def get_email_verification(request):
    return render(request, 'email/email_verification.html')
