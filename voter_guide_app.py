import streamlit as st

st.set_page_config(
    page_title="VA Voter Registration Guide",
    page_icon=':material/how_to_vote:',  #"☑️",
    initial_sidebar_state="auto",
    layout = 'wide',
    menu_items={
        'Report a Bug': "mailto:voting_guide@pm.me"
    }
)

pg = st.navigation([st.Page("1_intro.py", title='FAQ'), st.Page('2_eligibility.py', title='Eligibility')], position='top')
pg.run()

st.info('This site contains information published by the [Virginia Department of Elections](https://www.elections.virginia.gov/registration/) except for the '+
        "guidance for how to fill out the felony questions on the voter registration form, which was provide by the "
        "[Fairfax County Registrar's Office](https://www.fairfaxcounty.gov/elections/registration).\n\n"
        'For questions about voter registration, please contact the [Fairfax County Registrar](https://www.fairfaxcounty.gov/elections/registration). \n\n'+
        'For questions/comments/issues about this site, please email [us](mailto:voting_guide@pm.me).')