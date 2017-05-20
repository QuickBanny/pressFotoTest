from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Image

import operator
from django.db.models import Q
# Create your views here.

def home(request):
	images = Image.objects.all()
	context = {
		'images': images
	} 
	return render(request, 'catalog/home.html',  context)

def about(request):
	return render(request, 'catalog/about.html')

def show_image(request, image_id):
	image = get_object_or_404(Image, id=image_id)
	context = {
		'image': image
	}
	return render(request, 'catalog/image.html', context)

def search_form(request):
    return render(request, 'catalog/search_form.html')

def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		image = Image.objects
		image_name = image.filter(name__icontains=q)
		image_desc = image.filter(desc__icontains=q)

		if len(image_name) != 0:			
			context = {
				'images': image_name
			}
		elif len(image_desc) != 0:
			context = {
				'images': image_desc
			}
		else:
			print('Не удволетворяет поиску')
			images = Image.objects.all()
			context = {
				'images': images
			}
		return render(request, 'catalog/home.html', context)
	else:
		return HttpResponse('Please submit a search term.')

# def bad_search(request):
#     # The following line will raise KeyError if 'q' hasn't
#     # been submitted!
#     message = 'You searched for: %r' % request.GET['q']
#     return HttpResponse(message)
