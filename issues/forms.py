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


class NewCommentForm(forms.Form):


== == == =


class CommentForm(forms.Form):


>>>>>> > b4a81a3cca4614f8358e2065f5720c0f43ee092c
comment = forms.CharField(required=True, widget=forms.Textarea)
