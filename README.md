# Repository description

Containerized API to count pixels produced by semantic segmentation class masks.

This repo has used content from PyTorch's documentation https://docs.pytorch.org/vision/main/models.html and from Mistral's Le Chat.

# How to use the API

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

# How to conduct load testing using Locust

The `Locust` library is used for load testing, i.e. simulating concurrent users sending requests to the API (cf. https://docs.locust.io/en/stable/writing-a-locustfile.html).

To launch `Locust` locally run:
```commandline
locust -f load_testing.py
```
then go to http://127.0.0.1:8089 in your browser to configure the number of users defining peak concurrency. Host should be set to http://127.0.0.1:5000 to correspond to our pixels counting API.