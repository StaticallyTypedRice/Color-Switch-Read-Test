from django.http import JsonResponse
from django.http import Http404

from .models import Trial
from .forms import TrialForm

# Create your API here.

def add_trial(request):
	form = TrialForm(request.POST)
	
	if form.is_valid():
		context = {
			"submitted": True,
		}
		form.save()
	else:
		context = {
			"submitted": False,
			"error": {
				"message": "Form Error: See Console.",
				"data": form.errors,
			}
		}

	return JsonResponse(context)

def edit_data(request):
	try:
		trial = Trial.objects.get(id=request.POST.get("id", False))
	except Trial.DoesNotExist:
		raise Http404

	stages = [
		"control",
		"stage_1",
		"stage_2",
		"stage_3",
		"stage_4",
		"stage_5",
	]

	time = []
	errors = []

	for s in stages:
		if request.POST.get("{0}_time".format(s), False):
			try:
				stage_time = float(request.POST.get("{0}_time".format(s), False))
			except ValueError:
				stage_time = None
		else:
			stage_time = None

		if request.POST.get("{0}_errors".format(s), False):
			try:
				stage_errors = int(request.POST.get("{0}_errors".format(s), False))
			except ValueError:
				stage_errors = None
		else:
			stage_errors = None

		time.append(stage_time)
		errors.append(stage_errors)


	trial.control_time = time[0]
	trial.stage_1_time = time[1]
	trial.stage_2_time = time[2]
	trial.stage_3_time = time[3]
	trial.stage_4_time = time[4]
	trial.stage_5_time = time[5]

	trial.control_errors = errors[0]
	trial.stage_1_errors = errors[1]
	trial.stage_2_errors = errors[2]
	trial.stage_3_errors = errors[3]
	trial.stage_4_errors = errors[4]
	trial.stage_5_errors = errors[5]

	trial.save()

	context = {
		"submitted": True,
	}

	return JsonResponse(context)