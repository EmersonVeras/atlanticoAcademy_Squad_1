import os

def list_images(path):
    return [f for f in os.listdir(path) if f.endswith('.jpg')]