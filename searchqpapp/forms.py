from django import forms
from .models import QuestionPaper


class SubjectForm(forms.ModelForm):
    class Meta:
        model = QuestionPaper
        fields = ['subject', 'questionPaperModel', 'description', 'fileImage', 'filePdfField']
