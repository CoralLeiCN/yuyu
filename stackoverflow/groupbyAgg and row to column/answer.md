https://stackoverflow.com/questions/77479119/calculating-groupby-sum-of-values-on-column-based-on-string-in-pandas/77479422#77479422

The groupby and aggreate function can be used to calculate the counts for each group, in this example (EXPIRYDT, and TYPE). However, since the values need to be same in `sum column`. Row to Column need apply to the result.

Slightly different implementation from @Panda Kim, you answered so quickly!
    
    result = df.groupby(["EXPIRYDT", "TYPE"])
    # calculate the sum by 'EXPIRYDT', 'TYPE'
    result = pd.DataFrame(result.agg(agg_dict).stack()).reset_index()

    # combined type and sum variable
    result['TYPE'] = result['TYPE'] + '_' + result['level_2']
    result = result.drop('level_2', axis=1)
    # row to column
    result = result.set_index(['EXPIRYDT','TYPE',]).unstack('TYPE')[0]
    join_key = 'EXPIRYDT'
    df = pd.merge(df, result, on = join_key)

output

      SYMBOL   EXPIRYDT  STRIKE TYPE  CONTRACTS  OPENINT TIMESTAMP  CE_CONTRACTS  \
    0   AAAA  26-Oct-23     480   CE          1     4000  4-Sep-23            33   
    1   AAAA  26-Oct-23     500   CE         31    25000  4-Sep-23            33   
    2   AAAA  26-Oct-23     525   CE          1     1000  4-Sep-23            33   
    3   AAAA  26-Oct-23     425   PE          0     1000  4-Sep-23            33   
    4   AAAA  26-Oct-23     450   PE         12    64000  4-Sep-23            33   
    5   AAAA  26-Oct-23     480   PE          2     2000  4-Sep-23            33   
    6   AAAA  26-Oct-23     500   PE          6     5000  4-Sep-23            33   
    
       CE_OPENINT  PE_CONTRACTS  PE_OPENINT  
    0       30000            20       72000  
    1       30000            20       72000  
    2       30000            20       72000  
    3       30000            20       72000  
    4       30000            20       72000  
    5       30000            20       72000  
    6       30000            20       72000  

