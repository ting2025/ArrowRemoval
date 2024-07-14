#!/bin/bash
#SBATCH --job-name=imgseg
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=5
#SBATCH --partition=gpu3090
#SBATCH --gres=gpu:1
#SBATCH --output=/home/ctleungaf/Pytorch-UNet-master/withsyntrain.out


NUM_NODES=1
NUM_GPUS_PER_NODE=1
NODE_RANK=0
MASTER_PORT=$(shuf -n 1 -i 10000-65535)

DATESTR=$(date +"%m-%d-%H-%M")

set -x
# export TORCH_USE_CUDA_DSA=1
# export CUDA_LAUNCH_BLOCKING=1
torchrun \
    --nproc_per_node=$NUM_GPUS_PER_NODE --nnodes=$NUM_NODES --node_rank $NODE_RANK --master_addr localhost --master_port $MASTER_PORT \
    train.py \
    --epochs 100 \
    --batch-size 12 \
    --validation 20 \
    --learning-rate 0.0001 \
    --scale 1
