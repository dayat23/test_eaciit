from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.conf import settings
from braces.views import AjaxResponseMixin
from django.http import JsonResponse

import os
import csv


class HomeView(AjaxResponseMixin, TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)

		# file_csv = os.path.join(settings.BASE_DIR, 'static', 'companies.csv')
		# read_file = open(file_csv, encoding="ISO-8859-1")
		# reader = list(csv.DictReader(read_file))

		# context.update({
		# 	'reader': reader
		# })

		return context

	def get_ajax(self, request, *args, **kwargs):
		file_csv = os.path.join(settings.BASE_DIR, 'static', 'companies.csv')
		read_file = open(file_csv, encoding="ISO-8859-1")
		reader = list(csv.DictReader(read_file))

		resp = {
			'data': reader
		}

		return JsonResponse(resp)


class CompanyDetailView(TemplateView):
	template_name = 'show.html'

	def get_context_data(self, **kwargs):
		context = super(CompanyDetailView, self).get_context_data(**kwargs)

		file_csv = os.path.join(settings.BASE_DIR, 'static', 'companies.csv')
		read_file = open(file_csv, encoding="ISO-8859-1")
		reader = list(csv.DictReader(read_file))

		slug = self.kwargs.get('slug')

		data_regulator_capital = []
		data_npat_alloc_eq = []
		data_total_limit_eop = []
		data_revenue = []

		total_data = 0
 
		if 'and' in slug:
			slug = slug.replace('and', '&').replace('-', ' ')
		else:
			slug = slug.replace('-', ' ')

		for i in reader:
			if i['CMGUnmaskedName'].lower() == slug:
				data_regulator_capital.append({
					'tahun': '2014',
					'value': i[' RegulatoryCapital_AVG_FY14'].replace(',', '').strip()
				})
				data_regulator_capital.append({
					'tahun': '2015',
					'value': i[' RegulatoryCapital_AVG_FY15'].replace(',', '').strip()
				})

				data_npat_alloc_eq.append({
					'tahun': '2014',
					'value': i[' NPAT_AllocEq_FY14'].replace(',', '').strip()
				})
				data_npat_alloc_eq.append({
					'tahun': '2015',
					'value': i[' NPAT_AllocEq_FY15X'].replace(',', '').strip()
				})

				data_total_limit_eop.append({
					'tahun': '2014',
					'value': i[' TotalLimits_EOP_FY14'].replace(',', '').strip()
				})
				data_total_limit_eop.append({
					'tahun': '2015',
					'value': i[' TotalLimits_EOP_FY15x'].replace(',', '').strip()
				})

				data_revenue.append({
					'tahun': '2014',
					'value': i['REVENUE FY14'].replace(',', '').strip()
				})
				data_revenue.append({
					'tahun': '2015',
					'value': i['REVENYE FY15X'].replace(',', '').strip()
				})

		context.update({
			'data_regulator_capital': data_regulator_capital,
			'data_npat_alloc_eq': data_npat_alloc_eq,
			'data_total_limit_eop': data_total_limit_eop,
			'data_revenue': data_revenue
		})

		return context


