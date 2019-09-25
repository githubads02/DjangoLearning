from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("<h1>Hello</h1>")
    return render(request,'Home.html')
def count(request):

    #dictionary
    worddict = {}

    #capture the http parameter value
    txt = request.GET['txt']

    #split the captured text into a list
    wrdlist = txt.split()

    #iterate through the list to find words and form a dictionary with word a key and the count as value
    for word in wrdlist:
        if word in worddict:
            #increase word count
            worddict[word] += 1
        else:
            #add word to dictionary and increase count
            worddict[word] = 1

    #put desired result to html page
    return render(request,'Count.html',{'txt':txt,'count':len(wrdlist),'worddict':worddict.items()})