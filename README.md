# PoroDet: Nano-porosity detection in TEM images using U-Net and computer vision

[![DOI](https://zenodo.org/badge/1095762451.svg)](https://doi.org/10.5281/zenodo.19342741)

**PoroDet** is a Python package for the contrast-based detection and analysis of nanoporosities in Fresnel-contrast transmission electron microscopy (TEM) images. It utilizes a U-Net convolutional neural network (CNN) to segment and quantify pores and cracks.

The current implementation was developed for oxides formed on zirconium (Zr) alloys, but the same method can be adapted to other materials and microscopy datasets where pores and cracks appear as bright/dark Fresnel features.

---

## Installation

### Step 1: Installing the package

### Option 1: Install directly from GitHub (Recommended for Colab)
Install the package directly into your environment using pip:
```python
pip install git+[https://github.com/Deep7285/PoroDet.git](https://github.com/Deep7285/PoroDet.git)
```
### Option 2 : Install the repository (Recommended for Local Machine)**  
Install the porodet repository in the terminal if you are using  

**Windows:**  
Run the following command in the terminal (e.g., Command Prompt, Anaconda Prompt, or VS Code terminal)  
```bash  
C:\users\home> pip install git+https://github.com/Deep7285/Porodet.git  
```
 
**Linux:**  
1. Create the conda enviroment (optional but recommended). read how to create the conda environment here: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html  
```bash
conda create -n porodet python=3.10
conda activate porodet  
```
2. Run the following command in the terminal in created environment (a VS code provide the terminal).  
```bash
(base) user1@my_pc:~$ conda activate my_new_env  
(my_new_env) user1@my_pc:~& pip install git+https://github.com/Deep7285/Porodet.git
```
## Usage
Once installed, the package can be imported (import porodet) in any Python script or Jupyter Notebook. The package contains five main tools:

## Step 2:  Data Augmentation
Increase dataset diversity by applying augmentation to input TEM images and corresponding binary masks, thereby improving robustness to variations in Fresnel contrast.  
  - Expects grayscale `.tif` images with matching `.png` binary masks.  
  - Applies flips, rotations, brightness/contrast adjustments, gamma/CLAHE, noise, blur and mild geometric distortions.  
  - Saves original and augmented image–mask pairs into a new timestamped output directory.
```python
import porodet
# This triggers the GUI for folder selection
porodet.augment()
```
Note: 
  1. By default, the package resizes the input image into 1024X1024 pixels. 
  2. Keep the square size input images. For example, if input images are 4096X1024 pixel then the image will be distorted during augmentation and    training performance will be affected.

## Step 3: Training the U-net model
Trains a U-Net CNN on the image–mask pairs for pixel-wise nanopore segmentation.  
  - Resizes images and masks to 1024×1024 pixels.  
  - Uses `BCEWithLogitsLoss` and reports training/validation loss and accuracy, as well as segmentation metrics (precision, recall, F1/Dice, IoU, PR–AUC, ROC–AUC).  
  - Performs K-fold cross-validation over the original images (default K = 3).  
  - Saves best model checkpoints, per-fold metric CSV files and plots (loss curves, accuracy curves, PR/ROC curves).
```python
# Starts the training workflow
porodet.train()
```
## Step 4: Nanoporosities detections (Inferences)
Applies a trained U-Net model to a new TEM image.  
  - Loads a `.pth` trained model.  
  - Produces a nanopore probability map, a binary nanopore mask and an overlay on the original TEM image.  
  - Computes basic statistics such as total pore count, total pore area and nanoporosity (%) for the analysed image.  
  - Saves a composite figure (`<image_name>_analysis.png`), the binary mask (`<image_name>_mask.png`) and a metrics text file.
```python
# Select your model and target image via GUI
porodet.detect()
```

## Step 5: Analysis
Performs detailed post-processing on a UNet-generated pore mask.  
  - Loads the binary mask, labels individual features and measures area, aspect ratio (from ellipse fitting) and equivalent diameter.  
  - Classifies objects as nanopores (approximately circular, low aspect ratio) or nanocracks (elongated, high aspect ratio) based on a user-defined aspect-ratio threshold.  
  - Computes the total nanoporosity percentage and the number of pores vs cracks.  
  - Saves histograms of size, aspect ratio and diameter, as well as coloured overlays highlighting pores and cracks separately.
```python
# process a single mask file
porodet.analyze()
```

## Additional Step if needed to fine-tune the trained model or fine-tune the pre-trained model
Fine-tunes an existing PoroDet U-Net model (`.pth`) on a new set of TEM images and masks, and allows freezing the encoder layers to adapt the model to new materials with smaller  datasets.
  - Starts from a pretrained checkpoint (e.g. the Zr-oxide model)  
  - Optionally freezes the encoder and only updates the decoder.
  - Reports the same metrics as the main trainer (loss, accuracy, precision, recall, F1, IoU, Dice, PR-AUC, ROC-AUC)  
```python
# Select pretrained model and new dataset
porodet.finetune()
```
## Instructions to run the package using the Google Colab  
User who prefers to use the Google Colab may use the Google Colab notebook (Training_google_colab.ipynb) in the repository. All instructions are given step by step get the output.   

## Instructions to run the package using local machine    
User who prefers to use the local machine may use the jupyter notebook (jupyter_guide_for_local_machine.ipynb) in the repository. All instructions are given step by step get the output.  

---
## Development Note
This software was developed with the assistance of large language models (LLMs) for code generation and debugging support.
Any contributions or suggestions to the package are welcome.

## Authors
Rajat Nama (University of Oxford)
  - github: https://github.com/rajatnama
  - web: https://nanoanalysis.web.ox.ac.uk/people/rajat-nama

Deepak Kumar (Indian Institute of Technology Madras, India)
  - github: https://github.com/Deep7285
  - web: https://sites.google.com/view/deepak7285/home

## License
This project is licensed under the MIT License. See the LICENSE file for details.




