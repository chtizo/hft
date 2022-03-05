from django import forms  

class Summarize(forms.Form): 
    ins = forms.CharField()
    ins.widget.attrs.update({'name': 'ins', 'value': 'summarize', 'hidden': 'true'})
    text = forms.CharField(widget=forms.Textarea)
    text.widget.attrs.update({'id': 'main_text', 'name':'main_text', 'rows':'15', 'cols':'60'})

class Answer(forms.Form):
    ins = forms.CharField()
    ins.widget.attrs.update({'name': 'ins', 'value': 'answer', 'hidden': 'true'})
    text = forms.CharField(widget=forms.Textarea)
    text.widget.attrs.update({'id': 'ques', 'name':'ques', 'rows':'5', 'cols':'50'})

class Init(forms.Form):
    ins = forms.CharField()
    ins.widget.attrs.update({'name': 'ins', 'value': 'init', 'hidden': 'true'})