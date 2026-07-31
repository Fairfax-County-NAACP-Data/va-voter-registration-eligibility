import pandas as pd
import re
import streamlit as st

def get_search_terms(df):
    words = set()
    for colname in ['Name', 'Description']:
        col = df[colname].tolist()
        for c in col:
            words.update([x.lower() for x in re.split(r'\s|/', c.replace(',','').replace('.','').replace(')','').replace('(',''))])

    words-=set(['or','the','of','etc','thereto','do','to','and','an','a','as','in','ina','where','such','act','more','by','than','those',
                'was','from','with','on','when','not','vic','any'])
    not_allowed = ['>','=','<','&']
    words = set(x for x in words if len(x)>1 and not re.search(r'\d', x) and not any(y in x for y in not_allowed) and "'" not in x)
    words = [x[1:] if x[0]=='-' else x for x in words]
    words = list(words)
    words.sort()

    return words

@st.cache_data()
def get_table():
    df = pd.read_csv('VA_Elections_Felony_Eligibility_Table.csv')
    row1 = pd.DataFrame({'Can I Register to Vote?':['YES'], 'Statute':['ALL OTHERS'],'Name':['ALL OTHERS'],'Description':['']})
    df = pd.concat([row1, df])

    return df

    
st.info("The below tool can help you determine if the "+
        "[Virginia Department of Elections"
        " has declared that you are eligible to vote](https://www.elections.virginia.gov/registration/felony-convictions-and-voter-eligibility/).")
st.subheader("You are eligible to vote in Virginia if you meet the [basic criteria]"+
        "(https://www.elections.virginia.gov/registration/how-to-register/https://www.elections.virginia.gov/registration/how-to-register/) "+
        "(over 18, U.S. citizen, resident of VA, etc.) AND:\n\n")
st.markdown(
        '1. The felony(s) that you are convicted of is **NOT** in the below list **OR**\n'+
        '2. The felony(s) that you are convicted of is labeled "**YES with Additional Evaluation**" below\n\n'+
        'If your felony conviction requires additional evaluation or it was not a Virginia state conviction, your local general registrar will' +
        'send you a supplemental form for more information after you submit a voter registration application.'
        )

df = get_table().sort_values(by='Can I Register to Vote?', ascending=False)

col1, col2 = st.columns(2)

if 'statute' in st.session_state and len(st.session_state['statute'])>0:
    df = df[df['Statute'].isin(st.session_state['statute'])]

if 'search' in st.session_state and len(st.session_state['search'])>0:
    for s in st.session_state['search']:
        df = df[df['Name'].str.lower().str.contains(s) | df['Description'].str.lower().str.contains(s)]

st.markdown(f'**{len(df)} Results of Search** (*hover over table to show scrollbar*)')
st.dataframe(df, hide_index=True,
             column_config={
                 'Can I Register to Vote?':st.column_config.TextColumn(width='medium')
             })

with col1:
    statutes = st.multiselect('Statute', set(df['Statute'].tolist()), default=None,
                              placeholder='Enter statute number',
                              max_selections=10,
                              key='statute')

with col2:
    words = get_search_terms(df)
    search_terms = st.multiselect('Key Words', words, default=None,
                                  placeholder='Enter search term(s)',
                                  max_selections=10,
                                  key='search')
    
st.header("If you do NOT see your conviction(s) in this table OR your convictions are labeled 'YES with Additional Evaluation', "+
            "[register to VOTE here!](https://www.elections.virginia.gov/registration/how-to-register/)")
    
st.markdown("Based on *What are the applicable common law felonies?* PDFs from the "+
            "[Felony Convictions and Voter Eligibility](https://www.elections.virginia.gov/registration/felony-convictions-and-voter-eligibility/) "+
            'site of the Virginia Department of Elections.')

# TODO: Add mobile mode