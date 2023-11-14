https://stackoverflow.com/questions/77479119/calculating-groupby-sum-of-values-on-column-based-on-string-in-pandas/77479422#77479422

The groupby and aggreate function can be used to calculate the counts for each group, in this example (EXPIRYDT, and TYPE). However, since the values need to be same in `sum column`. Row to Column need apply to the result.

Slightly different implementation from @Panda Kim, you answered so quickly!

    # calculate the sum by 'EXPIRYDT', 'TYPE'
    result = pd.DataFrame(result.agg(agg_dict).stack()).reset_index()
    print(result)
    # combined type and sum variable
    result['TYPE'] = result['TYPE'] + '_' + result['level_2']
    result = result.drop('level_2', axis=1)
    # row to column
    result = result.set_index(['EXPIRYDT','TYPE',]).unstack('TYPE')[0]
    join_key = 'EXPIRYDT'
    df = pd.merge(df, result, on = join_key)

output

[output result][1]


  [1]: https://i.stack.imgur.com/R0WXy.png