import pandas as pd
import os

os.chdir('C:/Users/leeha/Documents/pythons/data salary')
df = pd.read_csv('DataAnalystScientistFULL.csv')

# To confirm the file loaded properly
print(df.head(5)) 

# Cleaning salary information
df = df[df['Salary Estimate'] != '-1']
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
remove_K_dollar = salary.apply(lambda x: x.replace('K', '').replace('$', ''))

minus_hourly = remove_K_dollar.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:', ''))

df['min_salary'] = minus_hourly.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_hourly.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

# Convert hourly to salary
df['min_salary'] = df.apply(lambda x: x.min_salary*2 if x.hourly == 1 else x.min_salary, axis=1)
df['max_salary'] = df.apply(lambda x: x.max_salary*2 if x.hourly == 1 else x.max_salary, axis=1)

# Cleaning company name
df['company_name'] = df.apply(lambda x: str(x['Company Name']).replace('\n', '') if x['Rating'] == -1 else str(x['Company Name'][:-3]).replace('\n', ''), axis = 1)

# Clean Location
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1] if x.count(',') == 1 else x.split(',')[2])
df['job_city'] = df['Location'].apply(lambda x: x.split(',')[0])

# Age of company
df['age of company'] = df['Founded'].apply(lambda x: x if x == -1 else 2021 - x)

# Length of Description
df['desc_len'] = df['Job Description'].apply(lambda x: len(x))

# - python
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
# - r studio
df['r studio'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
# - cloud
df['cloud'] = df['Job Description'].apply(lambda x: 1 if 'cloud' in x.lower() else 0)
# - SQL
df['SQL'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
# - AWS
df['AWS'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

df_out = df.drop(['Index'], axis = 1)

df_out.to_csv('DataAnalystScientistFULL_cleaned.csv', index=False)