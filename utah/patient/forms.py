from django import forms

from .models import Patient


class CustomModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_input_types()

    def init_input_types(self):
        for field in self:
            if isinstance(field.field, forms.fields.DateTimeField):
                field.input_type = 'date'
            else:
                field.input_type = field.field.widget.input_type


class PreopPatientFileForm(CustomModelForm):
    class Meta:
        model = Patient
        fields = ["firstname", "lastname", "height", "weight", "ddn", "ddi", "intervention",
                  "chirurgien", "chirurgie", "pathologie", "traitement1", "traitement2"]


class PostopPatientFileForm(CustomModelForm):
    class Meta:
        model = Patient
        fields = ["schema_therap", "date_derniere_prise_th1", "date_derniere_prise1", "inobservance1", "date_derniere_prise_th2", "date_derniere_prise2", "inobservance2",
                  "aptt", "pt", "inr", "hemoglobine", "plaquette", "dfg", "vol_sang", "coag"]

    def save(self, commit=True):
        patient = self.instance

        if commit:
            patient.save()
        return patient


class UpdatePatientFileForm(CustomModelForm):
    class Meta:
        model = Patient
        fields = ["firstname", "lastname", "height", "weight", "ddn", "ddi", "intervention",
                  "consultant",
                  "chirurgien", "chirurgie", "pathologie", "traitement1", "traitement2",
                  "algo", "algo_result",
                  "schema_therap", "date_derniere_prise_th1", "date_derniere_prise1", "inobservance1", "date_derniere_prise_th2", "date_derniere_prise2", "inobservance2",
                  "aptt", "pt", "inr", "hemoglobine", "plaquette", "dfg", "vol_sang", "coag"]

    def save(self, commit=True):
        patient = self.instance

        if commit:
            patient.save()
        return patient
