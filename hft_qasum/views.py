from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from hft_qasum.hft_script import init, summ, ques
from hft_qasum.forms import Summarize, Answer, Init

summarize = NULL
summary = NULL
question = NULL

# Create your views here.
def index(request):
    if request.method == "POST":
        if request.POST['ins'] == 'summarize':
            summary = summ(summarize, request.POST['main_text'])
            return HttpResponse(summary[0]['summary_text'])
        elif request.POST['ins'] == 'answer':
            answer = ques(question, summary, request.POST['ques'])
            return HttpResponse(answer['answer'])
        elif request.POST['ins'] == 'init':
            summarize, question = init()
            return HttpResponse('Initialized')
    else:
        m_form = Summarize()
        q_form = Answer()
        i_form = Init()
        return render(request, 'index.html', {'m_form': m_form, 'q_form': q_form, 'i_form': i_form})