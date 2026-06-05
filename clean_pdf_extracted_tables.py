import glob
import os
import pandas as pd
import re

misspellings = {'withany':'with any',
                'murdercommitted':'murder committed',
                'Statue':'Statute',
                'drugenterprise':'drug enterprise',
                'catalyticconverter':'catalytic converter',
                'ordistribute':'or distribute',
                'orboat':'or boat',
                'ticketvalued':'ticket valued',
                'torape':'to rape',
                'forhire':'for hire',
                'inwork':'in work',
                'law-enforcement':'law enforcement',
                'Grany':'Grand',
                '–':'-'}

# Tables extracted from https://www.elections.virginia.gov/media/electionadministration/electionlaw/Virginia-Crimes-Applicable-to-Common-Law-Felonies-in-1870.pdf
folders = ['Virginia-Crimes-Applicable-to-Common-Law-Felonies-in-1870_tables','Virginia-Crimes-Requiring-Additional-Evaluation_tables']
labels = ['NO', 'YES with Additional Evaluation']
dfs = []
for folder, label in zip(folders, labels):
    table = {'num':[], 'Statute':[], 'Name':[],'Description':[]}
    keys = list(table.keys())
    files = glob.glob(os.path.join(folder,'*.xlsx'))
    rows_found = False
    for f in files:
        df = pd.read_excel(f)
        for k in range(len(df)):
            if not rows_found:
                try:
                    float(df.iloc[k,0]) # First row contains a number
                except:
                    continue
            rows_found = True
            if pd.notnull(df.iloc[k,0]):
                table['num'].append(df.iloc[k,0])
                for j in range(1,4):
                    table[keys[j]].append(df.iloc[k,j] if pd.notnull(df.iloc[k,j]) else "")
            else:
                for j in range(1,4):
                    table[keys[j]][-1] += " "+df.iloc[k,j] if pd.notnull(df.iloc[k,j]) else ""

    def clean(x: str):
        x = x.strip()
        for k,v in misspellings.items():
            x = x.replace(k,v)
            
        x = re.sub(r'([^\s])([><\$])', r'\1 \2', x) # Ensure space before <, >, $
        x = re.sub(r',([^\s])',r', \1', x)
        x = re.sub(r'\)([^\s])',r') \1', x)
        x = re.sub(r'([^\s])\(',r'\1 (', x)
        x = re.sub(r'(\d)([A-Za-z])',r'\1 \2', x)
        x = re.sub(r'\s\-([A-Za-z])', r' - \1', x)
        x = re.sub(r"'s([^\s])",r"'s \1", x)
        

        always_alone = ['of', 'subsequent', 'aggravated', 'commission', 'facilitate','planting','killing','offense', 'officer',
                        'involuntary','manslaughter','culpable','accommodation','communications','enforcement', r'etc.',
                        'another']
        for w in always_alone:
            x = re.sub(rf'([^\s]){w}',rf'\1 {w}', x)  
            x = re.sub(rf'\s{w}([^\sf])',rf' {w} \1', x)  

        x = re.sub(r'\s+',' ', x)

        return x

    for k,v in table.items():
        if k not in ['Statute']:
            table[k] = [clean(x) if isinstance(x,str) else x for x in v]

    df = pd.DataFrame(table)
    assert df['num'].notnull().all()
    df['num'] = df['num'].apply(lambda x: int(float(x)))
    df = df.sort_values(by='num')

    df['Can I Register to Vote?'] = label

    dfs.append(df[['Can I Register to Vote?', 'Statute','Name','Description']])

df = pd.concat(dfs, ignore_index=True)
df.sort_values('Statute')

df.to_csv('VA_Elections_Felony_Eligibility_Table.csv', index=False)