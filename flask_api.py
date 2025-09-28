# inspired by https://docs.pytorch.org/vision/main/models.html

from flask import Flask, request, jsonify
from PIL import Image
import requests
import numpy as np
from torchvision.models.segmentation import fcn_resnet50, FCN_ResNet50_Weights

app = Flask(__name__)

weights = FCN_ResNet50_Weights.DEFAULT
model = fcn_resnet50(weights=weights)
model.eval()
preprocess = weights.transforms()

@app.route('/count_cat_pixels', methods=['POST'])
def count_cat_pixels():
    # Get the image URL from the request
    data = request.get_json()
    image_url = data.get('image_url')
    if not image_url:
        return jsonify({'error': 'No image URL provided'}), 400

    try:
        img = Image.open(requests.get(image_url, stream=True).raw)

        batch = preprocess(img).unsqueeze(0)

        prediction = model(batch)["out"]
        normalized_masks = prediction.softmax(dim=1)
        class_to_idx = {cls: idx for (idx, cls) in enumerate(weights.meta["categories"])}
        mask = normalized_masks[0, class_to_idx["cat"]]

        return jsonify({'cat_pixel_count': int(np.sum(mask.detach().numpy()>0.5))})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
