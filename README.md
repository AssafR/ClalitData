# ClalitData
Merge the output of Clalit test results exported to CSV on the website

Usage:
ingest_clalit.py --dirname {dir} --outputfile {outputfile}

dir = Path containing a collection of Person*.csv files in Clalit download format
outputfile = CSV file containing the full database (will be created if does not exist).

