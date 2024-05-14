import pandas as pd
import time

# candidate_path = r'C:\Users\student\Desktop\JOSAA\data\Round1-20240508T102918Z-001\Round1\Candidate.csv'
# choice_path = r'C:\Users\student\Desktop\JOSAA\data\Round1-20240508T102918Z-001\Round1\Choice.csv'
# branch_path = r'C:\Users\student\Desktop\JOSAA\data\Round1-20240508T102918Z-001\Round1\Institute and Branch master.csv'


start_time_loading_merging = time.time()
# candidate = pd.read_csv(candidate_path)
# choice = pd.read_csv(choice_path)
# branch = pd.read_csv(branch_path)
# # If branch_path is not loading, try using the following code:
# branch = pd.read_csv(branch_path, encoding='cp1252')

# # Continue with your processing
# df = pd.merge(candidate, choice, on="RollNo")
# branch_subset = branch[['InstCd', 'SeatType', 'HomeState']]
# merged_df = pd.merge(df, branch_subset, left_on="InstCode", right_on="InstCd", how="left")
# merged_df.drop(columns=['InstCd'], inplace=True)

# Read the data
merged_df = pd.read_csv(r'C:\Users\student\Desktop\JOSAA\data\Round1-20240508T102918Z-001\Round1\processed_data2.csv', nrows=100000)


end_time_loading_merging = time.time()

print(f"Time taken for loading tables and merging: {end_time_loading_merging- start_time_loading_merging:.2f} seconds")


# Functions to determine virtual categories, sub-categories, and gender
def determine_virtual_categories(row):
    if row['Cat'] == 'BC':
        return ['OP', 'BC']
    elif row['Cat'] == 'OP':
        return ['OP']
    elif row['Cat'] == 'EW':
        return ['OP', 'EW']
    elif row['Cat'] == 'SC':
        return ['OP', 'SC']
    elif row['Cat'] == 'ST':
        return ['OP', 'ST']
    else:
        print(f"Unknown category for candidate with RollNo {row['RollNo']}")
        return []


def determine_virtual_sub_categories(row):
    if row['SubCat'] == 'NO':
        return ['NO']
    elif row['SubCat'] == 'PH':
        return ['NO', 'PH']
    else:
        print(f"Unknown sub-category for candidate with RollNo {row['RollNo']}")
        return []


def determine_virtual_gender(row):
    if row['Gender'] == 'F':
        return ['F', 'B']
    elif row['Gender'] == 'B':
        return ['B']
    else:
        print(f"Unknown gender for candidate with RollNo {row['RollNo']}")
        return []


def determine_virtual_state_quota(row):
    if row['InstQuota'] == 'AI':
        return ['AI']
    elif row['InstQuota'] == 'OH':
        if row['StateCode'] in row['HomeState'].split(','):
            return ['HS']
        else:
            return ['OS']
    elif row['InstQuota'] == 'AH':
        if row['StateCode'] in row['HomeState'].split(','):
            return ['AI','HS']
        else:
            return ['AI']
    else:
        print(f"Unknown virtual state for candidate with RollNo {row['RollNo']}")
        return []
    

# Apply the functions to generate virtual categories, sub-categories, and genders
merged_df['Cat_V'] = merged_df.apply(determine_virtual_categories, axis=1)
merged_df = merged_df.explode('Cat_V')
merged_df['SubCat_V'] = merged_df.apply(determine_virtual_sub_categories, axis=1)
merged_df = merged_df.explode('SubCat_V')
merged_df['Gender_V'] = merged_df.apply(determine_virtual_gender, axis=1)
merged_df = merged_df.explode('Gender_V')
merged_df['State_quota_V'] = merged_df.apply(determine_virtual_state_quota, axis=1)
merged_df = merged_df.explode('State_quota_V')



merged_df.sort_values(by=['RollNo', 'ChoiceNo'], inplace=True)


# Generate virtual_choice_number correctly
# Create a unique identifier for each combination of RollNo and ChoiceNo
merged_df['Roll_Choice_ID'] = merged_df['RollNo'].astype(str)
# Calculate VirtualChoiceNumber such that it resets for each new ChoiceNo within the same RollNo
merged_df['ChoiceNo_V'] = merged_df.groupby('Roll_Choice_ID').cumcount() + 1


# Select columns to reorder them as needed
reordered_columns = ['RollNo', 'InstCode', 'Brcode', 'ChoiceNo','ChoiceNo_V', 
                     'InstType', 'InstQuota', 'Stream', 'StateCode', 'HomeState', 'Cat','Cat_V', 'SubCat', 'SubCat_V', 'Gender', 'Gender_V','State_quota_V','Validity']
merged_df = merged_df[reordered_columns]


# Write to CSV
merged_df.to_csv(r'C:\Users\student\Desktop\JOSAA\data\Round1-20240508T102918Z-001\Round1\Virtualized_Choices.csv', index=False)

print(f"Time taken for Virtualization: {time.time()- end_time_loading_merging:.2f} seconds")





