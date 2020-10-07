from django import forms
from django.core import validators

#Writing our own validators
def check_for_z(value):
    #check for Z letter and 0 value
    if value[0].lower() != 'z':
        raise forms.ValidationError('NAME NEEDS TO Start WITH Z')

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)


    #Protrction from bots
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    #def clean_botcatcher (self):
     #   botcatcher = self.cleaned_data['botcatcher']
      #  if len(botcatcher)> 0:
       #     raise forms.ValidationError('Gotcha Bot!')
        #return botcatcher