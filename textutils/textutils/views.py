from django.http import HttpResponse
from django.shortcuts import render

def caps(txt):
    return txt.capitalize()

def spa(txt):
    st = ""
    for i in range(len(txt)):
        if not(txt[i]==" " and txt[i+1]==" "):
            st = st + txt[i]
    return st

def repunc(txt):
    sr = ""
    p = ['.', '?',' "','\' ',' ,',' -', '!', ':', ';']
    for i in txt:
        if i not in p:
            sr = sr+i
    return sr

def cnt(txt):
    l = txt.split(" ")
    return len(l)


def index(request):
    return render(request, 'index.html')

def analyze(request):
    txt = request.GET.get('text', 'off')
    rmv_space = request.GET.get('rmv_space', 'off')
    capitalize = request.GET.get('capitalize', 'off')
    rmv_punct = request.GET.get('rmv_punct', 'off')
    count = request.GET.get('count', 'off')

    if rmv_space == 'on':
        f = spa(txt)
        if capitalize == 'on':
            g = caps(f)
            if rmv_punct == 'on':
                h = repunc(g)
                params= {'op':'removing spaces and capitalising...', 'file':h}
            else:
                params= {'op':'removing spaces and capitalising and removing punctuations...', 'file':g}
        elif rmv_punct == 'on':
            g = repunc(f)
            params= {'op':'removing spaces and punctuations...', 'file':g}

        elif count == 'on':
            g = cnt(f)
            params= {'op':'removing spaces and counting words...', 'file':g}

        else:
            params= {'op':'removing spaces...', 'file':f}
        return render(request, 'otpt.html', params)

    elif capitalize == 'on':
        f = caps(txt)
        if rmv_punct == 'on':
            g = repunc(f)
            params= {'op':'removing punctuations and capitalizing...', 'file':g}
        else:
            params= {'op':'capitalizing...', 'file':f}
        return render(request, 'otpt.html', params)

    elif rmv_punct == 'on':
        f = repunc(txt)
        params= {'op':'removing punctuations...','file':f}
        return render(request, 'otpt.html', params)

    elif count == 'on':
        f = cnt(txt)
        params= {'op':'counting....', 'file':f}
        return render(request, 'otpt.html', params)






