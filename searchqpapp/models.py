from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from django.urls import reverse_lazy

class Branch(models.Model):
    branchName = models.CharField(max_length=100)

    def __str__(self):
        return self.branchName


class Subject(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    subjectName = models.CharField(max_length=100)

    def __str__(self):
        return self.subjectName


class QuestionPaper(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    questionPaperModel = models.CharField(max_length=10)  # CIA1,CIA2,MODEL,SEM
    description = models.TextField()
    date = models.DateTimeField(default=now())
    fileImage = models.ImageField(upload_to="searchqpapp/images")
    filePdfField = models.FileField(upload_to="searchqpapp/pdf")

    def __str__(self):
        return self.questionPaperModel

    def get_success_url(self):
        subject = self.object.subject
        return reverse_lazy('subject-detail', kwargs={'pk': subject.pk})
