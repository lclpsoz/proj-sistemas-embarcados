import requests
from django.http import HttpResponse

def index(request):
	with open ("sistema.html", "r") as f:
		s = f.read()

	return HttpResponse(s)

def fInv (s, pos):
	if (s[pos] == 1):
		s[pos] = 0
	else:
		s[pos] = 1
		
	return s

def upd(request):
	s = str (request).split ('/')[1]
	
	with open ("info.txt", "r") as f:
		l = list (f.read())
		info = [int (x) for x in l]
	
	if (s == 'sala'):
		info = fInv (info, 0)
	elif (s == 'cozinha'):
		info = fInv (info, 1)
	elif (s == 'quarto'):
		info = fInv (info, 2)
	else:
		info = fInv (info, 3)
		
	with open ("info.txt", "w") as f:
		out = ""
		for i in info:
			out += str (i)
		f.write (out)
	
	pattern = "/*" + s + "*/"
	with open ("sistema.html", "r") as f:
		fi = f.read()
		fi = fi.split (pattern)
		if (fi[1][0] == 'b'): # black
			fi[1] = fi[1][5:]
			inv = "yellow"
		else: # yellow
			fi[1] = fi[1][6:]
			inv = "black"
		
	with open ("sistema.html", "w") as f:
		f.write (fi[0] + pattern + inv + fi[1])
		
	return index (request)

def info(request):
	with open ("info.txt", "r") as f:
		s = f.read()
		
	return HttpResponse(s)
