"""Clean and analyze Statcast data from CSV. Currently optimized for recent (2025) statcast data and may break with older schemas"""

import pandas as pd

from config import year


def debug_print(pitches):
        # Debug printing - data shape and structure
    print("\n" + "="*60)
    print("DATA SHAPE AND STRUCTURE (AFTER CLEANING)")
    print("="*60)
    print(f"Shape: {pitches.shape[0]:,} rows × {pitches.shape[1]} columns")
    print(f"Memory usage: {pitches.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    
    print("\n" + "-"*60)
    print("COLUMN NAMES")
    print("-"*60)
    print(f"Total columns: {len(pitches.columns)}")
    for i, col in enumerate(pitches.columns, 1):
        print(f"{i:3d}. {col}: {pitches.dtypes.iloc[i-1]}")
    
    print("\n" + "-"*60)
    print("FIRST FEW ROWS")
    print("-"*60)
    print(pitches.head())
    
    print("\n" + "-"*60)
    print("BASIC STATISTICS")
    print("-"*60)
    print(pitches.describe())
    
    print("\n" + "-"*60)
    print("MISSING VALUES")
    print("-"*60)
    missing = pitches.isnull().sum()
    missing_pct = (missing / len(pitches) * 100).round(2)
    missing_df = pd.DataFrame({
        'NA Count': missing,
        'NA %': missing_pct
    })
    print(missing_df[missing_df['NA Count'] > 0].sort_values('NA Count', ascending=False))

def main():
    """Load Statcast data and display debug information."""
    csv_file = f"{year}_statcast.csv"
    
    print(f"Loading data from {csv_file}...")
    pitches = pd.read_csv(csv_file)
    
    # Show original shape
    original_shape = pitches.shape
    print(f"Original shape: {original_shape[0]:,} rows × {original_shape[1]} columns")
    
    # Remove columns that are entirely NA/null
    cols_before = pitches.shape[1]
    pitches = pitches.dropna(axis=1, how='all')
    cols_removed = cols_before - pitches.shape[1]
    if cols_removed > 0:
        print(f"Removed {cols_removed} column(s) with only NA/null values")
    
    # Remove rows that are entirely NA/null
    rows_before = pitches.shape[0]
    pitches = pitches.dropna(axis=0, how='all')
    rows_removed = rows_before - pitches.shape[0]
    if rows_removed > 0:
        print(f"Removed {rows_removed} row(s) with only NA/null values")

    # Remove rows where game_type is exhibition or spring training
    if 'game_type' in pitches.columns:
        before_rows = pitches.shape[0]
        pitches = pitches[~pitches['game_type'].isin(['E', 'S'])].reset_index(drop=True)
        after_rows = pitches.shape[0]
        removed = before_rows - after_rows
        if removed > 0:
            print(f"Removed {removed} rows where game_type was 'E' or 'S'")
    else:
        print("Warning: 'game_type' column not found in dataset.")
    
    debug_print(pitches)
    
    output_file = f"{year}_statcast_cleaned.csv"
    pitches.to_csv(output_file, index=False)
    print(f"Cleaned data written to {output_file}")


if __name__ == "__main__":
    pitches = main()

