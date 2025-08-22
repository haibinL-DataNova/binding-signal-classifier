# binding-signal-classifier
This project applies a CNN-LSTM hybrid architecture to classify biosensor signal patterns into binding vs. non-binding events.he system includes preprocessing pipelines, model training scripts, and interactive dashboards for visualizing charge interaction events across test conditions.

# Biosensor Oscillation Classifier

A deep learning pipeline to classify biosensor signal patterns into binding vs non-binding events. Built with CNN-LSTM architecture and visualized using Dash.

## Features
- Signal normalization and segmentation
- CNN-LSTM hybrid model
- Precision-focused evaluation
- Interactive dashboard

## Usage
1. Place your signal data in `data/sample_signals.csv`
2. Run preprocessing and model training via `notebooks/model_training.ipynb`
3. Launch dashboard with `python dashboard/app.py`
