# NEUT Seat Allocation System

The **NEUT Seat Allocation System** is designed for the seat allocation process involving candidates from the North East and Union Territories (NEUT) of India. This system facilitates the allocation of seats in various educational programs based on candidates' ranks, categories, and preferences.

### About NEUT
- **Participating Regions:** The NEUT Seat Allocation System includes candidates from eight North Eastern states (Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Nagaland, Sikkim, and Tripura) 5 Union Territories of India(Andaman & Nicobar Islands, Daman & Diu, Dadar & Nagar Haveli, Lakhsadweep, Ladakh) and NERIST, Itanagar.
- **Eligibility:** Candidates from these regions are eligible to participate in the NEUT Seat Allocation System, provided they meet the required criteria set by their respective boards and institutions.

## Classes and Methods Overview

### 1. **Class `Program`**

- **Attributes:**
  - `board_id`: Board ID of the program.
  - `stream`: Stream ID of the program.
  - `quota`: Quota ID for the program.
  - `institute`: Institute ID offering the program.
  - `program`: Program ID.
  - `category`: Category ID.
  - `subcategory`: Subcategory ID.
  - `gender`: Gender ID.
  - `capacity`: Total seat capacity.
  - `waitlist`: List of candidates waiting for allocation (using a heap for efficient access).
  - `subCatAssign`: Dictionary to keep track of candidates assigned based on subcategories.

- **Methods:**
  - `add_candidate(rk, roll_no)`: Adds a candidate to the waitlist if their rank is valid.
  - `remove_least_preferred()`: Removes and returns the candidate with the lowest rank from the waitlist.

### 2. **Class `Candidate`**

- **Attributes:**
  - `board_id`: Board ID of the candidate.
  - `roll_no`: Roll number of the candidate.
  - `state_id`: State ID of the candidate.
  - `domicile_id`: Domicile ID.
  - `gender_id`: Gender ID.
  - `category_id`: Category ID.
  - `subcat_list`: List of subcategories the candidate belongs to.
  - `choice_list`: Dictionary of program choices made by the candidate.
  - `choice_list_mapper`: Maps choice index to choice number.
  - `current_index`: Current index for processing choices.
  - `max_index`: Maximum index for choices.
  - `rank01`, `rank03`, `boardRank`: Rank information based on different criteria.
  - `cAlloc`: Program the candidate is currently allocated to.

- **Methods:**
  - `extract_yes_numbers(subCategoryList)`: Extracts subcategory IDs where "Yes" is present from the subcategory list.
  - `load_candidates(filename)`: Loads candidates from a CSV file into a dictionary.

## Major Methods and Functionality

1. **Loading Data:**
   - `load_programs(filename)`: Loads program data from a CSV file and initializes `Program` objects.
   - `load_candidates(filename)`: Loads candidate data from a CSV file and initializes `Candidate` objects.
   - `choiceReader(candidates, ch_df)`: Updates candidates' choice lists based on data from the choice CSV file.

2. **Ranking and Prioritization:**
   - `prioritizer()`: Adjusts ranks of candidates based on domicile and subcategory conditions, sorting candidates by rank in different streams.
   - `getRank(roll_no, program)`: Retrieves the rank of a candidate based on the stream of the program.

3. **Allocation and Waitlist Management:**
   - `checker(candidate)`: Checks if a candidate can be allocated to a program based on rank and capacity constraints.
   - `alloter()`: Allocates candidates to programs based on their choices, ranks, and the available capacity of the programs. Handles waitlists and subcategory assignments.

4. **Verification and Output:**
   - `print_all_candidates(candidates)`: Prints details of all candidates.
   - `allotReader(all_df)`: Reads final allotment data from a CSV file to verify if allocations are correct and adjust candidate allocations if needed.

## Data Output and Verification

1. **Data Output:**
   - **Allocations:** The program writes the allocations to `Smolfinal_allocations.csv`, listing details such as roll number, program code, quota, category, subcategory, gender, rank, choice index, and virtual index.
   - **Unallocated Candidates:** It also writes unallocated candidates to `final_unallocated_candidates.csv`, listing roll numbers of candidates who couldn't be allocated to any program.

2. **Verification:**
   - **Initial Verification:** The `allotReader` function is used to verify if the allocations match the expected results based on external data. If discrepancies are found, the function updates allocations accordingly.
   - **Final Check:** After the main allocation logic, it prints out the remaining seats in each program and any discrepancies, ensuring that all candidates are processed and the allocations are accurate.

## Summary

- **Classes:** `Program` manages program details and waitlists; `Candidate` handles candidate details and choices.
- **Data Handling:** Data is loaded from CSV files, candidates' choices are processed, and ranks are adjusted.
- **Allocation Logic:** Candidates are allocated to programs based on their choices, ranks, and program capacities. Special handling is done for subcategories and domicile-based prioritization.
- **Output and Verification:** Final allocations are written to a CSV file, and unallocated candidates are listed. Verifications are performed to ensure data consistency and accuracy.
