## Overview of `AN_virtualization.ipynb`

This is the virtualization file that is responsible for the virtualization/expansion of the choices into their actual programs based on the candidates' details.

### Tasks done during virtualization : 

- Filtering out only the Andaman and Nicobar Islands students(Students with state of domicile 'AN')
- Next, we merge the table of eligible candidates with the choice table.
- Then, we explode the choices on the basis of Category. Every category retains the same but for Category 3A and Category 3B, an additional Category 3(A+B) has to be added at the end.
- Further, we explode the choices into PwD and Non-PwD based on the students' details.
- Finally, a new virtual choice number is assigned and the virtual choices file is created.

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

- **`load_iprograms(filename)`**
   - This method is resposible for loading in all the institute programs from the IP Seats file and creating `Program` objects for each of them.

- **`load_programs(filename)`**
   - This method is resposible for loading in all the branch-category programs from the P Seats file and creating `Program` objects for each of them.

- **`load_candidates(filename)`**
   - This method is resposible for loading in all the candidates and creating `Candidate` objects for each of them.

- **`choiceReader(candidates, ch_df)`**
   - This is responsible for loading in all the choices of students into the candidates dictionary of objects.

- **`getRank(roll_no, program)`**
   - This is a utility function that returns the candidate's rank that has to be taken into consideration for that particular program.

- **`process_candidates()`**
   - This is the main function that performs the task of allocation of the candidates as per the DA algorithm with the tweak of using a stack instead of a queue.
   - First, it checks if the current choice of the candidate in their preference list is a DS preference or not. Based on the type it performs one of the 2 following tasks : 
      - If DS Program : It adds the candidate to the institute's DS quota if the IIT has lesser than 2 DS students filled or it replaces a worse rank candidate(if exists) from that institute's DS quota.
      - If non-DS Program : It allocates the seat to the candidate in accordance with the DA algorithm which has been implemented with some changes.

- **`getRank(roll_no, program)`**
   - This is a utility function responsible for getting the required type of rank based on the program.

- **`prioritizer()`**
   - This function is the function that gives the priorty to different candidates while allotting them seats by incresinf the rank of all the category-2 students by 10000000.

- **`remove_candidate_with_roll_number(waitlist, roll_number)`**
   - This is the method responsible for removing the candidate with the given roll number from the waitlists. This is mainly called in the allocator functions.

- **`checkAndAllocate(candidate, i, stream)`**
   - This function checks if the candidate has an i'th virtual choice. If present, the candidate's rank based on the stream is extracted. If the rank is positive and there is a vacant seat in both PSeat and IPSeat, the candidate is allocated the seat using add_candidate().

- **`allot3()`**
   - This method is responsible for allocation of candidates in order of their stream 3, or, JEE-Mains B.Tech marks. This parses through each candidate in increasing order of ranks(best rank to worst).
   - For each candidate, it is first checked if the candidate can be allocated a better program(if already allocated a program). If possible, the candidate is given that seat and this seat is vacated. If no better seat is available, the candidate retains the current seat, if present, or the program iterates through the rest of the candidate's choices and calls the checkAndAllocate() function.

- **`allot1()`**
   - This method is similar to the above one, but is responsible for stream 1, or, JEE-ARC based marks which are mainly for ARC(Architectural) courses.

- **`allot4()`**
   - This method is similar to the above 2, but is responsible for stream 4, or, board-based marks which are mainly for BPH or PHA courses.

- **`clearer()`**
   - This is the utility function that just clears out the unnecessary or redundant candidates which might've been missed out due to various reasons.

- **`Master for loop`**
   - This is the master loop that runs the same number of times as the number of candidates participating in the CSAB NEUT round for AN(Andaman and Nicobar state of domicile). This is a slight amount above the necessary since it can be proven mathematically that the entire process gets completed and no other seat shift happens after a smaller number of iterations.

## Data Output and Verification 

- The program generates a csv file with all the necessary details about the allocation of the candidates and their flags.

- It also generates a separate csv file that contains a list of all the unallocated candidates.

- Finally, the program compares the allocation with the allocation of an external source to verify its correctness.


