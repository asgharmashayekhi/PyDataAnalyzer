#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyDataAnalyzer - A CSV data analysis tool
Author: Asghar Mashayekhi
"""

import argparse
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

class PyDataAnalyzer:
    """A class for analyzing CSV data files."""
    
    def __init__(self, files, output_dir="output", filter_condition=None, 
                 plot_column=None, scatter_x=None, scatter_y=None):
        """
        # Initialization function for class instance
        Args:
            files (list): List of CSV files to analyze
            output_dir (str): Output directory path for saving results
            filter_condition (str): Condition for filtering data
            plot_column (str): Column for bar chart
            scatter_x (str): X column for scatter plot
            scatter_y (str): Y column for scatter plot
        """
        self.files = files
        self.output_dir = output_dir
        self.filter_condition = filter_condition
        self.plot_column = plot_column
        self.scatter_x = scatter_x
        self.scatter_y = scatter_y
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Analysis results log
        self.analysis_log = []
        
    def analyze_file(self, file_path):
        """
        # Analyze a CSV file
        Args:
            file_path (str): Path to the file for analysis
        Returns:
            pandas.DataFrame: Filtered data
        """
        try:
            # Read CSV file
            self.analysis_log.append(f"\n{'='*50}")
            self.analysis_log.append(f"Analyzing file: {file_path}")
            self.analysis_log.append(f"{'='*50}")
            
            df = pd.read_csv(file_path)
            
            # Identify numeric columns
            numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
            self.analysis_log.append(f"Numeric columns: {', '.join(numeric_columns)}")
            
            if not numeric_columns:
                self.analysis_log.append("WARNING: No numeric columns found in the file.")
                return None
            
            # Calculate descriptive statistics for numeric columns
            self.analysis_log.append("\nStatistical Analysis:")
            for col in numeric_columns:
                self.analysis_log.append(f"\nColumn: {col}")
                
                try:
                    # Calculate main statistics
                    mean_val = df[col].mean()
                    median_val = df[col].median()
                    max_val = df[col].max()
                    min_val = df[col].min()
                    sum_val = df[col].sum()
                    count_val = df[col].count()
                    
                    # Add to report
                    self.analysis_log.append(f"  Mean: {mean_val:.4f}")
                    self.analysis_log.append(f"  Median: {median_val:.4f}")
                    self.analysis_log.append(f"  Max: {max_val:.4f}")
                    self.analysis_log.append(f"  Min: {min_val:.4f}")
                    self.analysis_log.append(f"  Sum: {sum_val:.4f}")
                    self.analysis_log.append(f"  Count: {count_val}")
                except Exception as e:
                    self.analysis_log.append(f"  Error analyzing column {col}: {str(e)}")
            
            # Filter data based on condition if specified
            filtered_df = df
            if self.filter_condition:
                try:
                    filtered_df = df.query(self.filter_condition)
                    self.analysis_log.append(f"\nFiltered data using condition: {self.filter_condition}")
                    self.analysis_log.append(f"Number of rows after filtering: {len(filtered_df)}")
                except Exception as e:
                    self.analysis_log.append(f"Error applying filter: {str(e)}")
            
            return filtered_df
            
        except Exception as e:
            self.analysis_log.append(f"ERROR: Failed to analyze file {file_path}: {str(e)}")
            return None
    
    def create_plots(self, df, file_name):
        """
        # Create plots for the data
        Args:
            df (pandas.DataFrame): DataFrame for plotting
            file_name (str): File name to use in plot file names
        """
        if df is None or df.empty:
            self.analysis_log.append("WARNING: Cannot create plots - No data available.")
            return
        
        base_file_name = os.path.basename(file_name).split('.')[0]
        
        # Create bar chart
        if self.plot_column:
            try:
                if self.plot_column in df.columns:
                    if pd.api.types.is_numeric_dtype(df[self.plot_column]):
                        plt.figure(figsize=(10, 6))
                        df[self.plot_column].value_counts().sort_index().plot(kind='bar')
                        plt.title(f'Bar Chart of {self.plot_column}')
                        plt.xlabel(self.plot_column)
                        plt.ylabel('Frequency')
                        
                        # Add extra space at the bottom for the creator information
                        plt.subplots_adjust(bottom=0.15)
                        
                        # Add creator's name with updated format
                        plt.figtext(0.5, 0.01, "Created by: PyDataAnalyzer \n Developer: Asghar Mashayekhi",
                                   ha="center", fontsize=9, color="grey")
                        
                        plt.tight_layout(rect=[0, 0.07, 1, 1])  # Adjust layout but leave space at bottom
                        bar_chart_path = os.path.join(self.output_dir, f"{base_file_name}_{self.plot_column}_bar.png")
                        plt.savefig(bar_chart_path)
                        plt.close()
                        self.analysis_log.append(f"\nBar chart saved to: {bar_chart_path}")
                    else:
                        self.analysis_log.append(f"WARNING: Column {self.plot_column} is not numeric. Cannot create bar chart.")
                else:
                    self.analysis_log.append(f"WARNING: Column {self.plot_column} not found for bar chart.")
            except Exception as e:
                self.analysis_log.append(f"ERROR: Failed to create bar chart: {str(e)}")
        
        # Create scatter plot
        if self.scatter_x and self.scatter_y:
            try:
                if self.scatter_x in df.columns and self.scatter_y in df.columns:
                    if (pd.api.types.is_numeric_dtype(df[self.scatter_x]) and 
                        pd.api.types.is_numeric_dtype(df[self.scatter_y])):
                        plt.figure(figsize=(10, 6))
                        plt.scatter(df[self.scatter_x], df[self.scatter_y], alpha=0.5)
                        plt.title(f'Scatter Plot: {self.scatter_y} vs {self.scatter_x}')
                        plt.xlabel(self.scatter_x)
                        plt.ylabel(self.scatter_y)
                        plt.grid(True, linestyle='--', alpha=0.7)
                        
                        # Add extra space at the bottom for the creator information
                        plt.subplots_adjust(bottom=0.15)
                        
                        # Add creator's name with updated format
                        plt.figtext(0.5, 0.01, "Created by: PyDataAnalyzer \n Developer: Asghar Mashayekhi",
                                   ha="center", fontsize=9, color="grey")
                        
                        plt.tight_layout(rect=[0, 0.07, 1, 1])  # Adjust layout but leave space at bottom
                        scatter_path = os.path.join(self.output_dir, 
                                                  f"{base_file_name}_{self.scatter_x}_{self.scatter_y}_scatter.png")
                        plt.savefig(scatter_path)
                        plt.close()
                        self.analysis_log.append(f"Scatter plot saved to: {scatter_path}")
                    else:
                        self.analysis_log.append(f"WARNING: Both {self.scatter_x} and {self.scatter_y} must be numeric for scatter plot.")
                else:
                    self.analysis_log.append(f"WARNING: Columns {self.scatter_x} and/or {self.scatter_y} not found for scatter plot.")
            except Exception as e:
                self.analysis_log.append(f"ERROR: Failed to create scatter plot: {str(e)}")
    
    def save_results(self, df, file_name):
        """
        # Save analysis results and filtered data
        Args:
            df (pandas.DataFrame): Filtered DataFrame
            file_name (str): Original file name
        """
        base_file_name = os.path.basename(file_name).split('.')[0]
        
        # Save filtered data to CSV file
        if df is not None and not df.empty:
            filtered_csv_path = os.path.join(self.output_dir, f"{base_file_name}_filtered.csv")
            df.to_csv(filtered_csv_path, index=False)
            self.analysis_log.append(f"\nFiltered data saved to: {filtered_csv_path}")
    
    def run_analysis(self):
        """
        # Run analysis for all input files
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        main_log_file = os.path.join(self.output_dir, f"analysis_report_{timestamp}.txt")
        
        for file_path in self.files:
            if not os.path.exists(file_path):
                self.analysis_log.append(f"ERROR: File not found: {file_path}")
                continue
                
            if not file_path.lower().endswith('.csv'):
                self.analysis_log.append(f"ERROR: File is not a CSV: {file_path}")
                continue
                
            # Analyze file
            filtered_df = self.analyze_file(file_path)
            
            # Create plots
            self.create_plots(filtered_df, file_path)
            
            # Save results
            self.save_results(filtered_df, file_path)
        
        # Save overall analysis report
        with open(main_log_file, 'w', encoding='utf-8') as f:
            f.write("PyDataAnalyzer - Analysis Report\n")
            f.write(f"Author: Asghar Mashayekhi\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write('\n'.join(self.analysis_log))
        
        print(f"Analysis completed. Report saved to {main_log_file}")
        

def main():
    """
    # Main program function
    """
    parser = argparse.ArgumentParser(description='PyDataAnalyzer - A CSV data analysis tool by Asghar Mashayekhi')
    
    parser.add_argument('files', nargs='+', help='CSV files to analyze')
    parser.add_argument('-o', '--output', default='output', help='Output directory for results')
    parser.add_argument('-f', '--filter', help='Filter condition (e.g., "column > 100")')
    parser.add_argument('-p', '--plot', help='Column to create a bar chart')
    parser.add_argument('-sx', '--scatter-x', help='X column for scatter plot')
    parser.add_argument('-sy', '--scatter-y', help='Y column for scatter plot')
    
    args = parser.parse_args()
    
    # Create instance of PyDataAnalyzer class and run analysis
    analyzer = PyDataAnalyzer(
        files=args.files,
        output_dir=args.output,
        filter_condition=args.filter,
        plot_column=args.plot,
        scatter_x=args.scatter_x,
        scatter_y=args.scatter_y
    )
    
    analyzer.run_analysis()

if __name__ == "__main__":
    main() 