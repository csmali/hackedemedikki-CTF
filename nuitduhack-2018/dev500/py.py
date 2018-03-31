from PIL import Image
import wget
url = 'http://shreddinger.challs.malice.fr/challenge_accepted'
filename = wget.download(url)

import zipfile
zip_ref = zipfile.ZipFile(filename, 'r')
zip_ref.extractall("extract")
zip_ref.close()

width = 1000
height = 1400

img = Image.new('RGB', (width,height))
i = 1
k=1
common=[]
current=[]
next=[]
used = []

is_reverse=False
current_max = 1


i=1
notFound = True

'''
while i < 100:

    to_paste = Image.open("extract/" + str(i) + ".png", "r")
    current_pix = to_paste.load()
    for k in range (0,10):
    	for j in range (650,750):
		
		current_pix[k,j] = (255,255,255)
    
    to_paste.save("extracted/"+str(i)+".png", "PNG")
    i = i + 1
i=1
'''

offset = ((i*10),0)
to_paste_image = Image.open("extract/" + str(current_max) + ".png", "r")
img.paste(to_paste_image,offset)
while i < 100:
    current_cnt = 0

    k=1
    to_paste = Image.open("extract/" + str(current_max) + ".png", "r")
    current_max = 0
    if is_reverse:
    	to_paste = to_paste.rotate(180)

    current_pix = to_paste.load()
    is_reverse=False
    while k < 100 :
	
	if k not in used and k != i:
	    	to_check = Image.open("extract/" + str(k) + ".png", "r")
		pix = to_check.load()
		cnt = 0
	   	cnt_reverse = 0

		for j in range (0,1400):
			if (current_pix[9,j][0] - pix[0,j][0] < 30 and  current_pix[9,j][0] - pix[0,j][0] > -30):
				cnt = cnt + 1 

		if cnt > current_cnt  :
			current_cnt = cnt
			current_max = k
			is_reverse=False
	
		#reverse
		for j in range (0,1400):
			if (current_pix[9,j][0] - pix[0,1399-j][0] < 30 and  current_pix[9,j][0] - pix[0,1399-j][0] > -30):
				cnt_reverse = cnt_reverse + 1 

	
		if cnt_reverse > current_cnt:
			current_cnt = cnt_reverse
			current_max = k
			is_reverse=True

	k=k+1
		

    print(current_max)
    offset = ((i*10),0)
    to_paste_image = Image.open("extract/" + str(current_max) + ".png", "r")
    used.append(current_max)
    if is_reverse:
	    imgtemp=to_paste_image.rotate(180)
	    img.paste(imgtemp,offset)
    else:
	    img.paste(to_paste_image,offset)

    i = i + 1


img.save("output.jpeg", "JPEG")
to_paste = Image.open("output.jpeg")
img2 = to_paste.rotate(180)
img2.save("outputrev.jpeg", "JPEG")
