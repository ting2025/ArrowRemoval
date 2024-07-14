# ArrowRemoval
We introduce a method of pretreatment of molecular images in OSCR tasks. 

## Usage
**Use a conda environment for clean installation**
```
$ conda create --name molseg python=3.8.0
$ conda activate molseg
$ conda install pip
$ python3 -m pip install -U pip
$ pip install -r requirements.txt
```
**Data preparation** <br/>
Ground truth images used for training are in RGB format. Image masks should be in Black and White format. they should be in identical names under _imgs_ and _masks_ folders. <br/>
All the images should be squares. Place them on a squared canvas if necessary. The model works well for images sizing under 600*600. <br/>
Mechanistic molecular ground truth data and image segmentation masks can be found on [IMGS](https://doi.org/10.5281/zenodo.11060696) and [MASKS](https://doi.org/10.5281/zenodo.11060696). <br/>

**Model Training**<br/>
Run the training script or train.py.
```
$ sbatch scripts/train.sh
```
Save the best checkpoint to MODEL.pth
**Prediction**<br/>


## Updates
12/7/24 Repository created. Code coming soon.<br/>
14/7/24 Code updated.

