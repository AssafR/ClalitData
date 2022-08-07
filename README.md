# ClalitData
Merge the output of Clalit test results exported to CSV on the website

## Motivation:
Tests results on the Clalit website can be exported "to Excel" (actually CSV).

However, there are several issues:
* Each test report is saved separately
* The file names are meaningless - the filename is always called PersonList.csv and if there are already files in the directory they will be automatically renamed to PersonList (39).csv, etc. 
* The results are only saved for about 2 years backwards, so to save your history you need to store it yourself

## What this program does:
Given a directory of (possibly duplicate) files, merge all the data in them into one 'database' (stored as a CSV file), sorted by test name and date.  
All duplicates are merged, so no need to worry if you downloaded the same file more than once.


## Usage:
> ingest_clalit.py --dirname {dir} --outputfile {outputfile}

***dir*** = Path containing a collection of Person*.csv files in Clalit download format  
***outputfile*** = CSV file containing the full database (will be created if does not exist).

