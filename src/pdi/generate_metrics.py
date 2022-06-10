from chan_vese import chan_vese_segmentation
from otsu import otsu_segmentantion
import matplotlib.pyplot as plt


def segment(image, gold_standard):
    technique_01 = chan_vese_segmentation(image)
    technique_02 = otsu_segmentantion(image)


def plot_images(img1, img2, img3):
    fig, axes = plt.subplots(ncols=3, figsize=(9, 3), sharex=True, sharey=True)
    ax = axes.ravel()

    ax[0].imshow(img1, cmap=plt.cm.gray)
    ax[0].set_title('img1')
    ax[1].imshow(-img2, cmap=plt.cm.gray)
    ax[1].set_title('img2')
    ax[2].imshow(img3, cmap=plt.cm.gray)
    ax[2].set_title('img3')

    for a in ax:
        a.set_axis_off()

    fig.tight_layout()
    plt.show()
