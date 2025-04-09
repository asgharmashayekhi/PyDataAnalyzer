# PyDataAnalyzer

A powerful command-line tool for analyzing CSV data files and generating statistical reports and visualizations.

**Author:** Asghar Mashayekhi

## Features

- Read and analyze multiple CSV files
- Calculate statistical metrics (mean, median, max, min, sum, count) for numeric columns
- Filter data based on custom conditions
- Generate bar charts and scatter plots for data visualization
- Save analysis results to text files and filtered data to CSV files
- Handle errors gracefully with appropriate error messages
- Well-documented codebase with detailed comments

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/asgharmashayekhi/PyDataAnalyzer.git
   cd PyDataAnalyzer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

Analyze one or more CSV files:

```
python analyzer.py file1.csv file2.csv
```

### Command-line Arguments

- `files`: One or more CSV files to analyze (required)
- `-o, --output`: Output directory for results (default: "output")
- `-f, --filter`: Filter condition (e.g., "column > 100")
- `-p, --plot`: Column name to create a bar chart
- `-sx, --scatter-x`: X column for scatter plot
- `-sy, --scatter-y`: Y column for scatter plot

### Examples

1. Analyze a single CSV file:
   ```
   python analyzer.py data.csv
   ```

2. Analyze multiple files with a custom output directory:
   ```
   python analyzer.py data1.csv data2.csv -o results
   ```

3. Filter data and create visualizations:
   ```
   python analyzer.py data.csv -f "age > 30" -p age -sx income -sy expenses
   ```

## Output

The tool generates the following outputs in the specified directory:

1. Analysis report (TXT file) containing:
   - Statistical metrics for each numeric column
   - Information about filtered data
   - Information about generated plots

2. Filtered data (CSV files)

3. Visualizations:
   - Bar charts (PNG files)
   - Scatter plots (PNG files)

## Requirements

- Python 3.7+
- pandas
- numpy
- matplotlib


# For detailed documentation and usage instructions, check out the [docs folder](docs/):
- [Overview (English)](docs/overview-en.md) | [Overview (فارسی)](docs/overview-fa.md)
- [Usage (English)](docs/usage_en.md) | [Usage (فارسی)](docs/usage_fa.md)

## License

MIT 


## Developer Info

<p align="center">
  <img src="https://img.shields.io/badge/Developer-Asghar%20Mashayekhi-blue?style=for-the-badge" alt="Developer">
  <br>
  <a href="mailto:dallvllon@gmail.com">
    <img src="https://img.shields.io/badge/Email-dallvllon@gmail.com-orange?style=for-the-badge" alt="Email">
  </a>
  <br>
  <a href="https://github.com/asgharmashayekhi">
    <img src="https://img.shields.io/badge/GitHub-asgharmashayekhi-black?style=for-the-badge" alt="GitHub">
  </a>
</p>