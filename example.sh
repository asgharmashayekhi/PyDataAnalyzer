#!/bin/bash

echo "PyDataAnalyzer Examples by Asghar Mashayekhi"
echo "==========================================="
echo

echo "Example 1: Basic analysis of sample data"
python analyzer.py sample_data.csv
echo
echo "Example 1 completed. Check the 'output' directory for results."
echo
read -p "Press Enter to continue..."

echo "Example 2: Filtering data where age > 35"
python analyzer.py sample_data.csv -f "age > 35"
echo
echo "Example 2 completed. Check the 'output' directory for results."
echo
read -p "Press Enter to continue..."

echo "Example 3: Creating a bar chart of 'age' column"
python analyzer.py sample_data.csv -p age
echo
echo "Example 3 completed. Check the 'output' directory for results."
echo
read -p "Press Enter to continue..."

echo "Example 4: Creating a scatter plot of 'income' vs 'expenses'"
python analyzer.py sample_data.csv -sx income -sy expenses
echo
echo "Example 4 completed. Check the 'output' directory for results."
echo
read -p "Press Enter to continue..."

echo "Example 5: Complete analysis with filtering and visualization"
python analyzer.py sample_data.csv -o complete_analysis -f "income > 70000" -p satisfaction -sx age -sy income
echo
echo "Example 5 completed. Check the 'complete_analysis' directory for results."
echo
read -p "Press Enter to continue..."

echo "All examples completed." 