import requests
from django.http import HttpResponse


def index(request):
	with open ("sistema.html", "r") as f:
		s = f.read()

	return HttpResponse(s)

def upd(request):
	lampOn = 'https://www.w3schools.com/js/pic_bulbon.gif'
	lampOff = 'https://www.w3schools.com/js/pic_bulboff.gif'
	garagemOn = 'https://visualpharm.com/assets/4/Garage%20Open-595b40b65ba036ed117d2d57.svg'
	garagemOff = 'https://visualpharm.com/assets/971/Garage%20Closed-595b40b65ba036ed117d2d56.svg'
	alarmeOn = 'https://image.flaticon.com/icons/png/128/148/148921.png'
	alarmeOff = 'https://image.flaticon.com/icons/png/128/149/149845.png'
	idTag = str (request).split ('/')[1]

	src = ["", ""]
	if (idTag[0:4] == "lamp"):
		src[0] = lampOff
		src[1] = lampOn
	elif (idTag == "garagem"):
		src[0] = garagemOff
		src[1] = garagemOn
	elif (idTag == "alarme"):
		src[0] = alarmeOn
		src[1] = alarmeOff
	
	with open ("sistema.html", "r") as f:
		fi = str (f.read())
		patOff = idTag + '" src="' + src[0]
		patOn = idTag + '" src="' + src[1]
		print (patOff + " VS " + patOn)
		
		if (patOff in fi):
			fi = fi.split (patOff)
			pattern = patOn
		else:
			fi = fi.split (patOn)
			pattern = patOff
		
	print ("NEW: " + str (pattern))
	with open ("sistema.html", "w") as f:
		f.write (fi[0] + pattern + fi[1])

	return index (request)

def info(request):
	with open ("info.txt", "r") as f:
		s = f.read()
		
	return HttpResponse(s)
