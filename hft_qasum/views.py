from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from hft_qasum.upload import file_upload
from hft_qasum.hft_script import init, summ, ques
from hft_qasum.ocr_script import ocr_init, ocr_reader
from hft_qasum.forms import Summarize, Answer, Init, OCR

summarize = NULL
summary = NULL
question = NULL
main_text = NULL
image = NULL
image_url = NULL
image_name = NULL
easyocr = NULL
ocr_text = NULL
initiated = False

# Create your views here.
def index(request):
    global summarize, question, summary, main_text, easyocr, ocr_text, image, image_url, image_name, initiated
    if request.method == "POST":
        if request.POST['ins'] == 'init' and not initiated:
            pipelines = init()
            summarize = pipelines['summ']
            question = pipelines['qa']
            easyocr = ocr_init()
            initiated = True
            return HttpResponse('Initialized')
        elif request.POST['ins'] == 'init':
            return HttpResponse('Initialized')
        elif request.POST['ins'] == 'summarize':
            main_text = request.POST['text']
            summary = summ(summarize, main_text)
            return HttpResponse(summary[0]['summary_text'])
        elif request.POST['ins'] == 'answer':
            answer = ques(question, main_text, request.POST['text'])
            return HttpResponse(answer['answer'])
        elif request.POST['ins'] == 'ocr':
            image = request.FILES['image']
            image_url = file_upload(image)
            image_name = image._name
            print(image_url)
            ocr_text = ocr_reader(image_url, easyocr)
            return HttpResponse(ocr_text)
    else:
        m_form = Summarize()
        q_form = Answer()
        o_form = OCR()
        i_form = Init()
        return render(request, 'index.html', {'m_form': m_form, 'q_form': q_form, 'i_form': i_form, 'o_form': o_form})