Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> import os
>>> url = "https://en.wikipedia.org/wiki/Chicago_Mercantile_Exchange#/media/File:Cme_building_aerial_view.jpg"
>>> root = "C:\Users\kris\Desktop\photo"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> root = "C:/Users/kris/Desktop/photo"
>>> path = root + url.split('/')[-1]
>>> path
'C:/Users/kris/Desktop/photoFile:Cme_building_aerial_view.jpg'
>>> root = "C:/Users/kris/Desktop/photo/"
>>>  path = root + url.split('/')[-1]
 
SyntaxError: unexpected indent
>>> path = root + url.split('/')[-1]
>>> path
'C:/Users/kris/Desktop/photo/File:Cme_building_aerial_view.jpg'
>>> path = root + url.split(':')[-1]
>>> path
'C:/Users/kris/Desktop/photo/Cme_building_aerial_view.jpg'
>>> try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path, 'wb') as f:
			f.write(r.content)
			f.close()
			print("Pic is saved")
	else:
		print("pic exists")
excepte:
	
SyntaxError: invalid syntax
>>> except:
	
SyntaxError: invalid syntax
>>> try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path, 'wb') as f:
			f.write(r.content)
			f.close()
			print("Pic is saved")
	else:
		print("pic exists")
except:
	print("failing")

	
pic exists
>>> try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path, 'wb') as f:
			f.write(r.content)
			f.close()
			print("Pic is saved")
	else:
		print("pic exists")
except:
	print("failing")

66372
Pic is saved
>>> r.content

>>> r.text

>>> r.text[200:500]
'js";RLCONF={"wgBreakFrames":!1,"wgSeparatorTransformTable":["",""],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgMonthNamesShort":["","Jan","Feb","Mar","'
>>> r.raise_for_status
<bound method Response.raise_for_status of <Response [200]>>
>>> 