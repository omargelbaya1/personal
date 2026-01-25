# Meta/Facebook has developed a new programing language called Hack.
# To measure the popularity of Hack they ran a survey with their employees.
# The survey included data on previous programing familiarity as well as the number of years of experience, age, gender and most importantly satisfaction with Hack. Due to an error location data was not collected, but your supervisor demands a report showing average popularity of Hack by office location. Luckily the user IDs of employees completing the surveys were stored.
# Based on the above, find the average popularity of the Hack per office location.
# Output the location along with the average popularity.

# Import your libraries
import pandas as pd

# Start writing code
facebook_employees.merge(facebook_hack_survey,left_on='id',
right_on='employee_id').groupby('location', as_index=False)['popularity'].mean()

#other variations

merged = pd.merge(facebook_employees,facebook_hack_survey, left_on = 'id', right_on = 'employee_id', how = 'inner')
result = merged.groupby(['location'])['popularity'].mean().reset_index()


#
df = pd.merge(facebook_employees,facebook_hack_survey, how='inner', left_on='id',right_on='employee_id')
df1 = df.groupby(['location'])['popularity'].mean().reset_index()

## Start writing code

joined_df = facebook_employees.set_index('id').join(facebook_hack_survey.set_index('employee_id'),
    lsuffix='l_')

pop = pd.pivot_table(joined_df,
                     index='location',
                     values='popularity',
                     aggfunc='mean').reset_index()
pop



