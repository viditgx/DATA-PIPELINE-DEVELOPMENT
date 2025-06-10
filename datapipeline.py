import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def extract_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    return df

def transform_data(df):
    if df.isnull().values.any():
        df.fillna(df.mean(numeric_only=True), inplace=True)
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df.drop('target', axis=1))
    df_scaled = pd.DataFrame(scaled_features, columns=df.columns[:-1])
    df_scaled['target'] = df['target']
    return df_scaled

def load_data(df):
    train, test = train_test_split(df, test_size=0.2, random_state=42)
    train.to_csv("train_data.csv", index=False)
    test.to_csv("test_data.csv", index=False)

def main():
    df = extract_data()
    df_transformed = transform_data(df)
    load_data(df_transformed)

if __name__ == "__main__":
    main()
