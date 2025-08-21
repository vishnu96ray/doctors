from django.shortcuts import render





def audiocall(request):
	pass


def image(request):
	return render(request, 'gallery/gallery_image.html')


def video(request):
	return render(request, 'gallery/gallery_video.html')

