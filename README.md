# Overview

This repository contains the source code accompanying the paper

*CHAROT: Robustly controlling chaotic PDEs with partial observations*

by Max Weissenbacher, Anastasia Borovykh and Georgios Rigas

(Accepted at the ICLR 2024 Workshop on AI4Differential Equations in Science.)

# How to run

First install the requirements by running `pip install -r requirements.txt`. (If you are running on MacOS with an M1 chip, you need to install torchrl 0.2.0 from the GitHub repo.)

To run a training script, simply run `python tqc.py`.

All relevant hyperparameters may be changed in 'config.yaml'. In particular, to select which augmentation of TQC should be run, change the network.architecture parameter to one of 'base', 'attention' (= CHAROT) or 'lstm'.
