sp-convert-csv
==============

A Python script that will import one CSV file, process, and export another CSV file.

I am not a programmer, and I am just trying to help out a friend with his ecommerce site.

A composer submits their music score by filling out a form. The submission form records are stored in submission.csv. 

Before adding a new record to the ecommerce CMS, we need to convert this submission into the CMS's database format, which looks like converted.csv.

I got started by creating a script that would process one line of the submission.csv. I taught myself (poorly) how to use Python's CSV module in order to do this. 

Right now, I'm just trying to get the program to iterate over each line of submission.csv and write multiple new rows in converted.csv.
