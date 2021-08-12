from api.resources.coco_names import COCO_INSTANCE_CATEGORY_NAMES as coco_names
import torchvision.transforms as transforms
from PIL import Image
import torchvision
import cv2
import numpy as np
import torch
import ssl

# use unverified ssl
ssl._create_default_https_context = ssl._create_unverified_context

# this will help us create a different color for each class
COLORS = np.random.uniform(0, 255, size=(len(coco_names), 3))

# define the torchvision image transforms
transform = transforms.Compose([
    transforms.ToTensor(),
])

def predict(image, model, device, detection_threshold):
    # transform the image to tensor
    image = transform(image).to(device)
    image = image.unsqueeze(0) # add a batch dimension

    with torch.no_grad():
        outputs = model(image) # get the predictions on the image

    # get all the scores
    scores = list(outputs[0]['scores'].detach().cpu().numpy())

    # index of those scores which are above a certain threshold
    thresholded_preds_inidices = [scores.index(i) for i in scores if i > detection_threshold]

    # get all the predicited class names
    labels = outputs[0]['labels'].cpu().numpy()
    pred_classes = [coco_names[labels[i]] for i in thresholded_preds_inidices]

    return pred_classes

def classify(target_image):
    model = torchvision.models.detection.retinanet_resnet50_fpn(pretrained=True, min_size=800)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    # load the model onto the computation device
    model.eval().to(device)

    image = Image.open(target_image).convert('RGB')
    # a NumPy copy for OpenCV functions
    image_array = np.array(image)
    # convert to OpenCV BGR color format
    image_array = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)

    # get the bounding boxes and class labels
    classes = predict(image, model, device, 0.6)
    
    return classes