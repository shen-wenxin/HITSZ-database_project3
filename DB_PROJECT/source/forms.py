from django import forms
from course.models import Course 
'''
上传表单
'''
class UploadForm(forms.Form):
    course_list = []
    remark = forms.CharField(label="备注", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    file_info = forms.FileField(label = "文件", widget=forms.FileInput(attrs={'class': 'form-file'}))
    course = forms.ChoiceField(label = "课程",widget = forms.Select())

