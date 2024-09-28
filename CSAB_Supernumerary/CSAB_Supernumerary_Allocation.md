# Supernumerary CSAB Allocation Reader
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

## Code Snippet 2: File Paths

This section defines the paths to various CSV files used in the data processing pipeline.

### File Paths:
- `path_candidates`: Path to the file containing candidate data.
- `path_seats`: Path to the file containing seat information.
- `path_normChoices`: Path for the normal virtualized choices output.
- `path_dsChoices`: Path for the DS virtualized choices output.
- `path_choices`: Path to the file containing choices made by candidates.
- `path_allotment`: Path to the file containing allotment data.
- `path_output`: Path for the output file of allotments.
- `path_error`: Path for the output file of unalloted candidates.


## Code Snippet 3: Data Classes and Loading Functions

This section defines the classes `Program` and `Candidate`, along with functions to load data from CSV files into these classes.

### `Program` Class

The `Program` class represents an academic program and its attributes.

#### Attributes:
- `inst_code`: Institution code.
- `brcode`: Branch code.
- `quota`: Quota type.
- `cat`: Category (e.g., BC, GN, SC).
- `subcat`: Subcategory.
- `gender`: Gender specification.
- `capacity`: Capacity of the program.
- `ds`: Supernumerary seat designation.
- `min_cutoff`: Minimum cutoff rank for the program (default is 0).
- `round_no`: Round number (default is 1).
- `waitlist`: List of candidates waiting for the program.

#### Methods:
- `is_eligible(rk)`: Checks if the candidate’s rank is eligible for the program based on the round and minimum cutoff.
- `add_candidate(rk, roll_no)`: Adds a candidate to the waitlist if the rank is positive.
- `remove_least_preferred()`: Removes and returns the least preferred candidate from the waitlist.

### `Candidate` Class

The `Candidate` class represents a candidate with various ranks and attributes.

#### Attributes:
- `roll_no`: Roll number of the candidate.
- `current_index`: Current index in the choice list (default is 1).
- `max_index`: Maximum index in the choice list (default is 0).
- `choice_list`: Dictionary of choices made by the candidate.
- `choice_list_mapper`: Mapper for the choices.
- `isDS`: Supernumerary seat designation (1 if true, 0 otherwise).
- `prep`: Preparation status.
- Various rank attributes for different categories and programs.

### Functions

#### `load_candidates(filename)`

Loads candidate data from a CSV file into a dictionary of `Candidate` objects.

    
    def load_candidates(filename):
        df = pd.read_csv(filename)
        filtered_df = df.sort_values('Adv_CRL_Rank')
        filtered_df = filtered_df[filtered_df['Nationality'] != 4]
        return {row['RollNo']: Candidate(row['RollNo']
        ,row['AI_Eng_CRL_Rank']  
        ,row['AI_Eng_OBC_NCL_Rank']
        ,row['AI_Eng_SC_Rank']
        ,row['AI_Eng_ST_Rank']
        ,row['AI_Eng_EWS_Rank']
        ,row['AI_Eng_CRL_PD_Rank']
        ,row['AI_Eng_OBC_NCL_PD_Rank']
        ,row['AI_Eng_SC_PD_Rank']
        ,row['AI_Eng_ST_PD_Rank']
        ,row['AI_Eng_EWS_PD_Rank']
        ,row['AI_ARC_CRL_Rank']
        ,row['AI_ARC_OBC_NCL_Rank']
        ,row['AI_ARC_SC_Rank']
        ,row['AI_ARC_ST_Rank']
        ,row['AI_ARC_EWS_Rank']
        ,row['AI_ARC_CRL_PD_Rank']
        ,row['AI_ARC_OBC_NCL_PD_Rank']
        ,row['AI_ARC_SC_PD_Rank']
        ,row['AI_ARC_ST_PD_Rank']
        ,row['AI_ARC_EWS_PD_Rank']
        ,row['AI_Pln_CRL_Rank']
        ,row['AI_Pln_OBC_NCL_Rank']
        ,row['AI_Pln_SC_Rank']
        ,row['AI_Pln_ST_Rank']
        ,row['AI_Pln_EWS_Rank']
        ,row['AI_Pln_CRL_PD_Rank']
        ,row['AI_Pln_OBC_NCL_PD_Rank']
        ,row['AI_Pln_SC_PD_Rank']
        ,row['AI_Pln_ST_PD_Rank']
        ,row['AI_Pln_EWS_PD_Rank']
        ,row['Adv_CRL_Rank']
        ,row['Adv_OBC_NCL_Rank']
        ,row['Adv_SC_Rank']
        ,row['Adv_ST_Rank']
        ,row['Adv_EWS_Rank']
        ,row['Adv_CRL_PD_Rank']
        ,row['Adv_OBC_NCL_PD_Rank']
        ,row['Adv_SC_PD_Rank']
        ,row['Adv_ST_PD_Rank']
        ,row['Adv_EWS_PD_Rank']
        ,row['Adv_Prep_SC_Rank']
        ,row['Adv_Prep_ST_Rank']
        ,row['Adv_Prep_CRL_PD_Rank']
        ,row['Adv_Prep_OBC_NCL_PD_Rank']
        ,row['Adv_Prep_SC_PD_Rank']
        ,row['Adv_Prep_ST_PD_Rank']
        ,row['Adv_Prep_EWS_PD_Rank'], row['Adv_DS'], row['Adv_IsPrep']) for index, row in filtered_df.iterrows()}

### `load_programs(filename)`

This function loads program data from a CSV file into a dictionary of `Program` objects.

#### Parameters:
- `filename`: Path to the CSV file containing program data.

#### Returns:
- A dictionary where the key is a tuple `(inst_code, brcode, quota, cat, subcat, gender, 0)` and the value is an instance of the `Program` class.

#### Code:
    def load_programs(filename):
        df = pd.read_csv(filename)
        return {(row['InstCd'], row['BrCd'], row['Quota'], row['Cat'], row['SubCat'], row['Gender'], 0): Program(row['InstCd'], row['BrCd'], row['Quota'], row['Cat'], row['SubCat'], row['Gender'], row['TSeat'], 0) for index, row in df.iterrows()}

## Code Snippet 4:Process Choices into chunks

### `process_chunk(chunk)`

Processes a chunk of choice data and updates a local dictionary of candidates.

#### Parameters:
- `chunk`: A pandas DataFrame containing a portion of choice data.

#### Returns:
- A dictionary where:
  - The key is the candidate's roll number.
  - The value is a dictionary containing:
    - `'choice_list'`: A dictionary mapping virtual choice numbers to `Program` objects.
    - `'choice_list_mapper'`: A dictionary mapping virtual choice numbers to original choice numbers.
    - `'max_index'`: The total count of choices for the candidate.

#### Code:
    
    def process_chunk(chunk):
        local_candidates = {}
        for index, row in chunk.iterrows():
            roll_no = int(row['RollNo'])
            choice_no = row['ChoiceNo']
            v_choice_no = int(row['ChoiceNo_V'])
            inst_code = row['InstCode']
            brcode = row['Brcode']
            quota = row['State_quota_V']
            cat = row['Cat_V']
            subcat = row['SubCat_V']
            gender = row['Gender_V']
            if roll_no in candidates.keys():
                if roll_no not in local_candidates:
                    local_candidates[roll_no] = {'choice_list': {}, 'choice_list_mapper': {}, 'max_index': 0}
                program_key = (inst_code, brcode, quota, cat, subcat, gender, 0)
                program = programs.get(program_key)
                local_candidates[roll_no]['choice_list'][v_choice_no - 1] = program
                local_candidates[roll_no]['choice_list_mapper'][v_choice_no - 1] = choice_no
                local_candidates[roll_no]['max_index'] += 1
        return local_candidates

### `merge_results(results)`

Merges the results from processed chunks into the main `candidates` dictionary.

#### Parameters:
- `results`: A list of dictionaries, each representing processed data from chunks. Each dictionary maps candidate roll numbers to their respective choice data.

#### Code:
    
    def merge_results(results):
        for result in results:
            for roll_no, data in result.items():
                if roll_no in candidates:
                    candidates[roll_no].choice_list.update(data['choice_list'])
                    candidates[roll_no].choice_list_mapper.update(data['choice_list_mapper'])
                    candidates[roll_no].max_index += data['max_index']
### `load_choices_parallel(filename, chunk_size=500000)`

Loads and processes choice data from a CSV file in parallel.

#### Parameters:
- `filename` (str): The path to the CSV file containing choice data.
- `chunk_size` (int, optional): The number of rows per chunk to be processed. Default is 500,000.

#### Functionality:
1. **Read CSV in Chunks**: The CSV file is read in chunks of the specified size using `pd.read_csv()` with the `chunksize` parameter.
2. **Parallel Processing**: 
   - `ProcessPoolExecutor` is used to handle parallel processing of chunks.
   - Each chunk is submitted for processing using the `executor.submit()` method, which calls the `process_chunk` function.
3. **Collect Results**: 
   - Results from processed chunks are collected using `as_completed()` to handle futures.
   - Each result is appended to the `results` list.
4. **Merge Results**: Once all chunks have been processed, the `merge_results` function is called to integrate the processed data into the main `candidates` dataset.

#### Code:
    
    def load_choices_parallel(filename, chunk_size=500000):
        df = pd.read_csv(filename, chunksize=chunk_size)
        futures = []
        with ProcessPoolExecutor(max_workers=20) as executor:
            for chunk in df:
                futures.append(executor.submit(process_chunk, chunk))
            results = []
            for future in as_completed(futures):
                results.append(future.result())
        merge_results(results)


### Measuring Execution Time for Parallel Choice Loading

This code snippet measures the time taken to load choices from a CSV file using the `load_choices_parallel` function and prints the elapsed time.

    
    start_time = time.time()  # Record the start time
    load_choices_parallel(path_normChoices)  # Call the function to load choices in parallel
    end_time = time.time()  # Record the end time

    elapsed_time = end_time - start_time  # Calculate elapsed time
    print(f"Time taken for loading choices in parallel: {elapsed_time:.2f} seconds")  # Print the elapsed time
    print("The tough part is done.")  # Print a completion message

