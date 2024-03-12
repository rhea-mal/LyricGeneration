import pandas as pd
import numpy as np
import random

def main():
    print("\nReading file...")
    df = pd.read_csv('final_lyrics_features_combined.csv')

    print("\nRead file...")
    print("\nTotal lines ", len(df))

    # Shuffle the dataframe
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    train_size = int(0.8 * len(df))
    val_size = int(0.1 * len(df))
    test_size = len(df) - train_size - val_size

    # Split the dataframe into train, val, and test sets
    train_df = df.iloc[1:train_size]
    val_df = df.iloc[train_size:train_size + val_size]
    test_df = df.iloc[train_size + val_size:]

    # Modify test_df to have empty strings for Lyrics
    test_df['Lyrics'] = np.nan

    print("\nCreating train file...")
    train_df.to_csv('train_data.csv', index=False)
    print("\nCreated train file...")

    print("\nCreating val file...")
    val_df.to_csv('val_data.csv', index=False)
    print("\nCreated val file...")

    print("\nCreating test file...")
    test_df.to_csv('test_data.csv', index=False)
    print("\nCreated test file...")

if __name__ == '__main__':
    main()