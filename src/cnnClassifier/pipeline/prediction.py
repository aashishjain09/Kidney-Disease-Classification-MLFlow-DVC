import os, numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
    
    def predict(self):
        # Load Model
        model = load_model(os.path.join("model", "model.h5"))

        test_image = np.expand_dims(image.img_to_array(image.load_img(self.filename, target_size = (224, 224))), axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        prediction = "Tumor" if result[0] == 1 else "Normal"
        return [{"image" : prediction}]
