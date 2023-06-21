from django.shortcuts import get_object_or_404, render, redirect

from .forms import ReportForm
from .forms import Report
from django.http import HttpResponseNotFound


from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import datetime

import xlwt


def index(request):
    template = 'report/index.html'
    # context = {'category_posts': reports}
    reports = Report.objects.all().order_by('id')
    context = {'reports': reports}
    return render(request, template, context)
    # return render(request, template, context)

# def report_detail(request, id):
#     template = 'report/edit.html'

#     # context = {'post': posts[id]}
#     return render(request, template)

def report_edit(request, pk):
    template = 'report/edit.html'
    instance = get_object_or_404(Report, pk=pk)
    form = ReportForm(request.POST or None, instance=instance)
    context = {'form': form}
    if form.is_valid():
        form.save()
    # context = {'post': posts[id]}
    return render(request, template, context)

def report_delete(request, pk):
    template = 'report/delete.html'
    instance = get_object_or_404(Report, pk=pk)
    form = ReportForm(instance=instance)
    context = {'form': form}
    if request.method == 'POST':
        instance.delete()
        return redirect('report:index')
    return render(request, template, context)

def report_add(request):
    template = 'report/report_add.html'
    form = ReportForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, template, context)


def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="report.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = [
        'Номер запроса',
        'Дата поступления запроса',
        'Краткое описание запроса или задачи',
        'Тип работы',
        'Номер редактируемой или новой ДЕ/результат работы',
        'Исполнитель',
        'Трудозатраты (часы)',
        'не заполняется',
        'Дата выполнения'
    ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Report.objects.all().values_list(
        'number_report',
        'date_add_report',
        'about_report',
        'type',
        'MD',
        'author_report',
        'report',
        'no_field',
        'date_end_report',
        )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response