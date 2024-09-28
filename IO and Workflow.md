# Notebooks Overview

This documentation provides an overview of the sequence of notebooks used in the JoSAA allocation process, including the inputs, outputs, and the purpose of each notebook across different rounds.

## Round 1: Notebooks Overview

| Notebook Name                | Inputs                                     | Outputs                               | Description                                                                        |
|------------------------------|--------------------------------------------|---------------------------------------|------------------------------------------------------------------------------------|
| **merit_extended.py**         | Candidate.csv                              | Extended_merit_list1.csv              | Generates an extended merit list.                                                  |
| **virtualization.ipynb**      | Candidate.csv, Choice.csv, Seats.csv, Institutes.csv       | Normal_Virtualized_Choices_R1.csv, DS_Virtualized_Choices_R1.csv, candidate_choice_merge_R1.csv | Virtualizes the choices.                                                           |
| **allocationReader.ipynb**    | Candidates.csv, Seats_Foreign.csv, Normal_Virtualized_Choices.csv, Extended_merit_list1.csv, Seats.csv, allotment_NIC.csv | final_unallocated_candidates.csv, final_final_allocations.csv | Performs allocation and generates final lists.                                     |
| **mismatches.ipynb**          | allotment_NIC.csv, final_final_allocations.csv | mismatched_allocations_analysis.txt  | Analyzes mismatches between initial allotments and final allocations.              |

## Rounds 2-5: Notebooks Overview

The process for Rounds 2-5 is similar, with slight modifications to the inputs and outputs to accommodate the progressing rounds.

| Notebook Name                | Inputs                                        | Outputs                              | Description                                                                 |
|------------------------------|-----------------------------------------------|--------------------------------------|-----------------------------------------------------------------------------|
| **merit_extended.py**         | Candidate.csv                                 | Extended_merit_list.csv              | Generates an extended merit list.                                           |
| **virtualization.ipynb**      | Candidate.csv, Choice.csv, Seats.csv          | Normal_Virtualized_Choices_Rx.csv, DS_Virtualized_Choices_Rx.csv (X = 2 to 5) | Virtualizes the choices for the respective round.                            |
| **allocationReader.ipynb**    | Candidates.csv, Seats_Foreign.csv, Normal_Virtualized_Choices_Rx.csv, DS_Virtualized_Choices_Rx.csv, Extended_merit_list.csv, Seats.csv, allotment_NIC.csv, prev_allotment.csv or RX_Allotment.csv (X = 2 to 5) | final_unallocated_candidates.csv, final_final_allocations.csv  | Performs allocation for the respective round.                                  |
| **mismatches.ipynb**          | allotment_NIC.csv, final_final_allocations.csv  | mismatched_allocations_analysis.txt | Analyzes mismatches between allotments and final allocations for each round. |

## CSAB SPECIAL ROUNDS: Notebooks Overview

The process for Special Rounds is similar, with slight modifications to the inputs and outputs to accommodate the progressing rounds.

| Notebook Name                | Inputs                                        | Outputs                              | Description                                                                 |
|------------------------------|-----------------------------------------------|--------------------------------------|-----------------------------------------------------------------------------|
| **virtualization_csX.ipynb**      | Candidate.csv, Choices_NIC.csv, Seats.csv          | Normal_Virtualized_Choices_Rx.csv | Virtualizes the choices for the respective round.                            |
| **allocationReader_csX.ipynb**    | Candidates.csv, Normal_Virtualized_Choices_Rx.csv, Seats.csv, allotment_NIC.csv, prev_allotment.csv or RX_Allotment.csv  | final_unallocated_candidates.csv, final_final_allocations.csv  | Performs allocation for the respective round.                                  |
| **mismatches.ipynb**          | allotment_NIC.csv, final_final_allocations.csv  | mismatched_allocations_analysis.txt | Analyzes mismatches between allotments and final allocations for each round. |

## CSAB NEUT: Notebooks Overview

The process for NEUT is similar, with slight modifications to the inputs and outputs to accommodate the progressing rounds.

| Notebook Name                | Inputs                                        | Outputs                              | Description                                                                 |
|------------------------------|-----------------------------------------------|--------------------------------------|-----------------------------------------------------------------------------|
| **virtualization_cs_cons.ipynb**      | Candidate.csv, Choices_NIC.csv, Seats.csv          | Normal_Virtualized_Choices_Rx.csv (X = 2 to 5) | Virtualizes the choices for the respective round.                            |
| **reader.ipynb**    | VirtualizedChoices1.csv, R1_App_Seats.csv, R1_App_RankDetail.csv, R1_App_CandidateProfile.csv, R1_App_QualificationMarksDetail.csv, NEUT_Official_1.csv | final_unallocated_candidates.csv, Smolfinal_allocations.csv  | Performs allocation for the respective round.                                  |
| **mismatches.ipynb**          | NEUT_Official_1.csv, Smolfinal_allocations.csv  | mismatched_allocations_analysis.txt | Analyzes mismatches between allotments and final allocations for each round. |
| **AN_reader.ipynb**      | AN_Virtualized_Choices.csv, R1_App_Seats.csv, R1_App_RankDetail.csv, R1_App_CandidateProfile.csv, R1_App_QualificationMarksDetail.csv, CSAB_NITK_AndamanIPSeat_new.csv, CSAB_NITK_AndamanPSeat_new.csv       | AN_Final_allocationsLinear.csv | Performs allotment for NEUT Andaman only round 1.                            |
| **AN_virtualization.ipynb**      | R1_App_CandidateProfile.csv, R1_App_Choice.csv        | AN_Virtualized_Choices.csv | Virtualizes the choices for the respective round.                          |

## Workflow Summary

### Round 1
1. **merit_extended.py**: 
   - Generates an extended merit list.
   
2. **virtualization.ipynb**:
   - Virtualizes choices based on the merit list, candidate choices, and seats.
   
3. **allocationReader.ipynb**:
   - Allocates seats and produces final lists of allocated and unallocated candidates.
   
4. **mismatches.ipynb**:
   - Analyzes and reports mismatches between initial and final allocations.

### Rounds 2-5
1. **merit_extended.py**: 
   - Generates an extended merit list for each round.
   
2. **virtualization.ipynb**:
   - Virtualizes choices for each round.
   
3. **allocationReader.ipynb**:
   - Allocates seats for each round.
   
4. **mismatches.ipynb**:
   - Analyzes mismatches for each respective round.

### CSAB SPECIAL ROUNDS
1. **virtualization_csX.ipynb**:
   -Virtualizes choices for each round.

2. **allocationReader_csX.ipynb**
   -Allocates seats for each round.
   
3. **mismatches.ipynb**
   -Analyzes mismatches for each respective round.

### CSAB NEUT
1. **virtualization_cs_cons.ipynb**:
   -Virtualizes choices for each round.

2. **reader.ipynb**:
   -Allocates seats for each round.
   
3. **mismatches.ipynb**:
   -Analyzes mismatches for each respective round.

4. **AN_reader.ipynb**:
   -Allocates seats only for Andaman & Nicobar Islands .

5. **AN_virtualization.ipynb**:
   - Virtualizes choices only for Andaman & Nicobar Islands.
   
## Notes
- Ensure input files are placed in the correct directories before running each notebook.
- The output files will be generated in the same directories as the respective notebooks.
- Review `mismatched_allocations_analysis.txt` for any discrepancies in the allocation process.
