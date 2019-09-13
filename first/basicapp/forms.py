from django import forms
from basicapp.models import Open_Acc_App
from django.forms import DateField,CharField

class application(forms.ModelForm):
    # date= DateField(input_formats=['%d/%m/%y'])
    date_of_incorporation=DateField(
        widget=forms.DateInput(attrs={'class':'test','placeholder':'YYYY-MM-DD'}),input_formats=['%Y-%m-%d'])

    registered_address=CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 2}))
    mailing_address= CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 2}))
    nature_of_business =CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 2}),help_text="(e.g. manufacturing of electronic goods)")
    class Meta():
        model = Open_Acc_App
        fields='__all__'
