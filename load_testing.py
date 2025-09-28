from locust import HttpUser, task, between

class PixelCounterUser(HttpUser):
    wait_time = between(0.5, 3)

    @task
    def count_cat_pixels(self):
        payload = {"image_url": "http://images.cocodataset.org/val2017/000000039769.jpg"}
        headers = {"Content-Type": "application/json"}
        self.client.post("/count_cat_pixels", json=payload, headers=headers)

    @task
    def count_cat_pixels(self):
        payload = {"image_url": "https://farm2.staticflickr.com/1326/5164178695_2c03ab4d4d_z.jpg"}
        headers = {"Content-Type": "application/json"}
        self.client.post("/count_cat_pixels", json=payload, headers=headers)
        self.client.post("/count_cat_pixels", json=payload, headers=headers)
        self.client.post("/count_cat_pixels", json=payload, headers=headers)
        self.client.post("/count_cat_pixels", json=payload, headers=headers)