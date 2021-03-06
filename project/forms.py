
from django import forms
from .models import *

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        exclude = ['user'] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['project_num'].widget.attrs.update({'class' : 'form-control'})
        self.fields['source'].widget.attrs.update({'class' : 'form-control'})
        self.fields['person'].widget.attrs.update({'class' : 'form-control'})
        self.fields['bund'].widget.attrs.update({'class' : 'form-control'})
        self.fields['start_time'].widget.attrs.update({'class' : 'form-control'})
        self.fields['end_time'].widget.attrs.update({'class' : 'form-control'})
        self.fields['project_member'].widget.attrs.update({'class' : 'form-control'})


class ProjectCheckForm(forms.ModelForm):

    class Meta:
        model = ProjectCheck
        exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(ProjectCheckForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['project_num'].widget.attrs.update({'class' : 'form-control'})
        self.fields['source'].widget.attrs.update({'class' : 'form-control'})
        self.fields['person'].widget.attrs.update({'class' : 'form-control'})
        self.fields['bund'].widget.attrs.update({'class' : 'form-control'})
        self.fields['check_org'].widget.attrs.update({'class' : 'form-control'})
        self.fields['start_time'].widget.attrs.update({'class' : 'form-control'})
        self.fields['end_time'].widget.attrs.update({'class' : 'form-control'})
        self.fields['check_time'].widget.attrs.update({'class' : 'form-control'})
        self.fields['check_text'].widget.attrs.update({'class' : 'form-control'})




class ProjectIdentifyForm(forms.ModelForm):
	
    class Meta:
        model = ProjectIdentify
        exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(ProjectIdentifyForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['project_num'].widget.attrs.update({'class' : 'form-control'})
        self.fields['source'].widget.attrs.update({'class' : 'form-control'})
        self.fields['person'].widget.attrs.update({'class' : 'form-control'})
        self.fields['bund'].widget.attrs.update({'class' : 'form-control'})
        self.fields['start_time'].widget.attrs.update({'class' : 'form-control'})
        self.fields['end_time'].widget.attrs.update({'class' : 'form-control'})
        self.fields['identify_time'].widget.attrs.update({'class' : 'form-control'})
        self.fields['identify_org'].widget.attrs.update({'class' : 'form-control'})
        self.fields['identify_text'].widget.attrs.update({'class' : 'form-control'})


# class MemberForm(forms.ModelForm):
#
#     class Meta:
#         model = Member
#         exclude = ['age','user'] # uncomment this line and specify any field to exclude it from the form
#
#     def __init__(self, *args, **kwargs):
#         super(MemberForm, self).__init__(*args, **kwargs)
#         self.fields['name'].widget.attrs.update({'class' : 'form-control'})
