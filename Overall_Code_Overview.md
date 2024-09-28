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

## Methods:

- **`__init__(...)`**
  - **Purpose**: Initializes a new `Candidate` object with various ranks and attributes and flags.

- **`is_eligible(rk)`**
  - **Purpose**: Checks if a candidate is eligible based on their rank (`rk`) and the current round number. If the round number is 1, all candidates are considered eligible. For other rounds, eligibility is determined by comparing the candidate's rank with the minimum cutoff.

- **`add_candidate(rk, roll_no)`**
  - **Purpose**: Adds a candidate to the waitlist if their rank (`rk`) is greater than 0. Candidates are stored in a max-heap where higher ranks are prioritized.

- **`remove_least_preferred()`**
  - **Purpose**: Removes and returns the candidate with the least preferred rank (i.e., the highest rank number) from the waitlist.








