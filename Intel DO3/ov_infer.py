import openvino as ov
import cv2
import numpy as np

core = ov.Core()

modle = core.read_model("flower.xml")

compiled_model = core.compile_model(model=modle)

output_key = compiled_model.output(0)

op = "fl.jpg"
img_op = cv2.imread(op)
img_op = cv2.resize(img_op, (180,180))
img_op_n = np.expand_dims(img_op, axis=0)

new = compiled_model(img_op_n)[output_key]
new = np.argmax(new)
class_labels = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']
print(class_labels[new])