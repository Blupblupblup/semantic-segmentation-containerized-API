# Repository description

Containerized API to count pixels produced by semantic segmentation.

This repo has used content from PyTorch's documentation https://docs.pytorch.org/vision/main/models.html and from Mistral's Le Chat.

# How to test the API

## Without the Docker container

Run the API locally:

```commandline
python flask-api.py
```

Then query the API from the same server:

```commandline
curl -X POST http://localhost:5000/count_cat_pixels   -H "Content-Type: application/json"   -d '{"image_url": "http://images.cocodataset.org/val2017/000000039769.jpg"}'
```

```commandline
curl -X POST http://localhost:5000/count_cat_pixels   -H "Content-Type: application/json"   -d '{"image_url": "https://farm6.staticflickr.com/5291/5496830436_1b355de4c3_z.jpg"}'
```

## With the Docker container

Build the Docker image:

```commandline
docker build -t semant-segm-pix-counter .
```

Launch the container (this will trigger the downloading of the model `fcn_resnet50_coco-1167a1af.pth`):

```commandline
docker run -p 5000:5000 semant-segm-pix-counter
```

Then query the API from the server hosting the container with the previously introduced `curl` commands.