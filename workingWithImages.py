from PIL import Image
import csv

# mac=Image.open('C:\\Users\\malip\\OneDrive\\Desktop\\word_matrix.png')
# mac.crop((0,0,100,100))
# mac.show()

with open('csv.csv','r')as file:
	f=csv.reader(file)
	link=[]
	for i,j in enumerate(f):
		link.append(j[i])

	print(''.join(link))
