# **COVID 19 Lung Segmentation using various U-Net Models**
## Data
The original data is availaible at [Covid-19 CT scans](https://www.kaggle.com/datasets/andrewmvd/covid19-ct-scans) and data preprocessing is done on it.

After preprocessing we recieve .nii images of ct_scan, lung_mask, infection_mask and lung_and_infection_mask which are of dimension (512, 512, 200) each.
These images are then processed and arranged in lung and infection sets with dimesion (3520, 128, 128, 1) each.

## Data Augmentation
Minimal Data augmentation is done in model layer itself.

## Models
### U-Net
### U-Net Squared
### Attention U-Net
### Res U-Net
### LSTM U-Net
### GRU U-Net
### Recurrent U-Net
### Swin U-Net
### Trans U-Net
