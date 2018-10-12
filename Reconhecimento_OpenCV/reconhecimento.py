# coding=utf-8
import cv2
import numpy as np

# carregar as imagens
img1 = cv2.imread("ESTEIRA0.jpg")
img2 = cv2.imread("ESTEIRA1.jpg")
img3 = cv2.imread("mask.jpg")

# convert the images for gray scale
imgray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
imgray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
maskgray = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)

# cv2.imshow("Segunda",imgray2)
# cv2.imshow("Terceira",maskgray3)
# cv2.imshow("Terceira",imgray3)
# cv2.waitKey(0)

# procura diferença entre as duas img
diference = cv2.subtract(imgray1, imgray2)

# Se não fizer isso alguns pixels não vão ser binarios e vão mostrar cores diferentes
diference[diference > 0] = 255

# Kernel pra usar na função de tirar os contornos errados
kernel = np.ones((2, 2), np.uint8)

# Tirar erros
erode = cv2.erode(diference, kernel, iterations=2)
maskerode = cv2.erode(maskgray, kernel, iterations=2)

# Procurar contornos
im1, cont1, hier1 = cv2.findContours(maskerode, cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_NONE)

#find contours
im2, cont, hier = cv2.findContours(erode, cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_NONE)

fruits = [0,0,0]
for i in range(0, len(cont)):
    result = [0,0]
    for j in range(0, len(cont1)):
        result[j] = cv2.matchShapes(cont1[j], cont[i], 1, 0)
    index = result.index(min(result))
    if index is 0:
        fruits[i] = "banana"
        print min(result)
    else:
        fruits[i] = "laranja"
        print min(result)
fruits = np.array(fruits)

# draw the rectangle of the contour
if len(cont) > 0:
    num = 0
    for c in cont:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(img2, (x,y), (x+w,y+h), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img2,fruits[num],(x,y-10), font, 0.8,(0,255,0),2,cv2.LINE_AA)
        num += 1

# show the result
if result is not True:
    cv2.imshow('DETECCAO', img2)
    cv2.waitKey(0)
else:
    print("Não há itens!!")

# A função toma três argumentos: a imagem a ser erodida,
# o kernel que é basicamente um quadrado que será aplicado como erosão, logo acima eu criei um array 2×2
# zeros tipo uint8. E por último o iterations, que é a quantidade de vezes que será aplicado o processo de erosão.
# Tanto o tamanho do kernel e o iterations vão variar de acordo com a aplicação, então se você precisar utilizar,
# terá que testar na prática qual configuração lhe dá o melhor resultado. Neste caso poderia usar outra função chamada
# cv2.morphologyEx().
