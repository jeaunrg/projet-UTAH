from django import forms

from inclusion.models import Patient


class CreatePatientFileForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = ["height", "weight", "ddn", "ddi", "intervention", "chirurgie", "pathologie", "traitement1", "traitement2"]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.initInputTypes()

	def initInputTypes(self):
		for field in self:
			if isinstance(field.field, forms.fields.DateTimeField):
				field.input_type = 'date'
			else:
				field.input_type = field.field.widget.input_type

class UpdatePatientFileForm(forms.ModelForm):

	class Meta:
		model = Patient
		fields = ["height", "weight", "ddn", "ddi", "intervention", "chirurgie", "pathologie", "traitement1", "traitement2"]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.initInputTypes()

	def initInputTypes(self):
		for field in self:
			if isinstance(field.field, forms.fields.DateTimeField):
				field.input_type = 'date'
			else:
				field.input_type = field.field.widget.input_type

	def save(self, commit=True):
		patient = self.instance

		if commit:
			patient.save()
		return patient
