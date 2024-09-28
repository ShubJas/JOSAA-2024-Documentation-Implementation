# CSAB Round 1 Virtualisation
## Code Snippet 1: Importing Libraries

In this section of the code, the following libraries are imported:
- `pandas`: for data manipulation and analysis.
- `time`: for time-related functions.
- `concurrent.futures.ProcessPoolExecutor`: for parallel processing.
- `dask.dataframe`: for processing large datasets efficiently.

The script also starts a timer using `time.time()` to track the full execution time.

### Code:
    
        import pandas as pd
        import time
        from concurrent.futures import ProcessPoolExecutor
        import dask.dataframe as dd

        start_full = time.time()
    
## Code Snippet 2: Defining File Paths and Loading Data

In this section, the script defines the file paths for **CSAB Round 1** data, such as candidates, choices, and seat availability. The paths point to `.csv` files containing this information, and the data is loaded using `pandas.read_csv()`. Additionally, a dataset of confirmed candidates is read and filtered by roll numbers.

### Key File Paths:
- `candidate_path`: Path to the candidate data CSV file.
- `choice_path`: Path to the choices made by candidates.
- `seats_path`: Path to the seat availability data.
- `last_can_confirm_path`: Path to the last confirmed candidates dataset.

The **choice** data is further filtered to exclude invalid entries where the `Validity` column is marked 'N'.

### Code:
    
        # File paths for candidate, choice, and seat data
        candidate_path = '/home/it/Desktop/RUN/Official/Source/CSAB_R1/Candidate.csv'
        candidate_path = '/home/it/Desktop/RUN/Official/CSAB_R1/mergedCandidates.csv'
        choice_path = '/home/it/Desktop/RUN/Official/Source/CSAB_R1/Choices_NIC.csv'
        seats_path = '/home/it/Desktop/RUN/Official/Source/CSAB_R1/Seat.csv'

        # Path for last confirmed candidates
        last_can_confirm_path = '/home/it/Desktop/RUN/Official/CSAB_R1/last_op_append_candidates.csv'
        
        # Load data from CSV files
        last_can_confirm = pd.read_csv(last_can_confirm_path)
        last_can_confirm_rolls = last_can_confirm['Rollno']

        # Load candidate, choice, and seat data
        candidate = pd.read_csv(candidate_path)
        choice = pd.read_csv(choice_path)
        choice_filtered = choice[choice['Validity'] != 'N']
        seat = pd.read_csv(seats_path)
    
## Code Snippet 3: Filtering Candidates Based on Institution Code

In this section, the script filters the candidate dataset to select only those candidates whose `InstCd` (Institution Code) is greater than or equal to 200. This step is essential for focusing on specific categories of institutions, likely pertaining to certain eligibility criteria or allocation rules in **CSAB Round 1**.


### Filter candidates with Institution Code >= 200
    temp_cand = candidate[candidate['InstCd'] >= 200]

In this section, the script converts the data type of the `InstCd` (Institution Code) column in the `temp_cand` DataFrame to integers. This conversion ensures that subsequent operations and comparisons involving institution codes are performed correctly, as they need to be treated as numerical values.

### Convert InstCd data type to integer
    temp_cand['InstCd'] = temp_cand['InstCd'].astype(int)


## Code Snippet 4: Merging Candidate and Choice Data

In this section, the script measures the time taken to merge the `choice_filtered` DataFrame with the `candidate` DataFrame based on the `RollNo` column. The resulting merged DataFrame is then saved as a CSV file named `candidate_choice_merge_CSAB0.csv`. This step consolidates the candidates' choices with their corresponding details for further processing.

### Code:

    # Start timer
    start_ti = time.time()

    # Merge choice_filtered and candidate DataFrames on RollNo
    df = pd.merge(choice_filtered, candidate, on="RollNo")

    # Save the merged DataFrame as a CSV file
    df.to_csv('candidate_choice_merge_CSAB0.csv', index=False)

    # End timer and print time taken
    end_ti = time.time()
    print(f"time taken to merge candidate and choice and save as csv- {end_ti - start_ti}")


## Code Snippet 5: Extracting Unique Genders

In this section, the script retrieves the unique values from the `Gender` column of the merged DataFrame `df`. This operation is useful for understanding the distinct gender categories present in the dataset, which can be essential for further analysis or processing.

### Code:

    # Extract unique values from the Gender column
    unique_genders = df['Gender'].unique()

    # Optionally print the unique genders
    print(unique_genders)


## Code Snippet 6: Creating a Dictionary of Institutes

This section of the code constructs a dictionary called `institutes`, which maps institution codes to their respective state codes. The dictionary is populated by iterating through the `seat` DataFrame. Only institutions with quotas 'OS' (Other State) or 'HS' (Home State) are included. This helps in managing and referencing the relevant institutes for further processing.

### Code:

    # Initialize an empty dictionary to store institutes
    institutes = {}

    # Populate the institutes dictionary based on the seat DataFrame
    for index, row in seat.iterrows():
        if row['Quota'] == 'OS' or row['Quota'] == 'HS':
            if row['InstCd'] not in institutes.keys():
                institutes[row['InstCd']] = [
                    row['Stcode1'], row['Stcode2'], row['Stcode3'],
                    row['Stcode4'], row['Stcode5'], row['Stcode6'],
                    row['Stcode7'], row['Stcode8'], row['Stcode9'], row['Stcode10']
                ]


## Code Snippet 7: Constructing Institute Quota Dictionary

This section creates a dictionary called `institute_quota_dict` to track the quotas associated with each institute based on the `seat` DataFrame. The dictionary uses the institution code as the key and a set of quotas as the value. The code then processes this dictionary to determine the final quota for each institute, which is stored in `final_institute_quota_dict`. 

### Code:

    # Initialize an empty dictionary to store quotas for each institute
    institute_quota_dict = {}

    # Populate the institute_quota_dict with quotas from the seat DataFrame
    for _, row in seat.iterrows():
        institute = row['InstCd']
        quota = row['Quota']
        
        if institute not in institute_quota_dict:
            institute_quota_dict[institute] = set()
        
        institute_quota_dict[institute].add(quota)

    # Process the dictionary to set the final quota values
    final_institute_quota_dict = {}

    for institute, quotas in institute_quota_dict.items():
        if quotas == {'AI'}:
            final_institute_quota_dict[institute] = 'AI'
        elif quotas == {'AI', 'HS'}:
            final_institute_quota_dict[institute] = 'AH'
        else:
            final_institute_quota_dict[institute] = 'OH'



## Code Snippet 8: Deleting Unused DataFrames

In this section, the DataFrames `df`, `candidate`, and `choice` are deleted to free up memory and resources, as they are no longer needed after processing.

### Code:

    # Delete unused DataFrames to free up memory
    del df, candidate, choice




## Code Snippet 9: Defining Functions for Virtualization

In this section, several functions are defined to categorize candidates based on their attributes. These functions will be used to determine the virtual categories, subcategories, gender, and state quotas for each candidate.

### Code:

# Virtual Categories
This function categorizes candidates based on their specified category (`Cat`). It returns a list that includes the open category (`OP`) along with the candidate's specific virtualised category, allowing for proper classification within the admissions process.

    def determine_virtual_categories(row):
        if row['Cat'] == 'BC':
            return ['OP', 'BC']
        elif row['Cat'] == 'GN':
            return ['OP']
        elif row['Cat'] == 'EW':
            return ['OP', 'EW']
        elif row['Cat'] == 'SC':
            return ['OP', 'SC']
        elif row['Cat'] == 'ST':
            return ['OP', 'ST']
        else:
            return []

# Virtual Subcategories
This function determines the virtual subcategories based on the candidate's disability status (PwD). If the candidate is a person with no disabilities (indicated by PwD == 2), it returns a list with only the category NO. Otherwise, it includes both NO and PH to indicate the candidate's status.

    def determine_virtual_sub_categories(row):
        if row['PwD'] == 2:
            return ['NO']
        else:
            return ['NO', 'PH']

# Virtual Gender
This function determines the virtual gender for candidates based on their gender attribute. If the candidate identifies as female (indicated by Gender == 2), it returns a list including both female (F) and base Gender Nuetral category (B). If not, it only returns the base category.

    def determine_virtual_gender(row):
        if row['Gender'] == 2:
            return ['F', 'B']
        else:
            return ['B']

# Virtual State Quota
This function assesses the candidate's state quota eligibility based on their institution code (Instcd) and state code (SCode). It returns a list of quotas that the candidate is eligible for, including any specific state quotas that may apply based on the institution they are associated with.

    def determine_virtual_state_quota(row):
        if final_institute_quota_dict[row['Instcd']] == 'AI':
            return ['AI']
        
        if row['Instcd'] == 209 and row['SCode']=='GO':
            return ['AI', 'GO']    
        
        if row['Instcd'] == 225 and row['SCode']=='JK':
            return ['AI', 'JK']    
        
        if row['Instcd'] == 225 and row['SCode']=='LA':
            return ['AI', 'LA']    
        
        state_codes = institutes[row['Instcd']]
        if row['SCode'] in state_codes:
            return ['AI', 'HS']
        else:
            if final_institute_quota_dict[row['Instcd']] == 'OH':
                return ['AI', 'OS']
            else:
                return ['AI']


## Code Snippet 10: Processing Candidate Data in Chunks

This code snippet is responsible for processing candidate data in chunks, applying various virtualization functions to categorize candidates based on their attributes. The data is read from a CSV file in chunks to manage memory usage effectively. The processed data is then merged, sorted, and saved into a new CSV file for further analysis.

### Overview of the Process

1. **Chunk Processing**: The function `process_chunk` filters the candidate data based on specific decision criteria and applies various functions to derive virtual categories, subcategories, gender, and state quotas.
2. **Parallel Processing**: The script utilizes `ProcessPoolExecutor` for parallel processing of data chunks, improving processing time.
3. **Sorting and Virtual Count**: After merging processed chunks, the data is sorted by `RollNo` and `ChoiceNo`, and a virtual count is created to track choices.
4. **CSV Output**: Finally, the processed DataFrame is saved as a CSV file for further use.

### Code:
## process_chunk Function:
Filters candidates based on decision criteria,Applies virtualization functions (determine_virtual_categories, determine_virtual_sub_categories, determine_virtual_state_quota, determine_virtual_gender) to add relevant columns and uses the explode function to expand lists into separate rows for each virtual attribute.

    def process_chunk(chunk):
        chunk = chunk[
            (chunk['Decision'] == 'FL') | 
            ((chunk['Decision'] == 'FR') & (chunk['ChoiceNo'] >= chunk['AllotedOpt'])) | 
            ((chunk['Decision'] == 'SL') & 
            ((chunk['ChoiceNo'] >= chunk['AllotedOpt']) | 
            ((chunk['ChoiceNo'] < chunk['AllotedOpt']) & chunk['InstCd'].notna() & (chunk['InstCd'].fillna(-1).astype(int) == chunk['Instcd']))))
        ]
        chunk['Cat_V'] = chunk.apply(determine_virtual_categories, axis=1)
        chunk = chunk.explode('Cat_V')
        chunk['SubCat_V'] = chunk.apply(determine_virtual_sub_categories, axis=1)
        chunk = chunk.explode('SubCat_V')
        chunk['State_quota_V'] = chunk.apply(determine_virtual_state_quota, axis=1)
        chunk = chunk.explode('State_quota_V')
        chunk['Gender_V'] = chunk.apply(determine_virtual_gender, axis=1)
        chunk = chunk.explode('Gender_V')
        return chunk

## Data loading and merging

    start_time_loading_merging = time.time()

    chunks = pd.read_csv(r'candidate_choice_merge_CSAB0.csv', chunksize=70000)

    processed_chunks = []

    with ProcessPoolExecutor() as executor:
        for processed_chunk in executor.map(process_chunk, chunks):
            processed_chunks.append(processed_chunk)

    merged_df = pd.concat(processed_chunks, ignore_index=True)

    end_time_loading_merging = time.time()
    print(f"Time taken for loading tables and merging and running virtualization: {end_time_loading_merging - start_time_loading_merging:.2f} seconds")
## Sorting and Virtual Count:
    print(f"Now Sorting:")
    merged_df.sort_values(by=['RollNo', 'ChoiceNo'], inplace=True)
    end_time_sorting = time.time()

    print(f"Time taken for Sorting: {end_time_sorting - end_time_loading_merging:.2f} seconds")

    print(f"Now creating Virtual count")
    merged_df['ChoiceNo_V'] = merged_df.groupby(['RollNo']).cumcount() + 1
    end_time_V = time.time()
    print(f"Time taken for creating Virtual count: {end_time_V - end_time_sorting:.2f} seconds")

    reordered_columns = ['RollNo', 'Instcd', 'Brcd', 'ChoiceNo', 'ChoiceNo_V', 'Cat_V', 'SubCat_V', 'Gender_V', 'State_quota_V']

    normal_df = merged_df[reordered_columns]
## CSV Output

    print(f"Now creating csv file")
    normal_df.to_csv('Normal_Virtualized_Choices_CSAB0.csv', index=False)

    print(f"Time taken for creating csv file: {time.time() - end_time_V:.2f} seconds")
