from django import forms
  



class CourseForm(forms.Form):
    course_id = forms.CharField(label="课程编号(确定后无法更改，请慎重)", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label="课程名字", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    teacher = forms.CharField(label="任课老师", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    student = forms.CharField(label="学生", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))

class CourseModifyForm(forms.Form):
    name = forms.CharField(label="课程名字(若不想修改请输入“不修改”)", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    teacher = forms.CharField(label="新增任课老师", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    student = forms.CharField(label="新增学生", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))