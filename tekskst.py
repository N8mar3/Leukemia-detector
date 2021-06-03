import torch
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image as im
from main_canny_edge_maker import canny


d = 'C:/Coding/#Data/for_#3/clean/all/data/ALL_21.bmp'
threshold = 0.038


def get_img(path):
    image = im.open(path)
    images = np.asarray(image).copy()
    return images


def show_img(array):
    print(array.shape)
    data = array.expand(1920, 2560, 3).to(torch.float).cpu().detach().numpy()
    plt.imsave('canny_21.jpeg', data)
    plt.imshow(array)
    plt.show()


def main(path, cannys):
    image = get_img(path)
    if cannys:
        image = torch.movedim(torch.tensor(image), -1, 0)
        print(image.shape)
        image = canny(image)
        image = torch.squeeze(image, 0)
        image = torch.movedim(image, 0, -1)/torch.max(image).item()
        image = torch.where(image > threshold , 1, 0)
    show_img(image)


main(d, cannys=True)
