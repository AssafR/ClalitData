# ClalitData
Merge the output of **Clalit Health** test results exported to CSV on the website

## Motivation:
Tests results on the Clalit website can be exported "to Excel" (actually CSV).

However, there are several issues:
* Each test report is saved separately
* The file names are meaningless - the filename is always called *PersonList.csv* and if there are already files in the directory they will be automatically renamed to *PersonList (39).csv*, etc. 
* The results are only downloadable for about 2 years backwards, so to save your history you need to store it yourself

## What this program does:
Given a directory of (possibly duplicate) files named *PersonList\*.csv*, merge all the data in them into one 'database' (stored as a CSV file), sorted by test name and date.
If the database exists, all new data will be merged into it. If it doesn't, it will be created.

All duplicates are merged, so no need to worry if you downloaded the same file more than once.
It preserves the original fields of data, test number, test name, results, min/max values.

## Usage:
> ingest_clalit.py --dirname {dir} --outputfile {outputfile}

***dir*** = Path containing a collection of *Person\*.csv* files in Clalit download format  
***outputfile*** = CSV file containing the current full database (will be created if does not exist).

