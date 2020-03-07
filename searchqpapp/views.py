from django.shortcuts import redirect, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Branch, Subject, QuestionPaper
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SubjectForm
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib import messages


class BranchListView(LoginRequiredMixin, ListView):
    model = Branch
    template_name = 'searchqpapp/branch_list.html'
    context_object_name = 'branches'


class BranchDetailView(LoginRequiredMixin, DetailView):
    model = Branch
    template_name = 'searchqpapp/branch_detail.html'
    context_object_name = 'branches'


class SubjectDetailView(LoginRequiredMixin, DetailView):
    model = Subject
    template_name = 'searchqpapp/subject_detail.html'
    context_object_name = 'subjects'


class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = QuestionPaper
    form_class = SubjectForm
    template_name = 'searchqpapp/subject_create.html'
    context_object_name = 'form'

    def get_success_url(self):
        subject = self.object.subject
        return reverse_lazy('searchqpapp:subject-detail', kwargs={'pk': subject.pk})

    def form_valid(self, SubjectForm):
        SubjectForm.instance.author = self.request.user
        return super().form_valid(SubjectForm)


class MyDeleteView(DeleteView):
    model = QuestionPaper
    template_name = 'searchqpapp/qp_delete.html'

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(MyDeleteView, self).get_object()
        if obj.author == self.request.user:
            return obj
        else:
            raise Http404

    def get_success_url(self):
        subject = self.object.subject
        return reverse_lazy('searchqpapp:subject-detail', kwargs={'pk':subject.pk})

# def deleteQp(request, pk):
#     qp = QuestionPaper.objects.get(pk=pk)
#     if request.user == qp.author:
#         QuestionPaper.objects.filter(id=pk).delete()
#         messages.success(request, f'tweet is deleted')
#         subject = QuestionPaper.object.subject
#         return reverse_lazy('subject-detail', kwargs={'pk': subject.pk})
#
#     else:
#         return HttpResponse("you cannot delete this question paper")
#         # subject = QuestionPaper.object.subject
#         # messages.warning(request, f'you cannot have access to delete this tweet')
#         # return reverse_lazy('subject-detail', kwargs={'pk': subject.pk})
