# Galaxy-Classifier-Using-ML

This is a galaxy classifier ML model that uses a CNN to classify galaxies based on their shapes. It is being trained on 24,000 images from SDSS. 
It will be used to classify uncertain galaxies, which are taken from 240,000 galaxy classifications by Galaxy Zoo.

> Note:
> This is an unfinished project and is **currently in active development**. I'm uploading this to Github for the Portfilo for robotics application.
> After finishing this project, a new updated repository will be made.

# Introduction & Developmental Procedure:
* The Galaxy Zoo team is seeking volunteers to classify numerous galaxies that are collected from the James Webb Space Telescope.
* I love astronomy and wanted to do a mini research project, so I decided to code a way to help the Galaxy Zoo Team.
* The first part of my project is learning how to use a CNN and implement galaxy classifications by training my model made from scratch.
   * My current model (last cell of the Google Colab) has an accuracy of around 80%.
   * This is located in the google colab file (.ipynb file)
* The second part of this project was actually utilizing my model to classify uncertain galaxies:
   * To get a list of uncertain galaxies, I used the 2016 Galaxy Zoo excel dataset that has the classifications for over 240,000 galaxies.
   * I developed a script to look through all 240,000 galaxies and find the ones that had uncertain classifications (between 0.4 and 0.6).
   * This script found around ~20,000 uncertain galaxies.
   * However, I couldn't download 20,000 pictures of uncertain galaxies because it would damage my laptop, so I decided to only download about 1500 pictures of the uncertain galaxied using the script.
   * This file is the UncertainClassification.py file
   * These images are waiting for classification after I further improve my model to around 90% accuracy.

# Some Images of Gakaxy Images I collected

There are many images (1500 of them), but these are just snipits.

<img width="1707" height="835" alt="Screenshot 2026-05-02 110318" src="https://github.com/user-attachments/assets/7f6c0a45-4751-4f3d-9f7a-a1efc252af03" />
<img width="1706" height="739" alt="Screenshot 2026-05-02 110305" src="https://github.com/user-attachments/assets/de3a382d-ef42-48aa-b686-d7fd7305badf" />
<img width="1689" height="743" alt="Screenshot 2026-05-02 110248" src="https://github.com/user-attachments/assets/6a3d98d8-8a9d-40b2-8e5e-84295a8dd99f" />
















# Citation: 
Hart et al. (2016), Monthly Notices of the Royal Astronomical Society, 461, 3663. 
