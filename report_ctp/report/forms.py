from django import forms


from .models import Report

class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = '__all__' 
        # fields = ('number_report', 'date_add_report', 'about_report')
        widgets = {
            'number_report': forms.Textarea({'cols': '22', 'rows': '2'}),
            'date_add_report': forms.DateInput(attrs={'type': 'date'}),
            'about_report': forms.Textarea({'cols': '22', 'rows': '5'}),
            'MD': forms.Textarea({'cols': '22', 'rows': '5'}),
            'date_end_report': forms.DateInput(attrs={'type': 'date'}),
        }
