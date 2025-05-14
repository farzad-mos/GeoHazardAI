# Flood Detection from Simulated SAR Data

This repository contains a simple Python-based tool to simulate a Synthetic Aperture Radar (SAR) image and detect flood regions using a basic thresholding technique. It is intended as a prototype to demonstrate the concept of flood detection using remote sensing and can be extended to real satellite data like Sentinel-1.

## Features

- Simulates a SAR backscatter image
- Uses thresholding to detect flood-prone areas
- Visualizes the simulated image and flood mask

## Requirements

- Python 3.x
- numpy
- matplotlib
- scikit-image

Install dependencies via:

```bash
pip install numpy matplotlib scikit-image
```

## How to Run

```bash
python flood_detection.py
```

This will display and save the SAR image and detected flood map as `flood_map.png`.

## Example Output

![Flood Map](flood_map.png)

## Real-World Application

This simplified prototype is inspired by the growing need for rapid flood detection using satellite data during hydrological disasters. By adapting the model to handle Sentinel-1 GRD products, you can scale it up for operational early warning systems or post-disaster assessments.

## Author

[Majid Mostafavi]
