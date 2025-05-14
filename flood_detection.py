import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure

def simulate_sar_image(size=(100, 100), flood_region=(slice(30, 70), slice(30, 70))):
    image = np.random.normal(loc=0.3, scale=0.05, size=size)
    image[flood_region] = np.random.normal(loc=0.1, scale=0.02, size=image[flood_region].shape)
    return exposure.rescale_intensity(image, out_range=(0, 1))

def threshold_flood_detection(image, threshold=0.15):
    return image < threshold

if __name__ == "__main__":
    sar_image = simulate_sar_image()
    flood_mask = threshold_flood_detection(sar_image)

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(sar_image, cmap='gray')
    axs[0].set_title("Simulated SAR Image")
    axs[0].axis('off')

    axs[1].imshow(flood_mask, cmap='Blues')
    axs[1].set_title("Detected Flood Regions")
    axs[1].axis('off')

    plt.tight_layout()
    plt.savefig("flood_map.png")
    plt.show()
