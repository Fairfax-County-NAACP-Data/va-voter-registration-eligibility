import pandas as pd
import streamlit as st
import datetime
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title="VA Voter Registration Guide",
    page_icon=':material/how_to_vote:',  #"☑️",
    initial_sidebar_state="auto",
    layout = 'wide',
    menu_items={
        'Report a Bug': "mailto:voting_guide@pm.me"
    }
)

if 'v' in st.query_params:
    st.cache_data.clear()
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
    new_row = pd.DataFrame({'Date':[pd.Timestamp.now(datetime.timezone.utc)], 'Version':[st.query_params["v"]]})
    df = pd.concat([df, new_row]) if len(df)>0 else new_row
    conn.update(data=df)


if pd.Timestamp.now() < pd.Timestamp('2026-09-05 13:00:00'):
    st.error('Learn more and get help registering to vote with **Fairfax County NAACP at Sherwood Library on September 5 from 10 AM to 1 PM**.'
             f' Sign up [here]({st.secrets["signup"]}) to join us!')

pg = st.navigation([st.Page("1_intro.py", title='FAQ'), st.Page('2_eligibility.py', title='Eligibility')], position='top')
pg.run()

st.info('This site contains information published by the [Virginia Department of Elections](https://www.elections.virginia.gov/registration/) except for the '+
        "guidance for how to fill out the felony questions on the voter registration form, which was provide by the "
        "[Fairfax County Registrar's Office](https://www.fairfaxcounty.gov/elections/registration).\n\n"
        'For questions about voter registration, please contact the [Fairfax County Registrar](https://www.fairfaxcounty.gov/elections/registration). \n\n'+
        'For questions/comments/issues about this site, please email [us](mailto:voting_guide@pm.me).')