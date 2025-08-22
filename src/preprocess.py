import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_and_preprocess(filepath):
    df = pd.read_csv(filepath, parse_dates=['timestamp'])
    df.sort_values('timestamp', inplace=True)
    
    scaler = MinMaxScaler()
    df['scaled_signal'] = scaler.fit_transform(df[['signal_value']])
    
    return df
