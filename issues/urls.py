from django.urls import path

from . import views

app_name = 'issues'
urlpatterns = [
    path('', views.index, name='index'),
    path('view/<int:issue_id>', views.detail_issue, name='detail_issue'),
    path('add_issue', views.add_issue, name='add_issue'),
    path('<int:issue_id>/add_issue', views.add_issue, name='add'),
    path('edit/<int:issue_id>', views.edit_issue, name='edit_issue'),
    path('delete/<int:issue_id>', views.delete_issue, name='delete_issue'),
]
