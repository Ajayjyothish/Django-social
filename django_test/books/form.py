from django import forms
from .models import Book , Post

class BookForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )
    class Meta:
        model = Book
        fields = ['title','description','price']

class BookRawForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'rows' : 5,
            'placeholder' : 'Whats on your mind?'
        }
       
    ),
     help_text = "Max 400 words",
    
    )

class PostForm(forms.ModelForm):
    subject = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder' : "What's on your mind?"
            }
        )
    )
    class Meta:
        model = Post
        fields=['subject']