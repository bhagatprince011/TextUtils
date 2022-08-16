from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyzeText(request):
    text=request.POST.get('mytext','default')
    removePunc= request.POST.get('removePunc','off')
    Capitalize= request.POST.get('Capitalize','off')
    newLineRemover= request.POST.get('newLineRemover','off')
    if (removePunc=='on'):
        if(Capitalize=='on'):
            capitalizeText=''
            for char in text:
                capitalizeText+=char.upper()
                text=capitalizeText

        punctuation='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzedText=''
        for char in text:
            if char not in punctuation: 
                analyzedText+=char
        params= {'purpose':'Removing all the Punctuations',
                'analyzed_text':analyzedText}
        return render(request,'analyze.html',params)
    elif(Capitalize=='on'):
        capitalizeText=''
        for char in text:
            capitalizeText+=char.upper()
        params= {'purpose':'Capitalized Sentence',
                'analyzed_text':capitalizeText}
        return render(request,'analyze.html',params)
    elif(newLineRemover=='on'):
        newLine=''
        for char in text:
            if(char!='\n'):
                newLine+=char
        params= {'purpose':'Made all in one line',
                'analyzed_text':newLine}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse('<h2>ERROR 404, Not Capitalized</h2>')

 
 