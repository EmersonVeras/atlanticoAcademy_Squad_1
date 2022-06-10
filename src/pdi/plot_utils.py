import matplotlib.pyplot as plt

def plot_images(images, titles):
    fig, axes = plt.subplots(ncols=len(images), figsize=(9, 3), sharex=True, sharey=True)
    ax = axes.ravel()

    index = 0
    for image, title in zip(images, titles):        
        ax[index].imshow(image, cmap=plt.cm.gray)
        ax[index].set_title(title)
        index = index + 1
    for a in ax:
        a.set_axis_off()
    fig.tight_layout()
    plt.show()