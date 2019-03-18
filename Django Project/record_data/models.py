from django.db import models

# Create your models here.

class Trial(models.Model):
	name = models.CharField(max_length=20, blank=False, null=False)
	comments = models.CharField(max_length=10000, blank=True, null=True)
	stage_order = models.CharField(max_length=240, blank=False, null=False)

	# The numbers generated for the experiment
	control = models.CharField(max_length=240, blank=False, null=False)
	stage_1 = models.CharField(max_length=240, blank=False, null=False)
	stage_2 = models.CharField(max_length=240, blank=False, null=False)
	stage_3 = models.CharField(max_length=240, blank=False, null=False)
	stage_4 = models.CharField(max_length=240, blank=False, null=False)
	stage_5 = models.CharField(max_length=240, blank=False, null=False)

	# How long it took to read each stage
	control_time = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	stage_1_time = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	stage_2_time = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	stage_3_time = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	stage_4_time = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	stage_5_time = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

	# How many errors were made in reading?
	control_errors = models.IntegerField(blank=True, null=True)
	stage_1_errors = models.IntegerField(blank=True, null=True)
	stage_2_errors = models.IntegerField(blank=True, null=True)
	stage_3_errors = models.IntegerField(blank=True, null=True)
	stage_4_errors = models.IntegerField(blank=True, null=True)
	stage_5_errors = models.IntegerField(blank=True, null=True)

	# If True, something went wrong in the experiment and it should not be included in data analysis
	discard = models.BooleanField(default=False)

	time_created = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return self.name