#  Discrepancies Due to Changes in `choices.csv` and `choices_NIC.csv`

This document explains the discrepancies encountered during the CSAB Special Rounds allocation process due to variations between `choices.csv` and `choices_NIC.csv`, and the steps taken to resolve these issues.

### Background

According to the established business rules, a candidate who confirmed a seat in the JoSAA allocation must retain that seat if they participate in the CSAB Special Round unless they are allocated a more preferred seat during the Special Round. This rule ensures that candidates will not lose their previously confirmed seat unless they are upgraded to a better one.

To ensure compliance with this rule, during the CSAB Special Round, the candidate's confirmed JoSAA seat is appended to their new CSAB choice list if they were previously allocated a seat in JoSAA.

### Issue in the 2024 Allocation Cycle

In the 2024 cycle, a new scenario introduced complications:
- **Manual Entry of Confirmed JoSAA Seat:** Candidates were allowed to manually re-enter their previously confirmed JoSAA seat in their choice list for the CSAB Special Round. 
- **Discrepancy:** This led to discrepancies between the NIC-provided raw choice data (`choices.csv`) and the processed data (`choices_NIC.csv`), which contained the appended confirmed seat. The inconsistency arose when some candidates manually added their JoSAA confirmed seat, and thus their seat was not appended again by the system, while for others, the seat was appended automatically.

### The Problem Stemmed from Two Different Scenarios:

1. **Raw Data (`choices.csv`):** The NIC-provided raw choices list included candidates who manually re-entered their previously confirmed JoSAA seat into their choice list.

2. **Processed Data (`choices_NIC.csv`):** In contrast, the processed choices list, which was supposed to append the confirmed JoSAA seat to the end of the candidates' choices, did not append this seat for those candidates who had already manually added it to their new list. This resulted in an inconsistency where some candidates had their JoSAA seat appended twice, while others had it only once.

### Resolution Strategy

To address this, we adhered strictly to the business rules. The allocation logic was designed such that whenever a candidate encountered their previously confirmed JoSAA seat in their choice list during the allocation process, they were automatically allotted that seat, regardless of where it appeared in their list of preferences. This rule was enforced consistently to prevent any candidate from losing their previously confirmed seat unless a higher-preference seat was available.

By following this logic, we ensured that candidates who had manually added their confirmed JoSAA seat to their new choices did not experience any disadvantage or confusion during the allocation process. Their previously confirmed seat was treated with the same priority as in previous years, guaranteeing fairness and adherence to the established rules.
