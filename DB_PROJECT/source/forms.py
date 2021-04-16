from django import forms
  
'''
上传表单
'''
class UploadForm(forms.Form):
    course_id = forms.CharField(label="课程编号", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    remark = forms.CharField(label="备注", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    file_info = forms.FileField(label = "文件", widget=forms.FileInput(attrs={'class': 'form-file'}))
