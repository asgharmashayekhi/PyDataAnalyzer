# PyDataAnalyzer Commands

**Author:** Asghar Mashayekhi

This file contains all the available commands and usage examples for the PyDataAnalyzer tool.

## Basic Syntax

```
python analyzer.py [csv_files] [options]
```

## Required Arguments

| Argument | Description |
|----------|-------------|
| csv_files | One or more CSV files to analyze (at least one is required) |

## Optional Arguments

| Argument | Description |
|----------|-------------|
| -o, --output | Specify output directory for results (default: "output") |
| -f, --filter | Apply filter condition using pandas query syntax |
| -p, --plot | Create a bar chart for the specified column |
| -sx, --scatter-x | X-axis column for scatter plot (must be used with -sy) |
| -sy, --scatter-y | Y-axis column for scatter plot (must be used with -sx) |
| -h, --help | Display help message and exit |

## Command Examples

### 1. Basic Analysis - single file

```
python analyzer.py sample_data.csv
```

This command analyzes sample_data.csv, calculating statistics for all numeric columns and saving results to the default "output" directory.

### 2. Basic Analysis - multiple files

```
python analyzer.py sample_data.csv sample_data2.csv
```

This command analyzes both files separately, saving results to the default "output" directory.

### 3. Specify Output Directory

```
python analyzer.py sample_data.csv -o my_results
```

This command analyzes sample_data.csv and saves results to the "my_results" directory.

### 4. Apply Filter

```
python analyzer.py sample_data.csv -f "age > 35"
```

This command analyzes sample_data.csv, filters rows where age > 35, and saves results.

### 5. More Complex Filter

```
python analyzer.py sample_data.csv -f "age > 30 and income < 80000"
```

This command applies a more complex filter condition with multiple criteria.

### 6. Create Bar Chart

```
python analyzer.py sample_data.csv -p age
```

This command analyzes sample_data.csv and creates a bar chart for the "age" column.

### 7. Create Scatter Plot

```
python analyzer.py sample_data.csv -sx income -sy expenses
```

This command analyzes sample_data.csv and creates a scatter plot with "income" on the x-axis and "expenses" on the y-axis.

### 8. Multiple Options Combined

```
python analyzer.py sample_data.csv -o results -f "income > 70000" -p satisfaction -sx age -sy income
```

This command combines multiple options: custom output directory, filtering, bar chart, and scatter plot creation.

### 9. Multiple Files with Options

```
python analyzer.py sample_data.csv sample_data2.csv -o multi_analysis -f "age > 30 or price > 100"
```

This command analyzes multiple files with filtering and custom output directory.

### 10. Get Help

```
python analyzer.py --help
```

This command displays the help message with information about all available options.

## Notes

- Filter conditions follow pandas query syntax
- Both -sx and -sy must be provided to create a scatter plot
- File paths can be relative or absolute
- Multiple CSV files can be analyzed in a single command 