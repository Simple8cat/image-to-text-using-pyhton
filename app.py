## this is my first official project
## this scrit is far from perfect and was made for educational purpose
from math import trunc
from PIL import Image
## i made a function to map average pixel values in a chunk to a value from 0 to 10 
def mapv (k:int,y:int,j:int): 
    res = round((k*j)/y)
    return res
im = Image.open('Image\'s path')
pix = im.load()
## this two for loop makes a color image to black and white image 
for x in range(0, im.size[0]):
    for y in range(0, im.size[1]):
        ## calculate the average value rgb value
        avg_value = (pix[x, y][0]+pix[x, y][1]+pix[x, y][2])/3
        ## put the grey value to the pixels 
        im.putpixel((x, y), (round(avg_value), round(avg_value), round(avg_value), 255))
chunk_size = (3,3) ## you can decide how to devide your picture
l =[]
im.show()
## we pixelate the picture to choose which caracter fit the grey values
for x in range(0, im.size[0], chunk_size[0]):
    for y in range(0, im.size[1],chunk_size[1]):
        s = 0
        ## we claculate the average value of all pixels in a chunck
        for i in range (chunk_size[0]-1):
            for j in range (chunk_size[1]-1):
                if (x+i <= im.size[0]-1 and y+j <= im.size[1]-1):    
                    s= s + pix[x+i,y+j][0]
        avg_pix =   round(s /(chunk_size[0]*chunk_size[1]))
        l.append(mapv(avg_pix,500,10))
        ## rebuild the picture using chunkd
        for i in range (chunk_size[0]):
            for j in range (chunk_size[1]):
                if (x+i <= im.size[0]-1 and y+j <= im.size[1]-1):
                    im.putpixel((x+i,y+j),(avg_pix,avg_pix,avg_pix,255))
## assign every gray value to a specific carater !! this dict is chosen randomly !! If you have suggestions you can contact me 
dic = {
    '0' :'8',
    '1':'u',
    '2':'y',
    '3':'g',
    '4':'Q',
    '5':'|',
    '6':';',
    '7':'o',
    '8':'l',
    '9':':',
    '10':'.'
}
## convert the list using the dict value
im.show()
for i in range(0,len(l)) :
    l[i]= dic[str(l[i])]
x ,y = im.size
x1 , y1 = chunk_size
## print the result
for i in range(0,trunc((x*y)/(x1*y1)),trunc(x/x1)) :
    for j in range(0,trunc(x/x1)):
        if j != trunc(x/x1)-1 :
            print(l[i+j],end='')
        else : 
            print(l[i+j],end='\n')
