## Overview of `merit_extended.py`

In JEE Advanced, candidates who do not initially qualify for admission under their respective categories but are still eligible for a preparatory course are assigned preparatory ranks. These preparatory candidates are given a special rank list to facilitate their admission in subsequent rounds if they meet certain criteria.

The goal of the `merit_extended.py` code is to integrate these preparatory candidates into the main merit list by extending their ranks accordingly. Here’s how this is accomplished:

1. **Reading the Input Data**:
   - The code starts by reading the existing merit list from a CSV file into a pandas DataFrame. This list includes both regular candidates and those eligible for the preparatory course.

2. **Identifying Preparatory Candidates**:
   - The code identifies candidates eligible for the preparatory course using a specific column (`Adv_IsPrep`). This column flags candidates who are part of the preparatory list.

3. **Determining Last Ranks**:
   - The code calculates the highest (last) rank in each merit list column to understand the current state of ranks before integration.

4. **Extending Ranks**:
   - For each preparatory candidate, the code retrieves their preparatory rank from columns designated for preparatory ranks (e.g., `Adv_Prep_CRL_PD_Rank`, `Adv_Prep_OBC_NCL_PD_Rank`).
   - It then updates the main merit list ranks by adding the preparatory ranks to the maximum ranks of the corresponding regular rank columns. This effectively places the preparatory candidates into the main merit list at appropriate positions.

5. **Saving the Updated List**:
   - After extending the ranks, the updated DataFrame, which now includes the preparatory candidates integrated into the main merit list, is saved to a new CSV file.

This process ensures that preparatory candidates are appropriately ranked in the main merit list, reflecting their eligibility and extending their consideration for admission based on their preparatory ranks.


---

## Overview of `allocationReader.py`

This file contains the implementation of the Core Deferred Acceptance Algorithm (DA) algorithm responsible for the allocation process. It handles the logic for distributing candidates based on their ranks and preferences.


## Reading the Input Data

### `Extended_merit_list1.csv`

- **Description**: This file contains detailed information about candidates. It includes ranks across various categories and preparation modes, as well as flags indicating specific attributes of the candidates.
- **Source**: This file is generated as the output of the `merit_extended.py` script.
- **Purpose**: It is used to create `Candidate` objects with comprehensive rank data for processing and admission decisions.

### `Seats.csv`

- **Description**: This file provides information about available programs, including their codes, quotas, categories, subcategories, gender classifications, and total capacities.
- **Source**: This file is provided by the NIC.
- **Purpose**: It is used to create `Program` objects, which include details about each program's availability and capacity, essential for managing the admission process.


### Class: `Program`

Represents a program with specific attributes and operations related to candidates and quotas.

---

### Class: `Candidate`

Represents a candidate with various ranks across different categories and his choice list.

---

## Methods of `Program` :

- **`__init__(...)`**
  - **Purpose**: Initializes a new `Program` object.

- **`is_eligible(rk)`**
  - **Purpose**: Checks if a candidate is eligible based on their rank (`rk`) and the current round number. If the round number is 1, all candidates are considered eligible. For other rounds, eligibility is determined by comparing the candidate's rank with the minimum cutoff.

- **`add_candidate(rk, roll_no)`**
  - **Purpose**: Adds a candidate to the waitlist if their rank (`rk`) is greater than 0. Candidates are stored in a max-heap where higher ranks are prioritized.

- **`remove_least_preferred()`**
  - **Purpose**: Removes and returns the candidate with the least preferred rank (i.e., the highest rank number) from the waitlist.


## Major Tasks/Methods across the Program :

- **`load_candidates(filename)`**
   - This method is resposible for loading in all the candidates and creating `Candidate` objects for each of them.

- **`load_programs(filename)`**
   - This method is resposible for loading in all the programs and creating `Program` objects for each of them.

- **`load_allotment(filename)`**
   - This method is responsible for assigning the previously allocated programs to the candidates.

- **`Cutoff Generation Loop`**
   - This loop takes the least rank(highest numerical value) and assigns it as the min_cut off for each program.

- **`load_choices_parallel(filename, chunk_size)`**
   - This is responsible for :
      - loading the file
      - splitting it into chunks of specified size
      - call the function process_chunk on each chunk and assign its execution to threads to parellize the entire process of loading all the normal choices.
   - Choices here are loaded in parallel since there are around 2.8 crore raw choices and around 8 crore virtualized choices. To load these linearly would take a lot of time, and thus the task is parellized.

- **`ds_load_choices_parallel(filename, chunk_size)`**
   - This is responsible for loading all the ds choices from the virtualized choices. This is similar to the previous function, but has the major difference that the programs are DS programs and have the tag 1 for is_DS.

- **`getRank(roll_no, program)`**
   - This is a utility function that returns the candidate's rank that has to be taken into consideration for that particular program.

- **`process_candidates()`**
   - This is the main function that performs the task of allocation of the candidates as per the DA algorithm with the tweak of using a stack instead of a queue.
   - First, it checks if the current choice of the candidate in their preference list is a DS preference or not. Based on the type it performs one of the 2 following tasks : 
      - If DS Program : It adds the candidate to the institute's DS quota if the IIT has lesser than 2 DS students filled or it replaces a worse rank candidate(if exists) from that institute's DS quota.
      - If non-DS Program : It allocates the seat to the candidate in accordance with the DA algorithm which has been implemented with some changes.

- **`(Not a method)Seat Reallocation Loop`**
   - This loop reallocates all the empty seats in IIT-'PH' programs to their NO counterparts.

- **`ENDresetter()`**
   - This function clears waitlists of all the programs and sets the current index of each candidate to 1, the beginning index.

- **`load_fcandidates(filename)`**
   - This method is resposible for loading in all the foreign candidates (Nationality 4) and creating `Candidate` objects for each of them.

- **`load_fprograms(filename)`**
   - This method is resposible for loading in all the foreign programs and creating `Program` objects for each of them.

- **`fload_choices_parallel(filename, chunk_size)`**
   - This method performs the same functionalities as `load_choices_parallel(filename, chunk_size)` but for foreign candidates only.

- **`getForeignRank(roll_no, program)`**
   - This is the utility function that is the foreign counterpart of the function `getRank(roll_no, program)`.

- **`f_process_candidates()`**
   - This is similar to the function `process_candidates()` but doesn't have the DS differentiation since foreign candidates are mutually exclusive with DS candidates.

## Data Output and Verification 

- The program generates a csv file with all the necessary details about the allocation of the candidates and their flags.

- It also generates a separate csv file that contains a list of all the unallocated candidates.

- Finally, the program compares the allocation with the allocation of an external source to verify its correctness.


