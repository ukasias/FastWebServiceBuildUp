# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def main_view(request):
	value = {'title' : 'Hello', 'msg' : 'world' }
	return render_to_response('main.html', value)
	
def post_view(request):
	html = "value : %s"%(request.POST['param'])
	
	return HttpResponse(html)