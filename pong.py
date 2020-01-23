import cv2
import numpy as np

#Global Variables to be used through our program

WINDOWWIDTH = 400
WINDOWHEIGHT = 300
LINETHICKNESS = 10

#captura = cv2.VideoCapture(0)

#Main function

#Keeps track of ball direction
ballDirX = 10 ## -1 = left 1 = right
ballDirY = 10 ## -1 = up 1 = down
    
x = 1
y = 1

while True: #main game loop
	#ret,imagen = captura.read()

	imagen = np.zeros((WINDOWHEIGHT,WINDOWWIDTH,3), np.uint8)
	imagen[:,:]=(255,255,255) #color de fondo
	

	#imagen = cv2.resize(imagen,(400,300))

	cv2.circle(imagen,(x,y),10,(0,0,255),-1)


	cv2.line(imagen, (0, 0), (250, 250), (0, 255, 0), 1) 
	


	x += ballDirX
	y += ballDirY
	
	if x >= WINDOWWIDTH or x <= 0:
		ballDirX = ballDirX * -1
	if y >= WINDOWHEIGHT or y <= 0:
		ballDirY = ballDirY * -1
		
	cv2.imshow("Pong",imagen)
		
	k = cv2.waitKey(1) & 0xFF
	if k==27:
		break
		
cv2.destroyAllWindows()
