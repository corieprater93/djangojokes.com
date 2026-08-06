from django.forms import ModelForm, Textarea

from .models import Joke

class JokeForm(ModelForm):
    class Meta:
        model = Joke
        fields = ['question', 'answer']
        widgets = {
            'question': Textarea(
                attrs={'cols': 80, 'rows': 3, 'autofocus': True}
            ),
            'answers': Textarea(
                attrs={'cols': 80, 'rows': 2, 'pleaseholder': 'Make it funny!'}
            )
        }
        help_texts = {
            'question': 'No dirty jokes please.'
        }