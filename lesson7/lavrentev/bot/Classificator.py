import PIL
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

model = load_model('autokeras_lavr.h5')

img = Image.open("1.jpg")
img = img.convert('L')
img = PIL.ImageOps.invert(img)
plt.imshow(img, cmap=plt.cm.binary)
plt.show()
image_array = np.array(img)
image_array = image_array.astype('float')/255.0
#print(image_array)

predicted_class = model.predict(image_array)
for i, x in enumerate((predicted_class*100)[0]):
  print(i, "%.6f" % x)
# print(predicted_class)
print('Predicted class:', np.argmax(predicted_class))