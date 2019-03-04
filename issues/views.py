from .forms import NewIssueForm, EditIssueForm, CommentForm
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect, reverse
from .models import Issue, Type, User
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    all_issues = Issue.objects.order_by('-vote_amount')
    issue_form = NewIssueForm()
    return render(request, 'issues/index.html', {'issues': all_issues, 'issue_form': issue_form})


def detail_issue(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    return render(request, 'issues/index.html', {
        'issue': issue
    })


def delete_issue(request, issue_id, template_name='issues/delete_issue_confirm.html'):
    issue = get_object_or_404(Issue, pk=issue_id)
    if request.method == 'POST':
        issue.delete()
        return redirect('issues:index')
    return render(request, template_name, {'object': issue})


def edit_issue(request, issue_id, template_name='issues/edit_issue.html'):
    issue = issue = get_object_or_404(Issue, pk=issue_id)
    form = EditIssueForm(request.POST or None, instance=issue)

    if form.is_valid():
        form.save()
        return redirect('issues:index')
    return render(request, template_name, {'form': form})


def add_issue(request):
    form = NewIssueForm(request.POST or None)
    if form.is_valid():
        issue = form.save(commit=False)
        issue.author = request.user
        issue.current_status = 'todo'
        issue.save()
        return redirect('issues:index')
