from bootstrap_datepicker_plus.widgets import DateTimePickerInput

from django import forms

class ToDoForm(forms.Form):
    datetime = forms.DateField(widget=DateTimePickerInput())