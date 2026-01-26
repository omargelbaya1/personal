# Import your libraries
import pandas as pd

# Start writing code
los_angeles_restaurant_health_inspections
df = los_angeles_restaurant_health_inspections
# Start writing code
df[(df['facility_name'] == 'STREET CHURROS') & (df['score'] < 95)][['activity_date', 'pe_description']]


#other ways of doing it:

# Import your libraries
import pandas as pd

# Start writing code
los_angeles_restaurant_health_inspections[(los_angeles_restaurant_health_inspections['facility_name'] == 'STREET CHURROS') & (los_angeles_restaurant_health_inspections['score'] < 95)][['activity_date', 'pe_description']]



# Import your libraries
import pandas as pd

# Start writing code
los_angeles_restaurant_health_inspections.activity_date=los_angeles_restaurant_health_inspections.activity_date.dt.date
los_angeles_restaurant_health_inspections.query("facility_name == 'STREET CHURROS' and score < 95")[['activity_date','pe_description']]