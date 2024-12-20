# Overview

This repository contains the source code accompanying the paper

[CHAROT: Robustly controlling chaotic PDEs with partial observations](https://openreview.net/pdf?id=SytuCWihJr)

Accepted at the ICLR 2024 Workshop on AI4Differential Equations in Science.

# To install (with dev dependencies)

```
cd charot
python -m venv .venv && . .venv/bin/activate
pip install --upgrade pip
pip install -e '.[dev]'
```

# How to run

Create a virtual environment (recommended)

```
python -m venv .venv
```

Activate

```
. .venv/bin/activate
```

Install

```
pip install --upgrade pip
cd charot && pip install .
```

For a development install

```
pip install '.[dev]'
```



First install the requirements by running `pip install -r requirements.txt`. (If you are running on MacOS with an M1 chip, you need to install torchrl 0.2.0 from the GitHub repo.)

To run a training script, simply run `python tqc.py`.

All relevant hyperparameters may be changed in 'config.yaml'. In particular, to select which augmentation of TQC should be run, change the network.architecture parameter to one of 'base', 'attention' (= CHAROT) or 'lstm'.


