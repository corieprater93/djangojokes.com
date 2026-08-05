from datetime import datetime
from django import forms

class JobsApplicationForm(forms.Form):
    EMPLOYMENT_TYPES = (
        (None, '--Please choose--'),
        ('ft', 'Full-time'),
        ('pt', 'Part-time'),
        ('contract', 'Contract work'),
    )

    DAYS = (
        (1, 'MON'),
        (2, 'TUE'),
        (3, 'WED'),
        (4, 'THU'),
        (5, 'FRI'), 
    )

    first_name = forms.CharField(
        widget=forms.URLInput(
            attrs={
                    'autofocus': True,
                    'class': 'form.control',
                }
        )
    )
    last_name = forms.CharField(
        widget=forms.URLInput(
            attrs={
                'class': 'form.control',
            }
        )
    )
    email = forms.EmailField(
        widget=forms.URLInput(
                    attrs={
                        'class': 'form.control',
                    }
                )
    )
    website = forms.URLField(
        required=False,
                widget=forms.URLInput(
                    attrs={
                    'size': '50',
                    'class': 'form-control',
                    'placeholder': 'https://www.example.com',
                    }
                )
    )
        
    employment_type = forms.ChoiceField(choices=EMPLOYMENT_TYPES)

    # Start date section
    YEARS = range(datetime.now().year, datetime.now().year+2)

    start_date = forms.DateField(
        help_text="The earliest you can start working.",
        widget=forms.SelectDateWidget(
            years=YEARS, 
        )
    )
    avaliable_days = forms.TypedMultipleChoiceField(
        choices=DAYS,
        coerce=int,
        help_text="Check all days that you can work.",
        widget=forms.CheckboxSelectMultiple(
            attrs={'checked':True}
        )
    )
    desired_hourly_wage = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={'min':'10.00', 'max':'100.00', 'step':'.25'}
        )
    )
    cover_letter = forms.CharField(
        widget=forms.Textarea(attrs={'cols':'75', 'rows': '5'})
    )
    confirmation = forms.BooleanField(
        label='I certify that the information I have provided is true.'
    )