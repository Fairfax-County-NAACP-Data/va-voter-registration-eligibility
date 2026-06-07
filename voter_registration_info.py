import re
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="VA Voter Eligibility",
    page_icon=':material/how_to_vote:',  #"☑️",
    initial_sidebar_state="auto",
    layout = 'wide',
    menu_items={
        'Report a Bug': "mailto:openpolicedata@gmail.com"
    }
)

def get_search_terms(df):
    words = set()
    for colname in ['Name', 'Description']:
        col = df[colname].tolist()
        for c in col:
            words.update([x.lower() for x in re.split(r'\s|/', c.replace(',','').replace('.','').replace(')','').replace('(',''))])

    words-=set(['or','the','of','etc','thereto','do','to','and'])
    not_allowed = ['>','=','<','&']
    words = set(x for x in words if len(x)>1 and not re.search(r'\d', x) and not any(y in x for y in not_allowed) and "'" not in x)
    words = list(words)
    words.sort()

    return words

@st.cache_data()
def get_table():
    df = pd.read_csv('VA_Elections_Felony_Eligibility_Table.csv')
    row1 = pd.DataFrame({'Can I Register to Vote?':['YES'], 'Statute':['ALL OTHERS'],'Name':['ALL OTHERS'],'Description':['']})
    df = pd.concat([row1, df])

    return df

with st.sidebar:
    st.header("Are you a VA resident and convicted of a felony? Based on a recent court ruling, you may now be eligible to vote!")
    st.subheader("**[In January, a federal judge ordered widespread voting rights restoration for Virginians convicted of a felony](https://www.vpm.org/news/2026-01-29/federal-judge-va-voting-rights-king-johnson-gibney-aclu-readmission-act-1870)**")
    st.markdown("- Voting rights can ONLY be taken away for certain felonies that were common law in 1870\n"+
                "- Virginia can no longer take away the right to vote for drug crimes and MANY other felonies\n"+
                "- If you were not convicted of one of these crimes and are 18 or older, you may register to vote\n"+
                "- No need to apply for restoration of rights from the Governor ")
    
    st.warning("**DON'T FORGET!: If the "+\
               "[Voting Rights Restoration Constitutional Amendment](https://fairelectionscenter.org/advocacy/virginia-voting-rights-restoration/) "+
               "passes this November, the right to vote will be restored to ALL Virginians who have been convicted of a felony (except when they are incarcerated "
               "for that felony).\n\nIf you cannot register now, you will be able to if and when the amendment passes.")
    
st.info("The below tool can help you determine if the "+
        "[Virginia Department of Elections](https://www.elections.virginia.gov/registration/felony-convictions-and-voter-eligibility/)"
        " has declared that you are eligible to vote.\n\n"+
        "**You are eligible to vote if:**\n\n"+
        '1. The felony(s) that you are convicted of is **NOT** in the below list **OR**\n'+
        '2. The felony(s) that you are convicted of is labeled "**YES with Additional Evaluation**" below\n\n'+
        'If your felony conviction requires additional evaluation or it was not a Virginia state conviction, your local general registrar will send you a supplemental form for more information after you submit a voter registration application.'
        )

st.header("[Register to VOTE Here!](https://www.elections.virginia.gov/registration/how-to-register/)")

df = get_table()

col1, col2 = st.columns(2)

if 'statute' in st.session_state and len(st.session_state['statute'])>0:
    df = df[df['Statute'].isin(st.session_state['statute'])]

if 'search' in st.session_state and len(st.session_state['search'])>0:
    for s in st.session_state['search']:
        df = df[df['Name'].str.lower().str.contains(s) | df['Description'].str.lower().str.contains(s)]

st.markdown(f'**{len(df)} Results of Search**')
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
    
st.markdown("Based on *What are the applicable common law felonies?* PDFs from the "+
            "[Felony Convictions and Voter Eligibility](https://www.elections.virginia.gov/registration/felony-convictions-and-voter-eligibility/) "+
            'site of the Virginia Department of Elections.')

st.markdown("Please [email](mailto:openpolicedata@gmail.com) if there are any issues with this site or questions about voting.")

# TODO: Add mobile mode
# TODO: Say something about Fairfax NAACP?