import cv2
from google.colab.patches import cv2_imshow

def show(img):
  img = cv2.imread("/content/drive/MyDrive/ImageRestoration/RWNN/examples/pnp/deblur/1_degraded_0_kernel.png")
  cv2_imshow(img)