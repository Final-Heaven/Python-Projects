from django.contrib import admin
# Need to import UniversityCampus from models file
from .models import UniversityCampus

# This registers the model
admin.site.register(UniversityCampus)
