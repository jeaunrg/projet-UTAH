from django import forms

from inclusion.models import PatientFile


class CreatePatientFileForm(forms.ModelForm):

	class Meta:
		model = PatientFile
		fields = ['title', 'body', 'image']


class UpdatePatientFileForm(forms.ModelForm):

	class Meta:
		model = PatientFile
		fields = ['title', 'body', 'image']

	def save(self, commit=True):
		patient_file = self.instance
		patient_file.title = self.cleaned_data['title']
		patient_file.body = self.cleaned_data['body']

		if self.cleaned_data['image']:
			patient_file.image = self.cleaned_data['image']

		if commit:
			patient_file.save()
		return patient_file
