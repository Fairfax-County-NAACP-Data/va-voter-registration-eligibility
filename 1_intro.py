import streamlit as st

st.header('Virginia Voter Registration Guide')
st.info('**Did you know that after a recent '
        '[court victory](https://www.vpm.org/news/2026-01-29/federal-judge-va-voting-rights-king-johnson-gibney-aclu-readmission-act-1870),'+
        ' the right to vote has been restored in Virginia to many people with a felony conviction?** Find out more below!')

questions = [
    "How do I register to vote?",
    'When is the deadline for registration?',
    'I have a felony conviction. Can I register to vote?',
    'I have a felony conviction. How do I answer the felony questions on the voter registration form?',
    'Tips for answering questions on the voter registration form',
    'What is this court ruling?',
    'Is this related to the constitutional amendment?'
]

answers = [
    'You can [register to VOTE here!](https://www.elections.virginia.gov/registration/how-to-register/)',
    'The deadline to register to vote in the November 3, 2026 General Election is 10/23/2026. You can also [register on the same day you vote at your polling place]'
            '(https://www.elections.virginia.gov/registration/same-day-voter-registration/) after 10/23/2026.\n\nHowever, if you have a felony conviction, the Fairfax County '
            "Registrar's Office recommends submitting the voter registration as early as possible. The registration will need to be reviewed to confirm that you are eligible to "
            'vote (see the Eligibility tab linked at the top of this page or the "Can I Register to Vote?" question below)',
    None,
    'Answer as follows:\n- Have you ever been convicted of a felony or judged mentally incapacitated and disqualified to vote? **Mark YES**\n'+
        '- If YES, has your right to vote been restored? **Mark NO** (Unless it has been restored!)\n\n'
        "Guidance provided by Fairfax County Registrar's Office.",
    'Improve your Chances of Successful Registration]:\n'
        '- Fields with asterisks (*) are REQUIRED\n'
        '- Middle name is required. If you do not have one, check "None"\n'
        '- Social security number is required. If one was never issued, check that box\n'
        '- Your residence address cannot be a PO Box. If you are homeless, [vote.gov](https://vote.gov/guide-to-voting/unhoused) recommends putting a '
            'shelter or religious center. If you are homeless or your residence cannot receive mail, provide a mailing address in Section 4 and check '
            'the appropriate box.\n'
        '- If you have been convicted of a felony, mark YES to that question in Section 3\n'
        '- If you have been convicted of a felony AND have not had the governor restore your rights, mark NO to that question in Section 3\n'
        '- Be sure to sign and date the registration application',
    '[In January 2026, a federal judge ordered widespread voting rights restoration for Virginians convicted of a felony]'+
            '(https://www.vpm.org/news/2026-01-29/federal-judge-va-voting-rights-king-johnson-gibney-aclu-readmission-act-1870).'+
            '\n\nThis means that:\n'+
            "- Voting rights can ONLY be taken away for certain felonies that were common law in *1870*\n"+
            "- Virginia can no longer take away the right to vote for drug crimes and MANY other felonies\n"+
            "- If you were not convicted of one of these crimes and meet the general eligibility criteria, you may register to vote\n"+
            "- No need to apply for restoration of rights from the Governor if felony conviction was not common law in 1870",
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