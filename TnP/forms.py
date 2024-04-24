from django.forms import ModelForm
from TnP import models

class registerStockRecievedForm(ModelForm):
    class Meta:
        model = models.registerStockRecieved
        fields = ['stockRecieved','stockRecievedChoices']

class registerStockOnLoan(ModelForm):
    class Meta:
        model = models.registerStockOnLoan
        fields = ['stockDispatched']

class registerStockDispatchSicklineform(ModelForm):
    class Meta:
        model = models.registerStockDispatchedSickline
        fields = ['stockDispatched']

class registerStockDispatchedYardform(ModelForm):
    class Meta:
        model =  models.registerStockDispatchedYard
        fields = ['stockDispatched', 'Yard']

class registerStockDispatchedTrainDutyform(ModelForm):
    class Meta:
        model = models.registerStockDispatchedTrainDuty
        fields = ['stockDispatched']