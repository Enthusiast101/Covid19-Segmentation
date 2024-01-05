# **COVID 19 Lung Segmentation using various U-Net Models**

## Computational Resources
These models were trained and validated using these resources:
CPU: AMD Ryzen 5800H
GPU: NVDIA RTX 3050 mobile (4GB)
RAM: 16 GB DDR4

## Data
The original data is availaible at [Covid-19 CT scans](https://www.kaggle.com/datasets/andrewmvd/covid19-ct-scans) and data preprocessing is done on it.

After preprocessing we recieve .nii images of ct_scan, lung_mask, infection_mask and lung_and_infection_mask which are of dimension (512, 512, 200) each.
These images are then processed and arranged in lung and infection sets with dimesion (3520, 128, 128, 1) each.

## Data Augmentation
Minimal Data augmentation is done in model layer itself.
'DA' abbreviation is marked when data augmentation layers are applied

## Models
### U-Net
Simple, vanilla U-Net implementation is done. 

<img src="https://github.com/Enthusiast101/Covid-19-Lung-Infection-Segmentation/assets/89479662/133884c0-8f81-47af-93a0-2c0f145d630e" width="1100" height="500" />  

| Metrics | Score |
| ------------- | ------------- |
| Jaccard Index (training) | 0.9020136 |
| Jaccard Index (testing) | 0.89031833 |

### U-Net Squared

<img src="https://github.com/Enthusiast101/Covid-19-Lung-Infection-Segmentation/assets/89479662/ace6ee11-9ca0-4b94-b69c-df33bd01cbad" width="1100" height="500" /> 

| Metrics | Score |
| ------------- | ------------- |
| Jaccard Index (training) | 0.9230074 |
| Jaccard Index (testing) | 0.88798153 |

### Attention U-Net

<img src="https://github.com/Enthusiast101/Covid-19-Lung-Infection-Segmentation/assets/89479662/8cf54ecb-6a29-4a88-b934-4b32a4ace39c" width="1100" height="500" /> 

| Metrics | Score |
| ------------- | ------------- |
| Jaccard Index (training) | 0.8733221 |
| Jaccard Index (testing) | 0.8631426 |

### Res U-Net

<img src="https://github.com/Enthusiast101/Covid-19-Lung-Infection-Segmentation/assets/89479662/4f112dd5-9bed-49ac-9258-bebc4b10e376" width="1100" height="500" /> 

| Metrics | Score |
| ------------- | ------------- |
| Jaccard Index (training) | 0.9140699 |
| Jaccard Index (testing) | 0.8803004 |

### Recurrent U-Net

<img src="https://github.com/Enthusiast101/Covid-19-Lung-Infection-Segmentation/assets/89479662/d8bee1b5-bc68-4cb1-b236-fe097ccb065f" width="1100" height="500" /> 

| Metrics | Score |
| ------------- | ------------- |
| Jaccard Index (training) | 0.9020136 |
| Jaccard Index (testing) | 0.89031833 |

### Swin U-Net

<img src="https://github.com/Enthusiast101/Covid-19-Lung-Infection-Segmentation/assets/89479662/b7b75069-852e-41e7-95a9-64e9afc84e89" width="1100" height="500" /> 

| Metrics | Score |
| ------------- | ------------- |
| Jaccard Index (training) | 0.8356 |
| Jaccard Index (testing) | 0.837337 |

### Trans U-Net

<img src="https://github.com/Enthusiast101/Covid-19-Lung-Infection-Segmentation/assets/89479662/18572715-6431-44de-a492-b25227f2073b" width="1100" height="500" /> 

| Metrics | Score |
| ------------- | ------------- |
| Jaccard Index (training) | NA |
| Jaccard Index (testing) | NA |

*Note*: NA indicates the loss of computational resources and not that the model behaved poorly.

## Results

<img src="https://github.com/Enthusiast101/Covid-19-Lung-Infection-Segmentation/assets/89479662/08f10997-ef64-4510-bb42-0927a22e430d" width="1100" height="500" /> 

