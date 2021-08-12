def classify(image_path):
    labels = []

    predictions = [] # TODO: fill
    for index in range(len(predictions)):
        if probabilities[index] > 10:
            labels.append(predictions[index])
        else:
            pass
        
    return labels