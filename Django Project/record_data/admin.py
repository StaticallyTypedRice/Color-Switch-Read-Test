from django.contrib import admin

from .models import Trial
from .forms import TrialForm

# Register your models here.

class TrialAdmin(admin.ModelAdmin):
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

	form = TrialForm

admin.site.register(Trial, TrialAdmin)