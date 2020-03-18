#!/bin/bash
#run bash ./script/install.sh from the root folder

apt-get install -y libsm6 libxext6 libxrender-dev
pip install gdown matplotlib pillow==6.2.2 opencv-python

cd save
gdown --id 1gjHR39deUSPChtRbKAD80waoQFTiXyMs #download example checkpoint files
unzip ShapeMGAN-data_plus_model.zip
rm -r data/style
mkdir ../data/rawtext/yaheiB/train
mv data/rawtext/yaheiB/train/*.* ../data/rawtext/yaheiB/train/
mkdir ../data/rawtext/augment
mv data/rawtext/augment/*.* ../data/rawtext/augment/
mv save/*.* ./
rmdir save
rm ShapeMGAN-data_plus_model.zip
rm -r data
