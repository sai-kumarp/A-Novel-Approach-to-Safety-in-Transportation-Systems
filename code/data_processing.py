import pandas as pd


def load_data(file_path):
    """Load CSV file"""
    return pd.read_csv(file_path)


def clean_data(df):
    """Clean missing values & incorrect formats"""
    df = df.dropna()
    df["speed"] = df["speed"].astype(int)
    df["temperature"] = df["temperature"].astype(float)
    return df


def analyze_data(df):
    """Analyze for hazards"""
    df["over_speed"] = df["speed"] > 80
    df["high_temp"] = df["temperature"] > 60
    df["hazard"] = df["over_speed"] | df["high_temp"]
    return df
