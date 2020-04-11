from project.models import Groups, GroupProgress, Department
from django import forms


class AddGroupForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ['department_id',  'group_name', 'group_email']


class AddGroupProgressForm(forms.ModelForm):
    class Meta:
        model = GroupProgress
        fields = ['group_id', 'files_type', 'file_title', 'file_description']


class CreateDepartment(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['school_id',  'department_name']
