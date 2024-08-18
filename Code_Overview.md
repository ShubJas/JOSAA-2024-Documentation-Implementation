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
