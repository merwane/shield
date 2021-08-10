from config import OPERATING_SYSTEM
import os

if OPERATING_SYSTEM == "Linux":
    from imageai.Classification import ImageClassification
    
    execution_path = os.getcwd()
    model_path = "{}/model/{}".format(execution_path, "resnet.h5")
    prediction = ImageClassification()
    prediction.setModelTypeAsResNet50()
    prediction.setModelPath(model_path)
    prediction.loadModel()

else:
    print("--- Classification not implemented in Darwin test mode ---")

def classify(image_path):
    labels = []

    if OPERATING_SYSTEM == "Linux":
        predictions, probabilities = prediction.classifyImage(image_path, result_count=5)
        for index in range(len(predictions)):
            if probabilities[index] > 10:
                labels.append(predictions[index])
            else:
                pass
    elif OPERATING_SYSTEM == "Darwin":
        pass
        
    return labels