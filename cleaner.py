import pandas as pd

def clean_sales_data(input_file, output_file):
    # Load messy data
    df = pd.read_csv(input_file)

    # 1. Remove duplicates
    df = df.drop_duplicates()

    # 2. Fix dates - handles DD/MM/YYYY, YYYY-MM-DD, etc.
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # 3. Clean product names - strip spaces, title case
    df['Product'] = df['Product'].str.strip().str.title()

    # 4. Fill missing prices with product average
    df['Price'] = df.groupby('Product')['Price'].transform(
        lambda x: x.fillna(x.mean())
    )

    # 5. Fill missing quantity with 1
    df['Quantity'] = df['Quantity'].fillna(1)

    # 6. Create Total column
    df['Total'] = df['Price'] * df['Quantity']

    # 7. Remove rows where Date is still missing
    df = df.dropna(subset=['Date'])

    # 8. Sort by date
    df = df.sort_values('Date')

    # Save clean file
    df.to_excel(output_file, index=False)

    # Print summary
    print(f"Cleaned {len(df)} rows")
    print(f"Total Sales: ${df['Total'].sum():,.2f}")
    print(f"Date Range: {df['Date'].min()} to {df['Date'].max()}")
    return df

if __name__ == "__main__":
    clean_sales_data("sample_messy_sales.csv", "sample_cleaned_sales.xlsx")
