from django import forms  

class Summarize(forms.Form): 
    ins = forms.CharField()
    ins.widget.attrs.update({'name': 'ins', 'value': 'summarize', 'hidden': 'true'})
    text = forms.CharField(widget=forms.Textarea)
    text.widget.attrs.update({'id': 'article', 'name': 'article', 'rows':'21', 'cols':'80'})

class Answer(forms.Form):
    ins = forms.CharField()
    ins.widget.attrs.update({'name': 'ins', 'value': 'answer', 'hidden': 'true'})
    text = forms.CharField(widget=forms.Textarea)
    text.widget.attrs.update({'id': 'ques', 'name': 'ques', 'rows': '5', 'cols': '80'})

class OCR(forms.Form):
    ins = forms.CharField()
    ins.widget.attrs.update({'name': 'ins', 'value': 'ocr', 'hidden': 'true'})
    image = forms.FileField()
    image.widget.attrs.update({'id': 'image', 'hidden': 'true'})

class Init(forms.Form):
    ins = forms.CharField()
    ins.widget.attrs.update({'name': 'ins', 'value': 'init', 'hidden': 'true'})