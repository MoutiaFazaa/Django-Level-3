from django import forms
from django.core import validators

#Writing our own validators
#def check_for_z(value):
    #check for Z letter and 0 value
   # if value[0].lower() != 'z':
       # raise forms.ValidationError('NAME NEEDS TO Start WITH Z')

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)


    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('MAKE SURE EMAILS MATCH!')

    #Protrction from bots
    #botcatcher = forms.CharField(required=False,
     #                           widget=forms.HiddenInput,
      #                          validators=[validators.MaxLengthValidator(0)])

    #def clean_botcatcher (self):
     #   botcatcher = self.cleaned_data['botcatcher']
      #  if len(botcatcher)> 0:
       #     raise forms.ValidationError('Gotcha Bot!')
        #return botcatcher