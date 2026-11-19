# Excel Cleaner - Automated Sales Data Cleaning

**Problem:** A retail shop owner was spending 4 hours every Monday cleaning a messy sales CSV with duplicates, wrong dates, and missing prices.

**Solution:** This Python script cleans the file in 30 seconds.

### What it does:
- Removes duplicate rows
- Fixes dates in different formats (DD/MM/YYYY, YYYY-MM-DD)
- Cleans product names (removes extra spaces, fixes caps)
- Fills missing prices using product average
- Creates a Total column (Price x Quantity)
- Exports a clean Excel file ready for reporting

### Before vs After:
**Before:** 5,000 rows, 340 duplicates, 120 missing prices, dates in 3 formats
**After:** 4,660 clean rows, 0 duplicates, 0 missing prices, 1 date format

### How to run:
pip install -r requirements.txt
python cleaner.py

### Tools: Python, Pandas, OpenPyxl
