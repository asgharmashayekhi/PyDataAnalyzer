# PyDataAnalyzer Tutorial

**Author:** Asghar Mashayekhi  
**Version:** 1.0

## Table of Contents

1. [Introduction](#introduction)
2. [Project Files Overview](#project-files-overview)
3. [Installation Guide](#installation-guide)
4. [Basic Usage](#basic-usage)
5. [Command-Line Arguments](#command-line-arguments)
6. [Examples](#examples)
7. [Output Files Explained](#output-files-explained)
8. [Advanced Usage Scenarios](#advanced-usage-scenarios)
9. [Troubleshooting](#troubleshooting)
10. [Contributing](#contributing)

## Introduction

PyDataAnalyzer is a powerful command-line tool for analyzing CSV data files. It provides statistical analysis, data filtering, and visualization capabilities for CSV files containing numeric data. This tutorial will guide you through the setup and usage of PyDataAnalyzer, along with explanations of all the project components.

Key features of PyDataAnalyzer include:
- Reading and analyzing multiple CSV files at once
- Calculating statistical metrics for numeric columns (mean, median, max, min, sum, count)
- Filtering data based on custom conditions
- Generating visualizations (bar charts and scatter plots)
- Saving analysis results to text files and filtered data to CSV files
- Robust error handling with detailed error messages

## Project Files Overview

The PyDataAnalyzer project consists of the following files:

1. **analyzer.py**
   - This is the main Python script that contains the entire implementation of the PyDataAnalyzer tool.
   - Contains the PyDataAnalyzer class with methods for analyzing CSV files, creating plots, and saving results.
   - Includes the command-line interface implementation using argparse.
   - Purpose: Core functionality of the project.

2. **requirements.txt**
   - Lists the Python package dependencies required for the project.
   - Includes pandas, numpy, and matplotlib with specific versions.
   - Purpose: Makes it easy to install all required dependencies using pip.

3. **README.md**
   - Contains the project documentation in Markdown format.
   - Includes features, installation instructions, usage examples, and output descriptions.
   - Purpose: Provides a quick reference for users of the project.

4. **sample_data.csv**
   - A sample CSV file containing dummy personal data (id, name, age, income, expenses, satisfaction).
   - Purpose: Used for testing and demonstration purposes.

5. **sample_data2.csv**
   - A second sample CSV file with different structure (product data).
   - Purpose: Demonstrates the tool's ability to handle different types of data.

6. **example.bat / example.sh**
   - Script files for Windows (.bat) and Linux/macOS (.sh) that demonstrate basic usage scenarios.
   - Contains five different examples showcasing various features of PyDataAnalyzer.
   - Purpose: Makes it easy for users to quickly test the functionality.

7. **multi_file_example.bat / multi_file_example.sh**
   - Script files for Windows (.bat) and Linux/macOS (.sh) that demonstrate analyzing multiple files at once.
   - Purpose: Shows advanced usage scenarios with multiple file analysis.

8. **PyDataAnalyzer_Tutorial.md** (this file)
   - Comprehensive tutorial on how to use the project.
   - Contains detailed explanations of all project files and usage scenarios.
   - Purpose: Serves as a complete guide for users.

## Installation Guide

Follow these steps to set up PyDataAnalyzer on your system:

1. **Clone or download the repository:**
   
   If you have Git installed, you can clone the repository:
   ```
   git clone https://github.com/asgharmashayekhi/PyDataAnalyzer.git
   cd PyDataAnalyzer
   ```
   
   Alternatively, download and extract the ZIP file from the repository.

2. **Install Python:**
   
   Make sure you have Python 3.7 or newer installed on your system.
   You can check your Python version with:
   ```
   python --version
   ```

3. **Install the required dependencies:**
   
   ```
   pip install -r requirements.txt
   ```
   
   This will install:
   - pandas (version 2.0.3): For data manipulation and analysis
   - numpy (version 1.24.4): For numerical operations
   - matplotlib (version 3.7.3): For creating visualizations

4. **Test the installation:**
   
   Run a simple test to ensure everything is set up correctly:
   ```
   python analyzer.py sample_data.csv
   ```
   
   If successful, it will create an "output" directory with analysis results.

## Basic Usage

PyDataAnalyzer is run from the command line. The basic syntax is:

```
python analyzer.py [csv_file(s)] [options]
```

At minimum, you need to provide one or more CSV files to analyze.

Example:
```
python analyzer.py data.csv
```

This will:
1. Read data.csv
2. Calculate statistics for all numeric columns
3. Create an "output" directory (if it doesn't exist)
4. Save a report file in the output directory (analysis_report_YYYYMMDD_HHMMSS.txt)
5. Save the data to a filtered CSV file (data_filtered.csv)

Multiple files can be analyzed in a single command:
```
python analyzer.py file1.csv file2.csv file3.csv
```

Each file will be analyzed separately, with results saved to the same output directory.

## Command-Line Arguments

PyDataAnalyzer supports the following command-line arguments:

1. **Required Arguments:**
   - files: One or more CSV files to analyze (positional argument)
     
     Example: `python analyzer.py file1.csv file2.csv`

2. **Optional Arguments:**
   - `-o, --output`: Output directory for results (default: "output")
     
     Example: `python analyzer.py data.csv -o results`

   - `-f, --filter`: Filter condition using pandas query syntax
     
     Example: `python analyzer.py data.csv -f "age > 30 and income < 80000"`

   - `-p, --plot`: Column name to create a bar chart
     
     Example: `python analyzer.py data.csv -p age`

   - `-sx, --scatter-x`: X column for scatter plot
     
     Example: `python analyzer.py data.csv -sx age -sy income`

   - `-sy, --scatter-y`: Y column for scatter plot (must be used with -sx)
     
     Example: `python analyzer.py data.csv -sx age -sy income`

   - `-h, --help`: Show the help message and exit
     
     Example: `python analyzer.py --help`

## Examples

Here are several example commands that demonstrate the capabilities of PyDataAnalyzer:

### Example 1: Basic Analysis
```
python analyzer.py sample_data.csv
```
- Analyzes all numeric columns in sample_data.csv
- Creates statistical reports for each column
- Saves results to the "output" directory

### Example 2: Filtering Data
```
python analyzer.py sample_data.csv -f "age > 35"
```
- Analyzes all numeric columns in sample_data.csv
- Filters to include only rows where age > 35
- Saves filtered data and analysis results

### Example 3: Creating a Bar Chart
```
python analyzer.py sample_data.csv -p age
```
- Analyzes all numeric columns in sample_data.csv
- Creates a bar chart showing the distribution of the "age" column
- Saves the chart as a PNG file in the output directory

### Example 4: Creating a Scatter Plot
```
python analyzer.py sample_data.csv -sx income -sy expenses
```
- Analyzes all numeric columns in sample_data.csv
- Creates a scatter plot with "income" on the x-axis and "expenses" on the y-axis
- Saves the plot as a PNG file in the output directory

### Example 5: Combined Features
```
python analyzer.py sample_data.csv -o results -f "income > 70000" -p satisfaction -sx age -sy income
```
- Analyzes all numeric columns in sample_data.csv
- Filters to include only rows where income > 70000
- Creates a bar chart of the "satisfaction" column
- Creates a scatter plot of "age" vs "income"
- Saves all results to the "results" directory

### Example 6: Multiple Files
```
python analyzer.py sample_data.csv sample_data2.csv -o multi_analysis
```
- Analyzes both sample_data.csv and sample_data2.csv
- Creates separate statistical reports for each file
- Saves all results to the "multi_analysis" directory

## Output Files Explained

PyDataAnalyzer generates several output files:

1. **Analysis Report (TXT)**
   - Filename: analysis_report_YYYYMMDD_HHMMSS.txt
   - Contains:
     * The date and time of analysis
     * Author information
     * List of numeric columns detected in each file
     * Statistical metrics for each numeric column (mean, median, max, min, sum, count)
     * Information about any filtering applied
     * Paths to any generated visualizations

2. **Filtered Data Files (CSV)**
   - Filename: [original_filename]_filtered.csv
   - Contains the data after any filters have been applied
   - If no filter is applied, this file will be identical to the input file

3. **Bar Chart Visualizations (PNG)**
   - Filename: bar_chart_[column_name]_YYYYMMDD_HHMMSS.png
   - Shows the distribution of values in the specified column
   - Created when the -p/--plot option is used

4. **Scatter Plot Visualizations (PNG)**
   - Filename: scatter_plot_[x_column]_vs_[y_column]_YYYYMMDD_HHMMSS.png
   - Shows the relationship between two numeric columns
   - Created when both -sx/--scatter-x and -sy/--scatter-y options are used

## Advanced Usage Scenarios

### Scenario 1: Data Filtering with Multiple Conditions
```
python analyzer.py sample_data.csv -f "age > 30 and income > 50000 and expenses < 30000"
```
This command filters the data based on multiple conditions combined with logical operators.

### Scenario 2: Multiple Files with Different Options
```
python analyzer.py sample_data.csv -p age -o age_analysis
python analyzer.py sample_data.csv -sx income -sy expenses -o income_expenses_analysis
```
These commands analyze the same file in different ways, saving results to separate output directories.

### Scenario 3: Batch Processing
You can create a batch file or shell script to process multiple files with different options:

```bash
# Windows batch file example (process_all.bat)
python analyzer.py data1.csv -o results/data1
python analyzer.py data2.csv -o results/data2
python analyzer.py data3.csv -p age -o results/data3_age_analysis
```

### Scenario 4: Using as a Module in Other Python Scripts
You can also import the PyDataAnalyzer class in your own Python scripts:

```python
from analyzer import PyDataAnalyzer

# Create analyzer instance
analyzer = PyDataAnalyzer()

# Analyze a file
analyzer.analyze_file('data.csv')

# Get the analyzed data
data = analyzer.data

# Apply custom transformations or analysis
# ...

# Save results
analyzer.save_results('custom_output')
```

## Troubleshooting

### Common Issues and Solutions

1. **Missing Dependencies**
   - Issue: Import errors when running the script
   - Solution: Make sure you've installed all dependencies with `pip install -r requirements.txt`

2. **File Not Found Errors**
   - Issue: The script can't locate the CSV file
   - Solution: Check the file path and make sure the file exists in the specified location

3. **Invalid CSV Format**
   - Issue: The script reports errors reading the CSV file
   - Solution: Verify that your CSV file has a header row and is correctly formatted

4. **Column Not Found for Plotting**
   - Issue: The script can't find the column specified for plotting
   - Solution: Check that the column name matches exactly (case-sensitive) with the header in your CSV file

5. **Invalid Filter Syntax**
   - Issue: The filter condition causes an error
   - Solution: Make sure your filter follows pandas query syntax and references columns that exist in your data

### Getting Help

If you encounter any issues not covered in this section, please:
1. Check the GitHub repository for known issues
2. Submit a new issue with a detailed description of your problem
3. Include any error messages and the exact command you were trying to run

## Contributing

Contributions to PyDataAnalyzer are welcome! Here's how you can contribute:

1. **Fork the repository**
   - Create your own fork of the project on GitHub

2. **Create a feature branch**
   - Make your changes in a new branch: `git checkout -b feature/your-feature-name`

3. **Commit your changes**
   - Write clear, concise commit messages describing your changes

4. **Push to your branch**
   - Push your changes to your fork: `git push origin feature/your-feature-name`

5. **Create a Pull Request**
   - Submit a pull request to the main repository

### Development Guidelines

- Follow PEP 8 style guidelines for Python code
- Add docstrings for all functions and classes
- Include unit tests for new features
- Update documentation to reflect any changes

Thank you for using PyDataAnalyzer! 