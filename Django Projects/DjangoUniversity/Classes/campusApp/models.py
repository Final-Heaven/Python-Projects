from django.db import models


# Creating the class here
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)  # Max length of 2 for state
    campus_id = models.IntegerField(default="", blank=True, null=False)

    # This creates the model manager
    object = models.Manager()

    # This code says what to display in the browser instead of
    # the default name (for clarity)
    def __str__(self):
        display_campus = '{0.campus_name} ({0.state})'
        return display_campus.format(self)

    # This dictates exactly what the class will display as in the browser
    class Meta:
        verbose_name_plural = "University Campus"
