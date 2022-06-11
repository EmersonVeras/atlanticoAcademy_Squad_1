from sklearn.cluster import KMeans
import numpy as np


# See https://www.analyticsvidhya.com/blog/2019/04/introduction-image-segmentation-techniques-python/


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def kmeans_segmentation(image):
    
    pic = image/255 
    pic_n = pic.reshape(pic.shape[0]*pic.shape[1], pic.shape[2])   
    kmeans = KMeans(n_clusters=2, random_state=0).fit(pic_n)
    pic2show = kmeans.cluster_centers_[kmeans.labels_]
    
    cluster_pic = pic2show.reshape(pic.shape[0], pic.shape[1], pic.shape[2]) * 255    
    cluster_pic = rgb2gray(cluster_pic)
    cluster_pic = cluster_pic.astype(np.int16)

    # to make sure that or object of interest is white
    # we assume that most of the image is background, so if the mean is more than 0.5
    # it means that the background is white 
    if cluster_pic.mean() > 0.5:
        cluster_pic = ~cluster_pic
    
    return cluster_pic