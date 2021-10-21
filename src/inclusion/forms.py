from django import forms

from inclusion.models import Patient


class CreatePatientFileForm(forms.ModelForm):

	class Meta:
		model = Patient
		fields = ["nipp", "first_name", "last_name", "age", "gender", "weight", "height"]


class UpdatePatientFileForm(forms.ModelForm):

	class Meta:
		model = Patient
		fields = ["nipp", "first_name", "last_name", "age", "gender", "weight", "height"]

	def save(self, commit=True):
		patient_file = self.instance
		patient_file.nipp = self.cleaned_data['nipp']
		patient_file.first_name = self.cleaned_data['first_name']
		patient_file.last_name = self.cleaned_data['last_name']

		if commit:
			patient_file.save()
		return patient_file
