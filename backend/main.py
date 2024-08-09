# main.py
import sys
import os
import torch
sys.path.append(os.path.join(os.path.dirname(__file__), 'dressing-in-order'))
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from models.dior_model import DIORModel
from datasets.deepfashion_datasets import DFVisualDataset

# Setup environment
repo_name = 'dressing-in-order'
if not os.path.exists(repo_name):
    os.system(f'git clone https://github.com/cuiaiyu/{repo_name}')
os.chdir(f'./{repo_name}')

# Define options class (dummy argparse)
class Opt:
    def __init__(self):
        pass

opt = Opt()
opt.dataroot = 'data'
opt.isTrain = False
opt.phase = 'test'
opt.n_human_parts = 8
opt.n_kpts = 18
opt.style_nc = 64
opt.n_style_blocks = 4
opt.netG = 'diorv1'
opt.netE = 'adgan'
opt.ngf = 64
opt.norm_type = 'instance'
opt.relu_type = 'leakyrelu'
opt.init_type = 'orthogonal'
opt.init_gain = 0.02
opt.gpu_ids = [0]
opt.frozen_flownet = True
opt.random_rate = 1
opt.perturb = False
opt.warmup = False
opt.name = 'DIORv1_64'
opt.vgg_path = ''
opt.flownet_path = ''
opt.checkpoints_dir = 'checkpoints'
opt.frozen_enc = True
opt.load_iter = 0
opt.epoch = 'latest'
opt.verbose = False

# Create and setup model
if not os.path.exists("checkpoints/DIORv1_64"):
    os.system("gdown --id 1MyHq-P0c8zz7ey7p_HTTZKeMie5ZuNlb -O checkpoints/DIORv1_64")
model = DIORModel(opt)
model.setup(opt)

# Load data
ds = DFVisualDataset(dataroot=opt.dataroot, dim=(256, 176), n_human_part=8)

# Define function to dress a person with a garment
def dress_person_with_garment(person_image, garment_image):
    # Load person and garment images
    person_img = Image.open(person_image).convert('RGB')
    garment_img = Image.open(garment_image).convert('RGB')

    # Assuming the images are processed similarly to dataset images
    person = ds.process_img(person_img)
    garment = ds.process_img(garment_img)

    # Run the dressing-in-order pipeline
    pimg, gimgs, oimgs, gen_img, pose = model.dress_in_order(person, garment)

    # Save and display the output
    output_img = Image.fromarray((gen_img.float().cpu().numpy().transpose(1, 2, 0) * 255).astype(np.uint8))
    output_img.save('output.png')
    plt.imshow(output_img)
    plt.axis('off')
    plt.show()

# Example usage
if __name__ == "__main__":
    person_image_path = input("Enter the path to the person's image: ")
    garment_image_path = input("Enter the path to the garment's image: ")
    dress_person_with_garment(person_image_path, garment_image_path)
