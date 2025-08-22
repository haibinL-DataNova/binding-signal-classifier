from src.preprocess import load_and_preprocess
from src.model import build_model
import numpy as np

def test_preprocessing():
    df = load_and_preprocess('data/sample_signals.csv')
    assert 'scaled_signal' in df.columns
    assert df['scaled_signal'].between(0, 1).all()

def test_model_build():
    model = build_model((3, 1))
    assert model.output_shape == (None, 1)
