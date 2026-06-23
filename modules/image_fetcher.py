import requests


def fetch_image(keyword):

    url = f"https://picsum.photos/1080/1920"

    response = requests.get(url)

    image_path = "static/background.jpg"

    with open(image_path, "wb") as f:

        f.write(response.content)

    return image_path