# Find all Lyft drivers who earn either equal to or less than 30k USD or equal to or more than 70k USD.
# Output all details related to retrieved records.

#my solution:

# Import your libraries
import pandas as pd

# Start writing code


df=lyft_drivers

df[(df['yearly_salary'] > 70000) | (df['yearly_salary'] < 30000)]

#or:

# Import your libraries
import pandas as pd

# Start writing code
lyft_drivers[~lyft_drivers.yearly_salary.between(30000, 70000)]



# Import your libraries
import pandas as pd

# Start writing code
lyft_drivers.query("yearly_salary <= 30000 or yearly_salary >= 70000")