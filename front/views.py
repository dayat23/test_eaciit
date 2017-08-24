from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.conf import settings

import os
import csv


class HomeView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)

		file_csv = os.path.join(settings.BASE_DIR, 'static', 'companies.csv')
		read_file = open(file_csv, encoding="ISO-8859-1")
		reader = list(csv.DictReader(read_file))

		context.update({
			'reader': reader
		})

		return context


class CompanyDetailView(TemplateView):
	template_name = 'show.html'

	def get_context_data(self, **kwargs):
		context = super(CompanyDetailView, self).get_context_data(**kwargs)

		return context


