# ClalitData
Python script to merge the output of many seperate **Clalit Health Services** test results which the user has exported to CSV on the website, into one easy sorted CSV file.

## Motivation:
In the *Clalit* website test-results view, it provides a button to export the results "to Excel" (actually CSV).

However, there are several issues:
* Each test report is saved separately
* The file names are meaningless - the filename is always called *PersonList.csv* and if there are already files in the download directory, they will be automatically renamed to *PersonList (39).csv*, etc. 
* The results are only viewable/downloadable for about 2 years backwards, so to save your history you need to store it yourself

## What this program does:
Given a directory of (possibly duplicate) files named *PersonList\*.csv* in the *Clalit* output format, merge all the data in them into one 'database' (stored as a CSV file), sorted by test name and date.
If the database already exists, all new data will be merged into it. If it doesn't, it will be created.

All duplicates are merged, so no need to worry if you downloaded the same file more than once.
It preserves the original fields of data, test number, test name, results, min/max values.

## Requirements:
* Basic understanding of running a script from the command line.
* Python language installed.
* Installed libraries: datetime, click, pathlib, pandas 

## Usage:
> ingest_clalit.py --dirname {dir} --outputfile {outputfile}

***dir*** = Path containing a collection of *Person\*.csv* files in Clalit download format  
***outputfile*** = CSV file containing the current full database (will be created if does not exist).

