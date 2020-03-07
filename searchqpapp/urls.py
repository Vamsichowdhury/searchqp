
from django.urls import path
from .views import BranchListView, BranchDetailView, SubjectDetailView, SubjectCreateView, MyDeleteView

app_name = 'searchqpapp'

urlpatterns = [
    path('branch/', BranchListView.as_view(), name='branch-list'),
    path('<int:pk>/subjects/', BranchDetailView.as_view(), name='branch-detail'),
    path('<int:pk>/question_papers/', SubjectDetailView.as_view(),name='subject-detail'),
    path("createSubject/", SubjectCreateView.as_view(), name='subject-create-form'),
    path("qpDelete/<int:pk>/", MyDeleteView.as_view(), name='delete-Question-paper'),

    ]
