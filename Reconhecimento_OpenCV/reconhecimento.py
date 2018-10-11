import cv2
import numpy as np

# carregar as imagens
img1 = cv2.imread("ESTEIRA0.jpg")
img2 = cv2.imread("ESTEIRA1.jpg")
img3 = cv2.imread("mask.jpg")

# convert the images for gray scale
imgray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
imgray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
maskgray3 = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)

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

# mostra a diferença
cv2.imshow('DETECCAO', erode)

# A função toma três argumentos: a imagem a ser erodida,
# o kernel que é basicamente um quadrado que será aplicado como erosão, logo acima eu criei um array 2×2
# zeros tipo uint8. E por último o iterations, que é a quantidade de vezes que será aplicado o processo de erosão.
# Tanto o tamanho do kernel e o iterations vão variar de acordo com a aplicação, então se você precisar utilizar,
# terá que testar na prática qual configuração lhe dá o melhor resultado. Neste caso poderia usar outra função chamada
# cv2.morphologyEx().

# wait any key to close the window
cv2.waitKey(0)