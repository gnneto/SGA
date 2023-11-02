from django import forms
from .models import SenhasContas

from django import forms
from .models import SenhasContas

class EditarContaForm(forms.Form):
    conta = forms.ModelChoiceField(
        queryset=SenhasContas.objects.none(),
        label='Selecione a conta',
        widget=forms.Select
    )
    nova_senha = forms.CharField(widget=forms.PasswordInput, label='Nova senha')

    def __init__(self, user, *args, **kwargs):
        super(EditarContaForm, self).__init__(*args, **kwargs)
        self.fields['conta'].queryset = SenhasContas.objects.filter(usuario__user=user)


