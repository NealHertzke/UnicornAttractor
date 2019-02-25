from django import forms
from .models import Issue


class NewIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('title', 'description', 'type')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class EditIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('title', 'description', 'type', 'current_status')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class CommentForm(forms.Form):
    comment = forms.CharField(required=True, widget=forms.Textarea)
