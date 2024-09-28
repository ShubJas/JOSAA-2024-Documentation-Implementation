## Overview of `virtualization_cs_cons.ipynb`

This is the virtualization file that is responsible for the virtualization/expansion of the choices into their actual programs based on the candidates' details.

### Tasks done during virtualization : 

- Filtering the NEUT students and removing the candidates with a domicile of '01' which is Andaman and Nicobar Islands.
- Next, we merge the table of eligible candidates with the choice table.
- Then, we explode the choices on the basis of domicile (additional domicile exploding is required for NERIST).
- After that, we explode the choices on the basis of Category. Each domicile has its own rules for category exploding.
- Further, we explode the choices into PwD and Non-PwD based on the students' details.
- Post that, we explode the choices based on the student's gender.
- Finally, a new virtual choice number is assigned and the virtual choices file is created.
- Additionally, we remove the choices which don't have a program or have a program with 0 seats pointed by them.

## Overview of `allocationReader.py`

This file contains the implementation of the an iterative algorithm responsible for the allocation process. It handles the logic for distributing candidates based on their ranks and preferences.

## Reading the Input Data

### Class: `Program`

Represents a program with specific attributes and operations related to candidates and quotas.

---

### Class: `Candidate`

Represents a candidate with various ranks across different categories and his choice list.

---

## Methods of `Program` :

- **`__init__(...)`**
  - **Purpose**: Initializes a new `Program` object.

- **`add_candidate(rk, roll_no)`**
  - **Purpose**: Adds a candidate to the waitlist if their rank (`rk`) is greater than 0. Candidates are stored in a max-heap where higher ranks are prioritized.

- **`remove_least_preferred()`**
  - **Purpose**: Removes and returns the candidate with the least preferred rank (i.e., the highest rank number) from the waitlist.


## Major Tasks/Methods across the Program :

- **`load_programs(filename)`**
   - This method is resposible for loading in all the programs from the  Seats file and creating `Program` objects for each of them.

- **`extract_yes_numbers(subCategoryList)`**
   - This is a utility function that is responsible for extracting the extra sub-categories each student is eligible to. This is mainly useful for Nagaland.

- **`load_candidates(filename)`**
   - This method is resposible for loading in all the candidates and creating `Candidate` objects for each of them.

- **`choiceReader(candidates, ch_df)`**
   - This is responsible for loading in all the choices of students into the candidates dictionary of objects.

- **`(NOT a Function)A section of code assign Board Rank`**
   - This is to custom assign the board rank to students by sorting the candidates based on their  BoardPercentage,Date of Birth and Roll Number.

- **`process_candidates()`**
   - This is the main function that performs the task of allocation of the candidates as per the DA algorithm with the tweak of using a stack instead of a queue.
   - First, it checks if the current choice of the candidate in their preference list is a DS preference or not. Based on the type it performs one of the 2 following tasks : 
      - If DS Program : It adds the candidate to the institute's DS quota if the IIT has lesser than 2 DS students filled or it replaces a worse rank candidate(if exists) from that institute's DS quota.
      - If non-DS Program : It allocates the seat to the candidate in accordance with the DA algorithm which has been implemented with some changes.

- **`getRank(roll_no, program)`**
   - This is a utility function responsible for getting the required type of rank based on the program.

- **`prioritizer()`**
   - This function is the function that gives the priorty to different candidates while allotting them seats by increasing the rank of students by 10000000 hence giving category 25, 26, 27, 28 priorities in that order for domicile-IDs 8 and 9.

- **`remove_candidate_with_roll_number(waitlist, roll_number)`**
   - This is the method responsible for removing the candidate with the given roll number from the waitlists. This is mainly called in the allocator functions.

- **`checker(candidate)`**
   - This function checks if the candidate can get any seat better than their current preference index and returns a boolean for the same.

- **`alloter()`**
   - This method is responsible for allocation of candidates utilizing the standard Deferred Acceptance algorithm(DA) with additional implementation of the checker function and a condition to allow only one candidate of a subcategory to get a seat in Nagaland's category 41.

- **`(NOT a Function)Master loop`**
   - This loop reruns the alloter function to maximize the allotment correctness of the students due to there being multiple streams from which students can be displaced and seats can become vacant.

## Data Output and Verification 

- The program generates a csv file with all the necessary details about the allocation of the candidates and their flags.

- It also generates a separate csv file that contains a list of all the unallocated candidates.

- Finally, the program compares the allocation with the allocation of an external source to verify its correctness.


