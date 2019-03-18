from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
import datetime

from .models import Trial

# Create your views here.

def sort_stages(trials):
	# Because the test groups were randomized when the experiment was run,
	# they need to be rearanged in order to ensure that each test group 
	# contains data from the the correct corresponding stage.

	test_group_names = [
		"[Control: 0Hz]",
		"[Test Group 1: 2Hz]",
		"[Test Group 2: 4Hz]",
		"[Test Group 3: 6Hz]",
		"[Test Group 4: 8Hz]",
		"[Test Group 5: 10Hz]",
	]

	trials_sorted = []

	for trial in trials:
		# Split the stage_order string into an array
		stage_order = trial.stage_order.split(", ")

		# The final element in 'stage_order' has an extra "," at the end
		# It is removed
		stage_order[-1] = stage_order[-1].split(",")[0]

		trial_data = {
			"name": trial.name,

			"control_time": trial.control_time,
			"control_errors": trial.control_errors,

			"time_created": trial.time_created,
			"comments": trial.comments,
		}
		
		# Add the 'time' and 'errors' data points for non-control test groups
		for t in range(1, 6):
			stage_location = str(stage_order.index(test_group_names[t]))
			trial_data["test_group_{0}_time".format(str(t))] = getattr(trial, "stage_{0}_time".format(stage_location))
			trial_data["test_group_{0}_errors".format(str(t))] = getattr(trial, "stage_{0}_errors".format(stage_location))

		trials_sorted.append(trial_data)

	return trials_sorted

def home(request):
	context = {
		
	}
	return render(request, 'index.html', context)

def data(request):
	# Only admins can access this page
	if not request.user.is_authenticated:
		return redirect('/admin/login/?next={0}'.format(request.path))
	if not request.user.is_staff:
		raise PermissionDenied

	trials = Trial.objects.all()

	# Use the GET variable 'order' to sort the results
	if request.GET.get("order", False) == "newest":
		trials = trials.order_by("-time_created")
	elif request.GET.get("order", False) == "oldest":
		trials = trials.order_by("time_created")
	else:
		# Add the show_discarded parameter if applicable
		redirection = "/export/?order=oldest"
		if request.GET.get("show_discarded", False) == "true":
			redirection += "&show_discarded=true"

		# This allows the order to be displayed in the URL at all times
		# Mainly to reduce confusion regarding how data without any parameters are ordered
		# Also only permits the allowed parameters to be set
		return redirect(redirection)

	# Hide discarded trials
	if request.GET.get("show_discarded", False) == "true":
		show_discarded = True
	else:
		trials = trials.filter(discard=False)
		show_discarded = False

	context = {
		"order": request.GET.get("order", False),
		"show_discarded": show_discarded,
		"time_generated": str(datetime.datetime.now()),
		"trials": trials,
	}
	return render(request, 'data-export/data.xml', context, content_type="text/xml")



def data_compiled(request, data="all"):
	# Only admins can access this page
	if not request.user.is_authenticated:
		return redirect('/admin/login/?next={0}'.format(request.path))
	if not request.user.is_staff:
		raise PermissionDenied

	trials = Trial.objects.filter(discard=False)

	context = {
		"trials": sort_stages(trials),
		"time_generated": str(datetime.datetime.now()),
	}
	
	if data == "all":
		return render(request, 'data-export/data-compiled.xml', context, content_type="text/xml")
	elif data == "time":
		return render(request, 'data-export/data-time.csv', context, content_type="text/csv")
	elif data == "errors":
		return render(request, 'data-export/data-errors.csv', context, content_type="text/csv")
	else:
		raise Http404

def data_time(request):
	return data_compiled(request, "time")
def data_errors(request):
	return data_compiled(request, "errors")

def data_list(request):
	# Only admins can access this page
	if not request.user.is_authenticated:
		return redirect('/admin/login/?next={0}'.format(request.path))
	if not request.user.is_staff:
		raise PermissionDenied

	trials = Trial.objects.all().order_by("-time_created")

	context = {
		"trials": trials,
	}
	return render(request, 'data-list.html', context)

def data_edit(request, id):
	# Only admins can access this page
	if not request.user.is_authenticated:
		return redirect('/admin/login/?next={0}'.format(request.path))
	if not request.user.is_staff:
		raise PermissionDenied

	trial = Trial.objects.get(id=id)

	context = {
		"trial": trial,
		"stage_numbers": [0, 1, 2, 3, 4, 5],
	}
	return render(request, 'data-edit.html', context)