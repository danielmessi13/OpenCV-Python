import cv2
import numpy as np

canvas = np.ones((300, 400, 3)) * 255
#imagem 400x300, com fundo branco e 3 canais para as cores
#cv2.imshow("Canvas", canvas)


# desenha a linha diagonal
azul = (255, 0, 0)
cv2.line(canvas, (0, 0), (400, 300), azul)
#img, ponto 1, ponto 2, cor, tickness (timidez)
#cv2.imshow("Canvas", canvas)

# desenha a linha vertical
verde = (0, 255, 0)
cv2.line(canvas, (200, 0), (200, 300), verde, 3)
#img, ponto 1, ponto 2, cor, tickness (timidez)
#cv2.imshow("Canvas", canvas)

# desenha o retângulo com borda verde
cv2.rectangle(canvas, (10, 70), (90, 190), verde)
#img, ponto 1, ponto 2, cor, tickness (timidez)
#cv2.imshow("Canvas", canvas)

# desenha o retângulo todo vermelho
vermelho = (0, 0, 255)
cv2.rectangle(canvas, (250, 50), (300, 125), vermelho, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)