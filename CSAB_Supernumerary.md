# Supernumerary CSAB Virtualisation
## Code Snippet 1: Importing Libraries

In this section of the code, the following libraries are imported:
- `pandas`: for data manipulation and analysis.
- `time`: for time-related functions.
- `concurrent.futures.ProcessPoolExecutor`: for parallel processing.
- `dask.dataframe`: (commented out) could be used for parallel processing of large datasets but is currently not included.

### Code:
    ```python
    import pandas as pd
    import time
    from concurrent.futures import ProcessPoolExecutor

## Code Snippet 2: File Paths and Data Loading

This section defines the paths to various CSV files and loads them into pandas dataframes. Additionally, it renames some columns for consistency.

### File Paths:
- `candidate_path`: Path to the file containing filtered candidate data.
- `choice_path`: Path to the file containing choices made by candidates.
- `seats_path`: Path to the file containing seat information.
- `Inst_path`: Path to the file containing institute information.
- `merge_path`: Path for the merged candidate and choice data.
- `normal_path`: Path for the normal virtualized choices output.
- `ds_path`: Path for the DS virtualized choices output.

### Code:
    ```python
    candidate_path = '/home/it/Desktop/RUN/Official/Source/CSAB_SuperNumerary/filtered_candidates.csv'
    choice_path = '/home/it/Desktop/RUN/Official/Source/CSAB_SuperNumerary/Choice.csv'
    seats_path = '/home/it/Desktop/RUN/Official/Source/CSAB_SuperNumerary/Seats.csv'

    Inst_path = '/home/it/Desktop/RUN/Official/Source/CSAB_SuperNumerary/Institutes.csv'
    merge_path='candidate_choice_merge.csv'
    normal_path='Normal_Virtualized_Choices.csv'
    ds_path='DS_Virtualized_Choices.csv'
## Code Snippet 3: Data Loading and Renaming

In this section, we load candidate, choice, and seat data from CSV files using `pandas`, followed by renaming columns for standardization. The commented-out `dask` lines indicate an alternative method for handling large datasets.

### Candidate Data:
The `candidate` dataframe is loaded from the path defined earlier, and columns are renamed:
- `CAT` → `Cat`
- `PwD` → `SubCat`
- `SCode` → `StateCode`

### Choice Data:
Similarly, the `choice` dataframe is loaded and its columns are renamed:
- `Rollno` → `RollNo`
- `Instcd` → `InstCode`
- `Brcd` → `Brcode`
- `Optno` → `ChoiceNo`

### Seat Data:
The seat data is updated with several column renames to ensure consistency. This step is critical when dealing with multiple data sources that have different column naming conventions.

#### Code:
    ```python
    candidate = pd.read_csv(candidate_path)
    candidate = candidate.rename(columns={'CAT': 'Cat', 'PwD': 'SubCat', 'SCode': 'StateCode'})
    choice = pd.read_csv(choice_path)
    choice = choice.rename(columns={'Rollno': 'RollNo', 'Instcd': 'InstCode', 'Brcd': 'Brcode', 'Optno':'ChoiceNo'})



#### Updated seats
    ```python
    seat = pd.read_csv(seats_path)
    seat = seat.rename(columns={'InstCd': 'InstCode', 'BrCd': 'Brcode',
                                'StCd1':'Stcode1','StCd2':'Stcode2','StCd2':'Stcode2',
                                'StCd3':'Stcode3','StCd4':'Stcode4','StCd5':'Stcode5',
                                'StCd6':'Stcode6','StCd7':'Stcode7','StCd8':'Stcode8',
                                'StCd9':'Stcode9','StCd10':'Stcode10','TSeat':'TotalSeat'})

## Code Snippet 4: Merging DataFrames and Measuring Time

In this section, we merge the `candidate` and `choice` dataframes on the `RollNo` column and save the merged dataframe as a CSV file. We also use `time` to measure the execution time for this operation.

### Code:
    
    start_ti = time.time()

#### Merging candidate and choice dataframes
    
    df = pd.merge(candidate, choice, on="RollNo")

#### Saving the merged dataframe to CSV
    
    df.to_csv(merge_path, index=False)

#### Measuring end time
    
    end_ti = time.time()

#### Printing the time taken for the operation
    
    print(f"time taken to merge candidate and choice and save as csv- {end_ti - start_ti}")

## Code Snippet 5: Populating the `institutes` Dictionary

In this section, we create a dictionary named `institutes` to store state codes associated with each institute code, based on the `Quota` field in the `seat` dataframe. Only institutes with quotas 'OS' or 'HS' are included.

### Code:
    
    institutes = {}

    # Iterating through the seat dataframe
    for index, row in seat.iterrows():
        # Checking for 'OS' or 'HS' quota
        if row['Quota'] == 'OS' or row['Quota'] == 'HS':
            # Adding the institute code and corresponding state codes to the dictionary
            if row['InstCode'] not in institutes.keys():
                institutes[row['InstCode']] = [
                    row['Stcode1'], row['Stcode2'], row['Stcode3'], 
                    row['Stcode4'], row['Stcode5'], row['Stcode6'], 
                    row['Stcode7'], row['Stcode8'], row['Stcode9'], row['Stcode10']
                ]

## Code Snippet 6: Populating the `Quotas` Dictionary

In this section, we create a dictionary named `Quotas` to map each institute code to its respective seat type from the `Inst` dataframe.

### Code:
    
    # Load the institutes data
    Inst = pd.read_csv(Inst_path)

    # Initialize an empty dictionary for quotas
    Quotas = {}

    # Iterating through the Inst dataframe
    for index, row in Inst.iterrows():
        # Adding institute code and corresponding seat type to the dictionary
        Quotas[row['InstCd']] = row['SeatType']

## Code Snippet 7: Deleting DataFrames

In this section, we delete the `df`, `candidate`, `choice`, and `seat` dataframes to free up memory after they are no longer needed.

### Code:
    
    # Deleting dataframes to free up memory
    del df
    del candidate
    del choice
    del seat

## Code Snippet 8: Virtual Category Determination and Data Processing

This section includes functions to determine virtual categories, sub-categories, and gender for each row of data. It processes data in chunks, applies these functions, and merges the results. The code also handles sorting and virtual count creation, and finally exports the processed data to a CSV file.

### Functions:
- `determine_virtual_categories(row)`: Determines virtual categories based on the `Cat` column.
- `determine_virtual_sub_categories(row)`: Determines virtual sub-categories based on the `SubCat` column.
- `determine_virtual_gender(row)`: Determines virtual gender based on the `Gender` column.

### Processing Function:
- `process_chunk(chunk)`: Applies the above functions to each chunk of data, explodes the lists of virtual categories, sub-categories, and gender, and returns the processed chunk.

### Code:
    
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

    def determine_virtual_sub_categories(row):
        if row['SubCat'] == 2:
            return ['NO']
        elif row['SubCat'] == 1:
            return ['NO', 'PH']
        else:
            return []

    def determine_virtual_gender(row):
        if row['Gender'] == 2:
            return ['F', 'B']
        else:
            return ['B']

    def process_chunk(chunk):
        chunk['Cat_V'] = chunk.apply(determine_virtual_categories, axis=1)
        chunk = chunk.explode('Cat_V')
        chunk['SubCat_V'] = chunk.apply(determine_virtual_sub_categories, axis=1)
        chunk = chunk.explode('SubCat_V')
        chunk['Gender_V'] = chunk.apply(determine_virtual_gender, axis=1)
        chunk = chunk.explode('Gender_V')
        # chunk['State_quota_V'] = chunk.apply(determine_virtual_state_quota, axis=1)
        # chunk = chunk.explode('State_quota_V')
        return chunk

    start_time_loading_merging = time.time()

### Reading data in chunks and processing each chunk in parallel
    chunks = pd.read_csv(merge_path, chunksize=100000)
    processed_chunks = []

    with ProcessPoolExecutor() as executor:
        for processed_chunk in executor.map(process_chunk, chunks):
            processed_chunks.append(processed_chunk)

### Concatenating all processed chunks
    merged_df = pd.concat(processed_chunks, ignore_index=True)

    end_time_loading_merging = time.time()
    print(f"Time taken for loading tables and merging and running virtualization: {end_time_loading_merging - start_time_loading_merging:.2f} seconds")

### Sorting the merged dataframe
    print(f"Now Sorting:")
    merged_df.sort_values(by=['RollNo', 'ChoiceNo'], inplace=True)
    end_time_sorting = time.time()
    print(f"Time taken for Sorting: {end_time_sorting - end_time_loading_merging:.2f} seconds")

### Creating virtual count
    print(f"Now creating Virtual count")
    merged_df['ChoiceNo_V'] = merged_df.groupby(['RollNo']).cumcount() + 1
    end_time_V = time.time()
    print(f"Time taken for creating Virtual count: {end_time_V - end_time_sorting:.2f} seconds")

### Select columns to reorder them as needed
    reordered_columns = ['RollNo', 'InstCode', 'Brcode', 'ChoiceNo', 'ChoiceNo_V', 'Cat_V', 'SubCat_V', 'Gender_V', 'State_quota_V', 'Validity', 'Adv_DS_V', 'Nationality']

    normal_df = merged_df[reordered_columns]

### Exporting the processed data to CSV
    print(f"Now creating csv file")
    normal_df.to_csv(normal_path, index=False)
    print(f"Time taken for creating csv file: {time.time() - end_time_V:.2f} seconds")

