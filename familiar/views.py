from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

import datetime

def main(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    data = {'html': html}
    return render_to_response('main.html',
                          data,
                          context_instance=RequestContext(request))

    
