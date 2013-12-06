from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf.urls import url
from utilities import logged_in

import datetime


def main(request):
    '''
    Handles the home page for the app. It displays the latest comments.
    '''
    
    username = 'chris'

    data = {
        'logged_in': logged_in(username),
        'btn_txt': 'click to submit yer info', 
    }
    return render_to_response('main.html',
                          data,
                          context_instance=RequestContext(request))


def Christmas_list(request):
    '''
    Handles and displays people's Christmas Wish Lists.
    '''
    return HttpResponse('Meery@@!!!')


    
