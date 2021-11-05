from django import forms

from patient.models import Patient

class CustomModelForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.initInputTypes()

	def initInputTypes(self):
		for field in self:
			if isinstance(field.field, forms.fields.DateTimeField):
				field.input_type = 'date'
			else:
				field.input_type = field.field.widget.input_type

class PreopPatientFileForm(CustomModelForm):
	class Meta:
		model = Patient
		fields = ["height", "weight", "ddn", "ddi", "intervention", "chirurgie", "pathologie", "traitement1", "traitement2"]


class PostopPatientFileForm(CustomModelForm):
	class Meta:
		model = Patient
		fields = ["schema_therap", "date_derniere_prise1", "inobservance1", "date_derniere_prise2", "inobservance2", "aptt", "pt", "inr", "hemoglobine", "plaquette", "dfg", "vol_sang", "coag"]

	def save(self, commit=True):
		patient = self.instance

		if commit:
			patient.save()
		return patient

class UpdatePatientFileForm(CustomModelForm):

	class Meta:
		model = Patient
		fields = ["height", "weight", "ddn", "ddi", "intervention", "chirurgie", "pathologie", "traitement1", "traitement2",
				  "schema_therap", "date_derniere_prise1", "inobservance1", "date_derniere_prise2", "inobservance2", "aptt", "pt", "inr", "hemoglobine", "plaquette", "dfg", "vol_sang", "coag"]

	def save(self, commit=True):
		patient = self.instance

		if commit:
			patient.save()
		return patient
