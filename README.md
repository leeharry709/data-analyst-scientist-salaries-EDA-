# data-analyst-scientist-salaries-EDA-
Exploratory data analysis on glassdoor data of data analyst and data science jobs across the nation

This was an exploratory data analysis of data analyst and data science jobs datasets from kaggle.com by user Larxel. The user scraped data from glassdoor for the job queries "data analyst" and "data scientist" and posted them as csv files. Using these csv files, I began my cleaning.

# Data Cleaning
Cleaning the data took a repition of lambda functions to keep the code cleaner. The main goals of cleaning were to:
- Parse average salary data from the range
- Convert hourly range to salary data
- Remove rating from company name
- Split the location into state and city
- Calculate the age of the company from the its founded date
- Calculate length of the job description
- Check if specific skills were found in the job description such as python, r studio, and aws.
- Simplify job title to core job such as data analyst, data scientist, and machine learning engineer.
After the file was cleaned, the program output the data into a new csv file.

# Exploratory Data Analysis (EDA)
The main goal was to see how the different data elements correlated with key variables such as average salary by location or by simplified job title. Below are highlights of the exploration.

# Future Goals
I hope to turn this into a prediction model so that it can incorporate user inputted location, job title, etc. and return an estimated salary and potential skills required. I believe that this could be a useful model to show pay-for-skill and pay equity by location.
