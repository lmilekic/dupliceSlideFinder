import numpy as np
import cv2
import corrConv

im1 = cv2.imread('./slides/no-u-final-slide525.png')
im2 = cv2.imread('./slides/no-u-final-slide648.png')

results =  corrConv.fastCorr(im1, im2, 5)

cv2.imshow('results',results)
cv2.waitKey(0)

cv2.imwrite('./results/slide525.png', im1)
cv2.imwrite('./results/slide648.png', im2)
cv2.imwrite('./results/correlation.png', results)
#cv2.imshow('image', im1)
#cv2.waitKey(0)

