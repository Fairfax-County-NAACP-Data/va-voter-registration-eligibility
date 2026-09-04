import pandas as pd
import streamlit as st

st.header('Virginia Voter Registration Guide')
st.info('**Did you know that after a recent '
        '[court victory](https://www.vpm.org/news/2026-01-29/federal-judge-va-voting-rights-king-johnson-gibney-aclu-readmission-act-1870),'+
        ' the right to vote has been restored in Virginia to many people with a felony conviction?** Find out more below and check out the [Campaign Legal Center Factsheet](https://campaignlegal.org/document/know-your-rights-voting-felony-conviction-virginia)!')

questions = [
    "How do I register to vote?",
    "Not sure if you are registered or not?",
    'When is the deadline for registration?',
    'I have a felony conviction. Can I register to vote?',
    'I have a felony conviction. How do I answer the felony questions on the voter registration form?',
    'Tips for answering questions on the voter registration form',
    'What is this court ruling?',
    'Is this related to the constitutional amendment?'
]

if pd.Timestamp.now() < pd.Timestamp('2026-09-05 13:00:00'):
    add = '\n\nIf you would like assistance registering, **Fairfax County NAACP will be registering voters at Sherwood Library on September 5 from 10 AM to 1 PM**.' \
        f' Sign up [here]({st.secrets["signup"]}) to join us!'
else:
    add = ''

answers = [
    'You can [register to VOTE here!](https://www.elections.virginia.gov/registration/how-to-register/)'+add,
    'Check your status [here](https://vote.elections.virginia.gov/VoterInformation)',
    'The deadline to register to vote in the November 3, 2026 General Election is October 23rd.\n\nYou can also [register on the same day you vote at your polling place]'
            '(https://www.elections.virginia.gov/registration/same-day-voter-registration/) after October 23rd.\n\nHowever, if you have a felony conviction, the Fairfax County '
            "Registrar's Office recommends submitting the voter registration as early as possible. The registration will need to be reviewed to confirm that you are eligible to "
            'vote.',
    'The court ruling states the ONLY people INELIGIBLE to vote are those convicted of the following: '
        '"[arson, burglary, escape or rescue from jail, larceny, manslaughter, mayhem, murder, rape, robbery, sodomy or suicide]'
        '(https://virginiamercury.com/2026/08/20/judge-affirms-ruling-in-favor-of-former-felons-in-voting-rights-lawsuit/)". According to the [Campaign Legal Center](https://campaignlegal.org/document/know-your-rights-voting-felony-conviction-virginia), "to determine whether you are eligible to vote, you should fill out the voter registration form, and Virginia election officials will determine your eligibility if you are not convicted of one of those crimes, you are eligible to vote."\n\n'
        'When registering to vote, mark YES on the form that you have been convicted of a felony, and your application will be '
        'reviewed to confirm your eligibility.',
    'According to the Fairfax County Registrar\'s Office, answer as follows:\n- Have you ever been convicted of a felony or judged mentally incapacitated and disqualified to vote? **Mark YES**\n'+
        '- Has your right to vote been restored? **Mark NO if it has not been restored by the governor or YES if it has been**',
    'Improve your chances of successful registration:\n'
        '- Fields with asterisks (*) are REQUIRED\n'
        '- Middle name is required. If you do not have one, check "None"\n'
        '- Social security number is required. If one was never issued, check the box that states "No SSN was ever issued"\n'
        '- Your residence address cannot be a PO Box. If you are homeless, [vote.gov](https://vote.gov/guide-to-voting/unhoused) recommends putting a '
            'shelter or religious center. If you are homeless or your residence cannot receive mail, provide a mailing address in Section 4 and check '
            'the appropriate box.\n'
        '- If you have been convicted of a felony, mark YES to that question in Section 3.\n'
        '- If you have been convicted of a felony AND have not had the governor restore your rights, mark NO to that question in Section 3\n'
        '- Be sure to sign and date the registration application',
    '[In January 2026, a federal judge ordered widespread voting rights restoration for Virginians convicted of a felony]'+
            '(https://www.vpm.org/news/2026-01-29/federal-judge-va-voting-rights-king-johnson-gibney-aclu-readmission-act-1870).'+
            '\n\nThis means that:\n'+
            "- Voting rights can ONLY be taken away for certain felonies that were common law in *1870*. "+
                "According to the ruling, voting can ONLY be taking away for arson, burglary, escape or rescue from jail, larceny, manslaughter, mayhem, murder, rape, robbery, sodomy or suicide.\n"+
            "- Virginia can no longer take away the right to vote for drug crimes and MANY other felonies\n"+
            "- If you were not convicted of one of these crimes and meet the general eligibility criteria, you are eligible to vote\n"+
            "- No need to apply for restoration of rights from the Governor if felony conviction was for a crime that was not common law in 1870",
    'No, the court ruling has an *immediate* effect and enables people to vote in the 2026 Elections. In November, there are '+
        '[3 constitutional amendments on the ballot]'
        '(https://virginiaindependentnews.com/politics/virginia-voters-will-decide-3-ballot-measures-in-november-general-election/) '+
        'that you will be able to vote on if you are eligible. If it passes, one of them states that a person convicted of a felony '+
        '"[upon release from incarceration for that felony conviction and without further action required of him, such person shall be invested '+
        'with all political rights, including the right to vote](https://lis.virginia.gov/bill-details/20251/HJ2)."',
]

for q,a in zip(questions, answers):
    with st.expander(q):
        if a:
            st.markdown(a)
        else:
            st.markdown('Many people can now vote with felony convictions! We have built a tool to help you determine if you are eligible to vote.\n\nClick **Am I Eligible?** below:')
            if st.button('Am I Eligible?'):
                st.switch_page('2_eligibility.py')