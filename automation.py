import pandas as pd

file_loc = r"C:\Users\ArjunSuresh\Downloads\data.xlsx"

df = pd.read_excel(file_loc, sheet_name='Sheet1')

#print(df.loc[df['Segment']=='Government'])
        
for c in df['Segment']:
    if (c == 'Government'):
        df.loc[df['Segment']=='Government'].to_excel('Government.xlsx', sheet_name='Data')
    elif (c == 'Small Business'):
        df.loc[df['Segment']=='Small Business'].to_excel('Small Business.xlsx', sheet_name='Data')
    elif (c == 'Enterprise'):
        df.loc[df['Segment']=='Enterprise'].to_excel('Enterprise.xlsx', sheet_name='Data')