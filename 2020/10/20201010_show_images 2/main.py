import glob
import os

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

if __name__ == '__main__':
    all_png = list(glob.glob('../20201007_small_dataset/piglet/*.png'))

    size = len(all_png)
    columns = 5
    rows = np.ceil(size / columns)
    fig = plt.figure(figsize=(8, 8))

    print(f'size: [{size}] rows: [{rows}] columns: [{columns}]')
    for i, png in enumerate(all_png):
        name = os.path.basename(png)
        image = Image.open(png)
        print(f'png: [{name}] size: [{image.height}x{image.width}]')
        ax = fig.add_subplot(rows, columns, i + 1)
        ax.title.set_text(name)
        plt.imshow(image)

    plt.tight_layout()  # prevent label overlap
    plt.show()
