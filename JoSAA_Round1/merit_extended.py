

#To extend the merit list to include preparatory candidates
import pandas as pd


merit_input = '/home/it/Desktop/RUN/Official/Source/R1/Candidates.csv'
merit_output= '/home/it/Desktop/RUN/Official/Source/R1/Extended_merit_list1.csv'

# RollNo,SCode,Gender,CAT,PwD,Nationality,AI_Eng_CRL_Rank,AI_Eng_OBC_NCL_Rank,AI_Eng_SC_Rank,AI_Eng_ST_Rank,AI_Eng_EWS_Rank,AI_Eng_CRL_PD_Rank,AI_Eng_OBC_NCL_PD_Rank,AI_Eng_SC_PD_Rank,AI_Eng_ST_PD_Rank,AI_Eng_EWS_PD_Rank,AI_ARC_CRL_Rank,AI_ARC_OBC_NCL_Rank,AI_ARC_SC_Rank,AI_ARC_ST_Rank,AI_ARC_EWS_Rank,AI_ARC_CRL_PD_Rank,AI_ARC_OBC_NCL_PD_Rank,AI_ARC_SC_PD_Rank,AI_ARC_ST_PD_Rank,AI_ARC_EWS_PD_Rank,AI_Pln_CRL_Rank,AI_Pln_OBC_NCL_Rank,AI_Pln_SC_Rank,AI_Pln_ST_Rank,AI_Pln_EWS_Rank,AI_Pln_CRL_PD_Rank,AI_Pln_OBC_NCL_PD_Rank,AI_Pln_SC_PD_Rank,AI_Pln_ST_PD_Rank,AI_Pln_EWS_PD_Rank,Adv_CRL_Rank,Adv_OBC_NCL_Rank,Adv_SC_Rank,Adv_ST_Rank,Adv_EWS_Rank,Adv_CRL_PD_Rank,Adv_OBC_NCL_PD_Rank,Adv_SC_PD_Rank,Adv_ST_PD_Rank,Adv_EWS_PD_Rank,Adv_IsPrep,Adv_Prep_SC_Rank,Adv_Prep_ST_Rank,Adv_Prep_CRL_PD_Rank,Adv_Prep_OBC_NCL_PD_Rank,Adv_Prep_SC_PD_Rank,Adv_Prep_ST_PD_Rank,Adv_Prep_EWS_PD_Rank,Adv_DS,Decision


def print_last_rank(df):

    # Get the last rank number for each column
    last_rank_Adv_CRL_PD_Rank = df['Adv_CRL_PD_Rank'].max()
    last_rank_Adv_OBC_NCL_PD_Rank = df['Adv_OBC_NCL_PD_Rank'].max()
    last_rank_Adv_SC_PD_Rank = df['Adv_SC_PD_Rank'].max()
    last_rank_Adv_ST_PD_Rank = df['Adv_ST_PD_Rank'].max()
    last_rank_Adv_EWS_PD_Rank = df['Adv_EWS_PD_Rank'].max()
    last_rank_Adv_SC_Rank = df['Adv_SC_Rank'].max()
    last_rank_Adv_ST_Rank = df['Adv_ST_Rank'].max()

    # Output the last rank number for each column
    print("Last Rank for Adv_CRL_PD_Rank:", last_rank_Adv_CRL_PD_Rank)
    print("Last Rank for Adv_OBC_NCL_PD_Rank:", last_rank_Adv_OBC_NCL_PD_Rank)
    print("Last Rank for Adv_SC_PD_Rank:", last_rank_Adv_SC_PD_Rank)
    print("Last Rank for Adv_ST_PD_Rank:", last_rank_Adv_ST_PD_Rank)
    print("Last Rank for Adv_EWS_PD_Rank:", last_rank_Adv_EWS_PD_Rank)
    print("Last Rank for Adv_SC_Rank:", last_rank_Adv_SC_Rank)
    print("Last Rank for Adv_ST_Rank:", last_rank_Adv_ST_Rank)

    # Identify rows where candidates are eligible for preparatory course
    prep_candidates = df[df['Adv_IsPrep'] == 1]

    # Find the last rank of each preparatory rank list column
    last_rank_crl_pd = prep_candidates['Adv_Prep_CRL_PD_Rank'].max()
    last_rank_obc_ncl_pd = prep_candidates['Adv_Prep_OBC_NCL_PD_Rank'].max()
    last_rank_sc_pd = prep_candidates['Adv_Prep_SC_PD_Rank'].max()
    last_rank_st_pd = prep_candidates['Adv_Prep_ST_PD_Rank'].max()
    last_rank_ews_pd = prep_candidates['Adv_Prep_EWS_PD_Rank'].max()
    last_rank_sc = prep_candidates['Adv_Prep_SC_Rank'].max()
    last_rank_st = prep_candidates['Adv_Prep_ST_Rank'].max()

    print("Last rank of Adv_Prep_CRL_PD_Rank:", last_rank_crl_pd)
    print("Last rank of Adv_Prep_OBC_NCL_PD_Rank:", last_rank_obc_ncl_pd)
    print("Last rank of Adv_Prep_SC_PD_Rank:", last_rank_sc_pd)
    print("Last rank of Adv_Prep_ST_PD_Rank:", last_rank_st_pd)
    print("Last rank of Adv_Prep_EWS_PD_Rank:", last_rank_ews_pd)
    print("Last rank of Adv_Prep_SC_Rank:", last_rank_sc)
    print("Last rank of Adv_Prep_ST_Rank:", last_rank_st)


# Read the CSV file
df = pd.read_csv(merit_input)
df = df.rename(columns={'CAT': 'Cat', 'PwD': 'SubCat', 'SCode': 'StateCode'})

print('ranks before extending')
print_last_rank(df)


# Identify rows where candidates are eligible for preparatory course
prep_candidates = df[df['Adv_IsPrep'] == 1]

# Initialize variables to store the maximum ranks
max_crl_pd_rank = df['Adv_CRL_PD_Rank'].max()
max_obc_ncl_pd_rank = df['Adv_OBC_NCL_PD_Rank'].max()
max_sc_pd_rank = df['Adv_SC_PD_Rank'].max()
max_st_pd_rank = df['Adv_ST_PD_Rank'].max()
max_ews_pd_rank = df['Adv_EWS_PD_Rank'].max()
max_sc_rank = df['Adv_SC_Rank'].max()
max_st_rank = df['Adv_ST_Rank'].max()

# Iterate over each preparatory candidate
for index, candidate in prep_candidates.iterrows():
    # Check if preparatory ranks are not null, and add them to the regular rank columns
    if not pd.isnull(candidate['Adv_Prep_CRL_PD_Rank']):
        df.at[index, 'Adv_CRL_PD_Rank'] = int(candidate['Adv_Prep_CRL_PD_Rank'] + max_crl_pd_rank)
    if not pd.isnull(candidate['Adv_Prep_OBC_NCL_PD_Rank']):
        df.at[index, 'Adv_OBC_NCL_PD_Rank'] = int(candidate['Adv_Prep_OBC_NCL_PD_Rank'] + max_obc_ncl_pd_rank)
    if not pd.isnull(candidate['Adv_Prep_SC_PD_Rank']):
        df.at[index, 'Adv_SC_PD_Rank'] = int(candidate['Adv_Prep_SC_PD_Rank'] + max_sc_pd_rank)
    if not pd.isnull(candidate['Adv_Prep_ST_PD_Rank']):
        df.at[index, 'Adv_ST_PD_Rank'] = int(candidate['Adv_Prep_ST_PD_Rank'] + max_st_pd_rank)
    if not pd.isnull(candidate['Adv_Prep_EWS_PD_Rank']):
        df.at[index, 'Adv_EWS_PD_Rank'] = int(candidate['Adv_Prep_EWS_PD_Rank'] + max_ews_pd_rank)
    if not pd.isnull(candidate['Adv_Prep_SC_Rank']):
        df.at[index, 'Adv_SC_Rank'] = int(candidate['Adv_Prep_SC_Rank'] + max_sc_rank)
    if not pd.isnull(candidate['Adv_Prep_ST_Rank']):
        df.at[index, 'Adv_ST_Rank'] = int(candidate['Adv_Prep_ST_Rank'] + max_st_rank)

# Now the empty rows in the regular rank columns for preparatory course candidates are filled with corresponding preparatory ranks plus the last rank of the regular rank column


# Now the empty rows in the regular rank columns for preparatory course candidates are filled with corresponding preparatory ranks plus the last rank of the regular rank column

print('Rank after extedning')
print_last_rank(df)


# Save the updated DataFrame to a new CSV file or overwrite the existing one
df.to_csv(merit_output, index=False)
