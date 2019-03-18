from django import forms

from .models import Trial

class TrialForm(forms.ModelForm):
	class Meta:
		model = Trial
		fields = [
			"name",
			"stage_order",

			"control",
			"stage_1",
			"stage_2",
			"stage_3",
			"stage_4",
			"stage_5",

			"control_time",
			"stage_1_time",
			"stage_2_time",
			"stage_3_time",
			"stage_4_time",
			"stage_5_time",

			"control_errors",
			"stage_1_errors",
			"stage_2_errors",
			"stage_3_errors",
			"stage_4_errors",
			"stage_5_errors",

			"discard",
			"comments",
		]

		widgets = {
			"control": forms.Textarea(),
			"stage_order": forms.Textarea(),
			"stage_1": forms.Textarea(),
			"stage_2": forms.Textarea(),
			"stage_3": forms.Textarea(),
			"stage_4": forms.Textarea(),
			"stage_5": forms.Textarea(),
			"comments": forms.Textarea(),
		}