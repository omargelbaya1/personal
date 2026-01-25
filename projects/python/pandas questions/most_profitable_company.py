#Find the most profitable company from the financial sector. Output the result along with the continent.

import pandas as pd
import numpy as np

finance_sector = forbes_global_2010_2014[
    forbes_global_2010_2014["sector"] == "Financials"
]
finance_sector["rank"] = finance_sector["profits"].rank(
    method="min", ascending=False
)
result = finance_sector[finance_sector["rank"] == 1][["company", "continent"]]




#

# Import your libraries
import pandas as pd
import numpy as np
# Start writing code
# Import your libraries
import pandas as pd

# Start writing code
df = forbes_global_2010_2014

df = df[df['profits']==df['profits'].max()]

df[['company', 'continent']]



