from django import forms
from django.forms import inlineformset_factory

from prospects.models import Prospects, Documents


ProspectsDocumentsFormset = inlineformset_factory(Prospects, Documents, fields=('name', 'file'), extra=1,
                                                  can_delete=False)


class DocumentsForm(forms.ModelForm):

    class Meta:
        model = Documents
        exclude = ['prospect']


class ProspectsForm(forms.ModelForm):
    documents = DocumentsForm()

    class Meta:
        model = Prospects
        exclude = ['status']


class ProspectsEvaluationForm(forms.ModelForm):

    class Meta:
        model = Prospects
        fields = ['reject_details']
