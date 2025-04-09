@echo off
echo PyDataAnalyzer Multi-File Example by Asghar Mashayekhi
echo ===================================================
echo.

echo Analyzing multiple CSV files with different structures
python analyzer.py sample_data.csv sample_data2.csv -o multi_file_analysis
echo.
echo Analysis completed. Check the 'multi_file_analysis' directory for results.
echo.
pause

echo Filtering and creating visualizations for multiple files
python analyzer.py sample_data.csv sample_data2.csv -o multi_file_viz -f "age > 30 or price > 100" -p satisfaction -sx income -sy expenses
echo.
echo Analysis with visualization completed. Check the 'multi_file_viz' directory for results.
echo.
pause

echo All examples completed. 