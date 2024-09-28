# Table Schemas Documentation

## Introduction
This document provides detailed documentation of the table schemas used in JoSAA/CSAB project. Each table is listed with its corresponding columns and a brief description.

## Table Documentation Overview

### General Information
The tables used in Round 1 are also used in all subsequent rounds. Each round builds upon the previous rounds by adding additional tables to capture more detailed information relevant to the allotment process.

### Tables Used in All Rounds
The following tables are common across all rounds:

1. **allotment_NIC.csv**
2. **Candidates.csv**
3. **Choice.csv**
4. **Extended_merit_list1.csv**
5. **Institutes.csv**
6. **Seats_Foreign.csv**
7. **Seats.csv**

### Additional Tables by Round

#### Round 2
- **prev_allotment.csv**: Includes allotment details from previous rounds.
- **RegistrationDetail.csv**: Contains registration and status details for candidates.

#### Round 3
- **ProgrammeStatistics_NIC.csv**: Provides statistical data about programs including rank details and seat capacities.
- **R3_Allotment.csv**: Consolidates allotment details from Rounds 1 and 2.

#### Round 4
- **R4_Allotment.csv**: Contains allotment details for Rounds 1, 2, and 3.

#### Round 5
- **R5_Allotment.csv**: Includes allotment details from Rounds 1, 2, 3, and 4.

Each round's additional tables provide extended data and insights, building on the foundational tables used in Round 1. This approach ensures a comprehensive view of allotments and candidate details throughout the entire process.


## Table Schemas For the common tables in all rounds
### 1. **allotment_NIC.csv**
   - **Description**: Stores allotment details for each candidate, including the round of allotment, candidate details, and the specific seat allotted.
   - **Columns**:
     - `RoundNo`: Allotment round number.
     - `Rollno`: Candidate's roll number.
     - `Birth_Cat`: Candidate's birth category.
     - `Rank`: Candidate's rank.
     - `Optno`: Option number representing the candidate's preference.
     - `Instcd`: Institute code of the allotted seat.
     - `Brcd`: Branch code of the allotted seat.
     - `AllottedCat`: Category under which the seat is allotted.
     - `AllottedQuota`: Quota under which the seat is allotted.
     - `AllottedGender`: Gender-specific allotment.
     - `Flag`: Indicates any special flags or markers related to the allotment.
     - `SupNumReason`: Reason for any supplementary number assigned.
     - `WithDraw`: Indicates if the candidate has withdrawn.
     - `RStatus`: Registration status.
     - `SStatus`: Seat status.
     - `Status`: Overall status of the allotment.
     - `ADate`: Allotment date.
     - `PIStatus`: Physical reporting status.
      


### 2. **Candidates.csv**
   - **Description**: Contains detailed information about candidates.
   - **Columns**:
     - `RollNo`: Candidate's roll number.
     - `SCode`: Subject code.
     - `Gender`: Candidate's gender.
     - `CAT`: Candidate's category.
     - `PwD`: Whether the candidate has a disability (Person with Disability).
     - `Nationality`: Candidate's nationality.
     - `AI_Eng_CRL_Rank`: All India Engineering Common Rank List rank.
     - `AI_Eng_OBC_NCL_Rank`: All India Engineering OBC NCL rank.
     - `AI_Eng_SC_Rank`: All India Engineering SC rank.
     - `AI_Eng_ST_Rank`: All India Engineering ST rank.
     - `AI_Eng_EWS_Rank`: All India Engineering EWS rank.
     - `AI_Eng_CRL_PD_Rank`: All India Engineering CRL PD rank.
     - `AI_Eng_OBC_NCL_PD_Rank`: All India Engineering OBC NCL PD rank.
     - `AI_Eng_SC_PD_Rank`: All India Engineering SC PD rank.
     - `AI_Eng_ST_PD_Rank`: All India Engineering ST PD rank.
     - `AI_Eng_EWS_PD_Rank`: All India Engineering EWS PD rank.
     - `AI_ARC_CRL_Rank`: All India Architecture Common Rank List rank.
     - `AI_ARC_OBC_NCL_Rank`: All India Architecture OBC NCL rank.
     - `AI_ARC_SC_Rank`: All India Architecture SC rank.
     - `AI_ARC_ST_Rank`: All India Architecture ST rank.
     - `AI_ARC_EWS_Rank`: All India Architecture EWS rank.
     - `AI_ARC_CRL_PD_Rank`: All India Architecture CRL PD rank.
     - `AI_ARC_OBC_NCL_PD_Rank`: All India Architecture OBC NCL PD rank.
     - `AI_ARC_SC_PD_Rank`: All India Architecture SC PD rank.
     - `AI_ARC_ST_PD_Rank`: All India Architecture ST PD rank.
     - `AI_ARC_EWS_PD_Rank`: All India Architecture EWS PD rank.
     - `AI_Pln_CRL_Rank`: All India Planning Common Rank List rank.
     - `AI_Pln_OBC_NCL_Rank`: All India Planning OBC NCL rank.
     - `AI_Pln_SC_Rank`: All India Planning SC rank.
     - `AI_Pln_ST_Rank`: All India Planning ST rank.
     - `AI_Pln_EWS_Rank`: All India Planning EWS rank.
     - `AI_Pln_CRL_PD_Rank`: All India Planning CRL PD rank.
     - `AI_Pln_OBC_NCL_PD_Rank`: All India Planning OBC NCL PD rank.
     - `AI_Pln_SC_PD_Rank`: All India Planning SC PD rank.
     - `AI_Pln_ST_PD_Rank`: All India Planning ST PD rank.
     - `AI_Pln_EWS_PD_Rank`: All India Planning EWS PD rank.
     - `Adv_CRL_Rank`: Advanced Common Rank List rank.
     - `Adv_OBC_NCL_Rank`: Advanced OBC NCL rank.
     - `Adv_SC_Rank`: Advanced SC rank.
     - `Adv_ST_Rank`: Advanced ST rank.
     - `Adv_EWS_Rank`: Advanced EWS rank.
     - `Adv_CRL_PD_Rank`: Advanced CRL PD rank.
     - `Adv_OBC_NCL_PD_Rank`: Advanced OBC NCL PD rank.
     - `Adv_SC_PD_Rank`: Advanced SC PD rank.
     - `Adv_ST_PD_Rank`: Advanced ST PD rank.
     - `Adv_EWS_PD_Rank`: Advanced EWS PD rank.
     - `Adv_IsPrep`: Whether the candidate is eligible for preparatory course.
     - `Adv_Prep_SC_Rank`: Advanced Preparatory SC rank.
     - `Adv_Prep_ST_Rank`: Advanced Preparatory ST rank.
     - `Adv_Prep_CRL_PD_Rank`: Advanced Preparatory CRL PD rank.
     - `Adv_Prep_OBC_NCL_PD_Rank`: Advanced Preparatory OBC NCL PD rank.
     - `Adv_Prep_SC_PD_Rank`: Advanced Preparatory SC PD rank.
     - `Adv_Prep_ST_PD_Rank`: Advanced Preparatory ST PD rank.
     - `Adv_Prep_EWS_PD_Rank`: Advanced Preparatory EWS PD rank.
     - `Adv_DS`: Defense Service status.
     - `Decision`: Final decision regarding the candidate's application.



 ### 3. **Extended_merit_list1.csv**
   - **Description**: Contains detailed information about candidates who are part of the extended merit list.
   - **Columns**:
     - `RollNo`: Candidate's roll number.
     - `StateCode`: Code representing the candidate's state.
     - `Gender`: Candidate's gender.
     - `Cat`: Candidate's category.
     - `SubCat`: Candidate's subcategory.
     - `Nationality`: Candidate's nationality.
     - `AI_Eng_CRL_Rank`: All India Engineering Common Rank List rank.
     - `AI_Eng_OBC_NCL_Rank`: All India Engineering OBC NCL rank.
     - `AI_Eng_SC_Rank`: All India Engineering SC rank.
     - `AI_Eng_ST_Rank`: All India Engineering ST rank.
     - `AI_Eng_EWS_Rank`: All India Engineering EWS rank.
     - `AI_Eng_CRL_PD_Rank`: All India Engineering CRL PD rank.
     - `AI_Eng_OBC_NCL_PD_Rank`: All India Engineering OBC NCL PD rank.
     - `AI_Eng_SC_PD_Rank`: All India Engineering SC PD rank.
     - `AI_Eng_ST_PD_Rank`: All India Engineering ST PD rank.
     - `AI_Eng_EWS_PD_Rank`: All India Engineering EWS PD rank.
     - `AI_ARC_CRL_Rank`: All India Architecture Common Rank List rank.
     - `AI_ARC_OBC_NCL_Rank`: All India Architecture OBC NCL rank.
     - `AI_ARC_SC_Rank`: All India Architecture SC rank.
     - `AI_ARC_ST_Rank`: All India Architecture ST rank.
     - `AI_ARC_EWS_Rank`: All India Architecture EWS rank.
     - `AI_ARC_CRL_PD_Rank`: All India Architecture CRL PD rank.
     - `AI_ARC_OBC_NCL_PD_Rank`: All India Architecture OBC NCL PD rank.
     - `AI_ARC_SC_PD_Rank`: All India Architecture SC PD rank.
     - `AI_ARC_ST_PD_Rank`: All India Architecture ST PD rank.
     - `AI_ARC_EWS_PD_Rank`: All India Architecture EWS PD rank.
     - `AI_Pln_CRL_Rank`: All India Planning Common Rank List rank.
     - `AI_Pln_OBC_NCL_Rank`: All India Planning OBC NCL rank.
     - `AI_Pln_SC_Rank`: All India Planning SC rank.
     - `AI_Pln_ST_Rank`: All India Planning ST rank.
     - `AI_Pln_EWS_Rank`: All India Planning EWS rank.
     - `AI_Pln_CRL_PD_Rank`: All India Planning CRL PD rank.
     - `AI_Pln_OBC_NCL_PD_Rank`: All India Planning OBC NCL PD rank.
     - `AI_Pln_SC_PD_Rank`: All India Planning SC PD rank.
     - `AI_Pln_ST_PD_Rank`: All India Planning ST PD rank.
     - `AI_Pln_EWS_PD_Rank`: All India Planning EWS PD rank.
     - `Adv_CRL_Rank`: Advanced Common Rank List rank.
     - `Adv_OBC_NCL_Rank`: Advanced OBC NCL rank.
     - `Adv_SC_Rank`: Advanced SC rank.
     - `Adv_ST_Rank`: Advanced ST rank.
     - `Adv_EWS_Rank`: Advanced EWS rank.
     - `Adv_CRL_PD_Rank`: Advanced CRL PD rank.
     - `Adv_OBC_NCL_PD_Rank`: Advanced OBC NCL PD rank.
     - `Adv_SC_PD_Rank`: Advanced SC PD rank.
     - `Adv_ST_PD_Rank`: Advanced ST PD rank.
     - `Adv_EWS_PD_Rank`: Advanced EWS PD rank.
     - `Adv_IsPrep`: Whether the candidate is eligible for a preparatory course.
     - `Adv_Prep_SC_Rank`: Advanced Preparatory SC rank.
     - `Adv_Prep_ST_Rank`: Advanced Preparatory ST rank.
     - `Adv_Prep_CRL_PD_Rank`: Advanced Preparatory CRL PD rank.
     - `Adv_Prep_OBC_NCL_PD_Rank`: Advanced Preparatory OBC NCL PD rank.
     - `Adv_Prep_SC_PD_Rank`: Advanced Preparatory SC PD rank.
     - `Adv_Prep_ST_PD_Rank`: Advanced Preparatory ST PD rank.
     - `Adv_Prep_EWS_PD_Rank`: Advanced Preparatory EWS PD rank.
     - `Adv_DS`: Defense Service status.
     - `Decision`: Final decision regarding the candidate's application.

### 4. **Institutes.csv**
   - **Description**: Contains information about the institutes participating in the process.
   - **Columns**:
     - `InstCd`: Institute code.
     - `InstNm`: Full name of the institute.
     - `AbbrNm`: Abbreviated name of the institute.
     - `InstType`: Type of institute (e.g., government, private).
     - `SeatType`: Type of seat available at the institute (e.g., general, reserved).
     - `InstAdd`: Address of the institute.
     - `InstPhone`: Phone number of the institute.
     - `InstFax`: Fax number of the institute.
     - `InstWebSite`: Website URL of the institute.
     - `EmailId`: Primary email ID of the institute.
     - `EmailId1`: Secondary email ID of the institute.
     - `ContactPerson`: Name of the contact person at the institute.
     - `Designation`: Designation of the contact person.
     - `MobileNo`: Mobile number of the contact person.

### 5. **Seats_Foreign.csv**
   - **Description**: Contains information about the seats available for foreign students at various institutes.
   - **Columns**:
     - `Instcd`: Institute code.
     - `BrCd`: Branch code.
     - `totalseat`: Total number of seats available for foreign students.

### 6. **Seats.csv**
   - **Description**: Contains detailed information about the seat allocation across various categories, branches, and states.
   - **Columns**:
     - `Quota`: Quota type (e.g., General, SC, ST, OBC).
     - `InstCd`: Institute code.
     - `BrCd`: Branch code.
     - `Cat`: Category of the seat (e.g., General, OBC, SC, ST).
     - `SubCat`: Subcategory of the seat (if applicable).
     - `Gender`: Gender-specific seat allocation (e.g., Male, Female).
     - `StCd1`: State code 1.
     - `StCd2`: State code 2.
     - `StCd3`: State code 3.
     - `StCd4`: State code 4.
     - `StCd5`: State code 5.
     - `StCd6`: State code 6.
     - `StCd7`: State code 7.
     - `StCd8`: State code 8.
     - `StCd9`: State code 9.
     - `StCd10`: State code 10.
     - `TSeat`: Total number of seats.
### 7. **Choice.csv**
   - **Description**: Contains information about the choices made by candidates for institutes and branches.
   - **Columns**:
     - `Rollno`: Candidate's roll number.
     - `Optno`: Option number representing the candidate's preference order.
     - `Instcd`: Institute code corresponding to the choice.
     - `Brcd`: Branch code corresponding to the choice.
     - `Validity`: Indicates the validity of the choice (e.g., valid or invalid).


## Additional Tables for Round 2

#### 1. **prev_allotment.csv**
   - **Description**: Contains allotment details from previous rounds for each candidate.
   - **Columns**:
     - `RoundNo`: Allotment round number.
     - `Rollno`: Candidate's roll number.
     - `Birth_Cat`: Candidate's birth category.
     - `Rank`: Candidate's rank.
     - `Optno`: Option number representing the candidate's preference.
     - `Instcd`: Institute code of the allotted seat.
     - `Brcd`: Branch code of the allotted seat.
     - `AllottedCat`: Category under which the seat was allotted.
     - `AllottedQuota`: Quota under which the seat was allotted.
     - `AllottedGender`: Gender-specific allotment.
     - `Flag`: Indicates any special flags or markers related to the allotment.
     - `SupNumReason`: Reason for any supplementary number assigned.
     - `WithDraw`: Indicates if the candidate has withdrawn.
     - `RStatus`: Registration status.
     - `SStatus`: Seat status.
     - `Status`: Overall status of the allotment.
     - `ADate`: Allotment date.
     - `PIStatus`: Physical reporting status.

#### 2. **RegistrationDetail.csv**
   - **Description**: Contains detailed registration information for each candidate, including security questions, password details, and registration status.
   - **Columns**:
     - `Rollno`: Candidate's roll number.
     - `SecQues`: Security question set by the candidate.
     - `SecAns`: Answer to the security question.
     - `Pwdhash`: Hashed password of the candidate.
     - `CandStatusEng`: Status of the candidate in the engineering stream.
     - `CandStatusArc`: Status of the candidate in the architecture stream.
     - `CandStatusPln`: Status of the candidate in the planning stream.
     - `CandStatusAdv`: Status of the candidate in the advanced stream.
     - `IsPwDGenerated`: Indicates if a PwD (Person with Disability) status has been generated.
     - `PwDGeneratedAt`: Timestamp of when the PwD status was generated.
     - `PwDGenerationIp`: IP address from which the PwD status was generated.
     - `IsRegistered`: Indicates if the candidate is registered.
     - `RegTime`: Timestamp of registration.
     - `IsAllowedForCurrentRound`: Indicates if the candidate is allowed for the current round.
     - `Remarks`: Any additional remarks or notes.
     - `IpAdd`: IP address of the candidate's registration.


## Additional Tables for Round 3

#### 1. **ProgrammeStatistics_NIC.csv**
   - **Description**: Contains statistical information about the programs offered, including rank details, seat capacities, and special quotas.
   - **Columns**:
     - `Quota`: Quota category for the seats.
     - `Instcd`: Institute code.
     - `BrCd`: Branch code.
     - `VCategory`: Vertical category of the candidate.
     - `GenderPool`: Gender-based seat pool.
     - `OpeningRank`: Opening rank for the category.
     - `ClosingRank`: Closing rank for the category.
     - `MinCutOff`: Minimum cutoff rank.
     - `TotalAllotted`: Total number of seats allotted.
     - `InitCap`: Initial seat capacity.
     - `NewCap`: New seat capacity after modifications.
     - `DeReserveFrom`: Starting rank of de-reservation (if applicable).
     - `DeReserveTo`: Ending rank of de-reservation (if applicable).
     - `SuperNum`: Supernumerary seat count.
     - `DSCap`: Seat capacity for Defence Service (DS) candidates.

#### 2. **R3_Allotment.csv**
   - **Description**: Contains allotment details for both Round 1 and Round 2, consolidating the allotment information for candidates across both rounds.
   - **Columns**:
     - `RoundNo`: Allotment round number.
     - `Rollno`: Candidate's roll number.
     - `Birth_Cat`: Candidate's birth category.
     - `Rank`: Candidate's rank.
     - `Optno`: Option number representing the candidate's preference.
     - `Instcd`: Institute code of the allotted seat.
     - `Brcd`: Branch code of the allotted seat.
     - `AllottedCat`: Category under which the seat was allotted.
     - `AllottedQuota`: Quota under which the seat was allotted.
     - `AllottedGender`: Gender-specific allotment.
     - `Flag`: Indicates any special flags or markers related to the allotment.
     - `SupNumReason`: Reason for any supplementary number assigned.
     - `WithDraw`: Indicates if the candidate has withdrawn.
     - `RStatus`: Registration status.
     - `SStatus`: Seat status.
     - `Status`: Overall status of the allotment.

## Additional Tables for Round 4

#### 1. **R4_Allotment.csv**
   - **Description**: Contains allotment details from Rounds 1, 2, and 3, including comprehensive status information for candidates.
   - **Columns**:
     - `RoundNo`: Allotment round number.
     - `Rollno`: Candidate's roll number.
     - `Birth_Cat`: Candidate's birth category.
     - `Rank`: Candidate's rank.
     - `Optno`: Option number representing the candidate's preference.
     - `Instcd`: Institute code of the allotted seat.
     - `Brcd`: Branch code of the allotted seat.
     - `AllottedCat`: Category under which the seat is allotted.
     - `AllottedQuota`: Quota under which the seat is allotted.
     - `AllottedGender`: Gender category under which the seat is allotted.
     - `Flag`: Special flag or note associated with the allotment.
     - `SupNumReason`: Reason for any supplementary number associated with the allotment.
     - `WithDraw`: Withdrawal status of the candidate.
     - `RStatus`: Reporting status of the candidate.
     - `SStatus`: Seat status of the candidate.
     - `Status`: General status of the allotment.
     - `ADate`: Allotment date.
     - `PIStatus`: Personal interview status of the candidate.


## Additional Tables for Round 5

#### 1. **R5_Allotment.csv**
   - **Description**: Contains allotment details from Rounds 1, 2, 3, and 4, including comprehensive status information for candidates across all these rounds.
   - **Columns**:
     - `RoundNo`: Allotment round number.
     - `Rollno`: Candidate's roll number.
     - `Birth_Cat`: Candidate's birth category.
     - `Rank`: Candidate's rank.
     - `Optno`: Option number representing the candidate's preference.
     - `Instcd`: Institute code of the allotted seat.
     - `Brcd`: Branch code of the allotted seat.
     - `AllottedCat`: Category under which the seat is allotted.
     - `AllottedQuota`: Quota under which the seat is allotted.
     - `AllottedGender`: Gender category under which the seat is allotted.
     - `Flag`: Special flag or note associated with the allotment.
     - `SupNumReason`: Reason for any supplementary number associated with the allotment.
     - `WithDraw`: Withdrawal status of the candidate.
     - `RStatus`: Reporting status of the candidate.
     - `SStatus`: Seat status of the candidate.
     - `Status`: General status of the allotment.
     - `ADate`: Allotment date.
     - `PIStatus`: Personal interview status of the candidate.


## Comprehensive Field Values Across All Rounds

### 1. **allotment_NIC.csv**
   - **Description**: Stores allotment details for each candidate, including the round of allotment, candidate details, and the specific seat allotted.
   - **Columns**:
     - `RoundNo`: Allotment round number.
     - `Rollno`: Candidate's roll number.
     - `Birth_Cat`: Candidate's birth category.
       - **Values**:
         - `EW`: Economically Weaker Section.
         - `BC`: Other Backward Classes.
         - `GN`: General Category.
         - `ST`: Scheduled Tribes.
         - `SC`: Scheduled Castes.
     - `Rank`: Candidate's rank.
     - `Optno`: Option number representing the candidate's preference.
     - `Instcd`: Institute code of the allotted seat.
     - `Brcd`: Branch code of the allotted seat.
     - `AllottedCat`: Category under which the seat is allotted.
       - **Values**:
         - `SCNO`: Scheduled Castes (Non-PwD).
         - `STNO`: Scheduled Tribes (Non-PwD).
         - `EWNO`: Economically Weaker Section (Non-PwD).
         - `BCNO`: Other Backward Classes (Non-PwD).
         - `OPNO`: General Category (Non-PwD).
         - `SCPH`: Scheduled Castes (PwD).
         - `STPH`: Scheduled Tribes (PwD).
         - `EWPH`: Economically Weaker Section (PwD).
         - `BCPH`: Other Backward Classes (PwD).
         - `OPPH`: General Category (PwD).
     - `AllottedQuota`: Quota under which the seat is allotted.
       - **Values**:
         - `AI`: All India quota.
         - `HS`: Home State quota.
         - `OS`: Other State quota.
         - `GO`: Goa State quota.
         - `LA`: Laddak quota.
         - `JK`: Jammu & Kashmir quota.
     - `AllottedGender`: Gender-specific allotment.
       - **Values**:
         - `B`: Male.
         - `F`: Female.
     - `Flag`: Indicates any special flags or markers related to the allotment.
       - **Values**:
         - `N`: No flag.
         - `P`: Preparatory candidates.
         - `F`: Foreign candidates.
         - `D`: Defence candidates.
     - `SupNumReason`: Reason for any supplementary number assigned.
       - **Values**:
         - `NA`: No flag.
         - `MC`: Multiple Candidature.
         - `DS`: Defence Service.
         - `FR`: Foreign.
     - `WithDraw`: Indicates if the candidate has withdrawn.
       - **Values**:
         - `N`: Not withdrawn.
         - `Y`: Withdrawn.
     - `RStatus`: Registration status.
       - **Values**:
         - `RT`: Seat retained.
         - `DR`: Dual reporting.
         - `RU`: Retained and upgraded.
         - `RC`: Reported and seat cancelled.
         - `NR`: Not reported.
     - `SStatus`: Seat status.
       - **Values**:
         - `NULL`.
     - `Status`: Overall status of the allotment.
       - **Values**:
         - `ALLOTED`: Alloted Seats.
         - `CANCELLED`: Cancelled Seats.
         
     - `ADate`: Allotment date.
     - `PIStatus`: Physical reporting status.
       - **Values**:
         - `NULL`.

### 2. **Candidates.csv**
   - **Description**: Contains detailed information about candidates.
   - **Columns**:
     - `RollNo`: Candidate's roll number.
     - `SCode`: Subject code.
     - `Gender`: Candidate's gender.
       - **Values**:
         - `1`: Male.
         - `2`: Female.
         - `3`: Transgender.
     - `CAT`: Candidate's category.
       - **Values**:
         - `GN`: General Category.
         - `BC`: Other Backward Classes.
         - `EW`: Economically Weaker Section.
         - `SC`: Scheduled Castes.
         - `ST`: Scheduled Tribes.
     - `PwD`: Indicates if the candidate is a Person with Disability (PwD).
       - **Values**:
         - `1`: PwD candidate.
         - `2`: Non-PwD candidate.
     - `Nationality`: Candidate's nationality.
       - **Values**:
         - `1`: Indian.
         - `2`: OCI (Other Country Indian), PIO (People of Indian Origin).
         - `4`: Foreign.
     - `AI_Eng_CRL_Rank`: All India Engineering Common Rank List rank.
     - `AI_Eng_OBC_NCL_Rank`: All India Engineering OBC NCL rank.
     - `AI_Eng_SC_Rank`: All India Engineering SC rank.
     - `AI_Eng_ST_Rank`: All India Engineering ST rank.
     - `AI_Eng_EWS_Rank`: All India Engineering EWS rank.
     - `AI_Eng_CRL_PD_Rank`: All India Engineering CRL PD rank.
     - `AI_Eng_OBC_NCL_PD_Rank`: All India Engineering OBC NCL PD rank.
     - `AI_Eng_SC_PD_Rank`: All India Engineering SC PD rank.
     - `AI_Eng_ST_PD_Rank`: All India Engineering ST PD rank.
     - `AI_Eng_EWS_PD_Rank`: All India Engineering EWS PD rank.
     - `AI_ARC_CRL_Rank`: All India Architecture Common Rank List rank.
     - `AI_ARC_OBC_NCL_Rank`: All India Architecture OBC NCL rank.
     - `AI_ARC_SC_Rank`: All India Architecture SC rank.
     - `AI_ARC_ST_Rank`: All India Architecture ST rank.
     - `AI_ARC_EWS_Rank`: All India Architecture EWS rank.
     - `AI_ARC_CRL_PD_Rank`: All India Architecture CRL PD rank.
     - `AI_ARC_OBC_NCL_PD_Rank`: All India Architecture OBC NCL PD rank.
     - `AI_ARC_SC_PD_Rank`: All India Architecture SC PD rank.
     - `AI_ARC_ST_PD_Rank`: All India Architecture ST PD rank.
     - `AI_ARC_EWS_PD_Rank`: All India Architecture EWS PD rank.
     - `AI_Pln_CRL_Rank`: All India Planning Common Rank List rank.
     - `AI_Pln_OBC_NCL_Rank`: All India Planning OBC NCL rank.
     - `AI_Pln_SC_Rank`: All India Planning SC rank.
     - `AI_Pln_ST_Rank`: All India Planning ST rank.
     - `AI_Pln_EWS_Rank`: All India Planning EWS rank.
     - `AI_Pln_CRL_PD_Rank`: All India Planning CRL PD rank.
     - `AI_Pln_OBC_NCL_PD_Rank`: All India Planning OBC NCL PD rank.
     - `AI_Pln_SC_PD_Rank`: All India Planning SC PD rank.
     - `AI_Pln_ST_PD_Rank`: All India Planning ST PD rank.
     - `AI_Pln_EWS_PD_Rank`: All India Planning EWS PD rank.
     - `Adv_CRL_Rank`: Advanced Common Rank List rank.
     - `Adv_OBC_NCL_Rank`: Advanced OBC NCL rank.
     - `Adv_SC_Rank`: Advanced SC rank.
     - `Adv_ST_Rank`: Advanced ST rank.
     - `Adv_EWS_Rank`: Advanced EWS rank.
     - `Adv_CRL_PD_Rank`: Advanced CRL PD rank.
     - `Adv_OBC_NCL_PD_Rank`: Advanced OBC NCL PD rank.
     - `Adv_SC_PD_Rank`: Advanced SC PD rank.
     - `Adv_ST_PD_Rank`: Advanced ST PD rank.
     - `Adv_EWS_PD_Rank`: Advanced EWS PD rank.
     - `Adv_IsPrep`: Whether the candidate is eligible for preparatory course.
     - `Adv_Prep_SC_Rank`: Advanced Preparatory SC rank.
     - `Adv_Prep_ST_Rank`: Advanced Preparatory ST rank.
     - `Adv_Prep_CRL_PD_Rank`: Advanced Preparatory CRL PD rank.
     - `Adv_Prep_OBC_NCL_PD_Rank`: Advanced Preparatory OBC NCL PD rank.
     - `Adv_Prep_SC_PD_Rank`: Advanced Preparatory SC PD rank.
     - `Adv_Prep_ST_PD_Rank`: Advanced Preparatory ST PD rank.
     - `Adv_Prep_EWS_PD_Rank`: Advanced Preparatory EWS PD rank.
     - `Adv_DS`: Defense Service status.
     - `Decision`: Final decision regarding the candidate's application.
       - **Values**:
         - `SL`: Slide.
         - `FR`: Freeze.
         - `FL`: Float.
         - `EX`: Exit.


### 3. **Choice.csv**
   - **Description**: Contains information about the choices made by candidates for institutes and branches.
   - **Columns**:
     - `Rollno`: Candidate's roll number.
     - `Optno`: Option number representing the candidate's preference order.
     - `Instcd`: Institute code corresponding to the choice.
     - `Brcd`: Branch code corresponding to the choice.
     - `Validity`: Indicates the validity of the choice.
       - **Values**:
         - `NULL`: Valid choice.
         - `N`: Not valid.

### 4. **Institutes.csv**
   - **Description**: Contains information about the institutes participating in the process.
   - **Columns**:
     - `InstCd`: Institute code.
     - `InstNm`: Full name of the institute.
     - `AbbrNm`: Abbreviated name of the institute.
     - `InstType`: Type of institute.
       - **Values**:
         - `IIT`: Indian Institute of Technology.
         - `NIT`: National Institute of Technology.
         - `3IT`: Triple IT.
         - `CFIs`: Centrally Funded Institutes.
     - `SeatType`: Type of seat available at the institute.
       - **Values**:
         - `AI`: All India open seats.
         - `OH`: Other state seats.
         - `HS`: Home state seats.
     - `InstAdd`: Address of the institute.
     - `InstPhone`: Phone number of the institute.
     - `InstFax`: Fax number of the institute.
     - `InstWebSite`: Website URL of the institute.
     - `EmailId`: Primary email ID of the institute.
     - `EmailId1`: Secondary email ID of the institute.
     - `ContactPerson`: Name of the contact person at the institute.
     - `Designation`: Designation of the contact person.
     - `MobileNo`: Mobile number of the contact person.

### 5. **Seats.csv**
   - **Description**: Contains detailed information about the seat allocation across various categories, branches, and states.
   - **Columns**:
     - `Quota`: Quota type.
       - **Values**:
         - `AI`: All India quota.
         - `HS`: Home State quota.
         - `OS`: Other State quota.
         - `GO`: Goa State quota.
         - `LA`: Laddak quota.
         - `JK`: Jammu & Kashmir quota.
     - `InstCd`: Institute code.
     - `BrCd`: Branch code.
     - `Cat`: Category of the seat.
       - **Values**:
         - `EW`: Economically Weaker Section.
         - `BC`: Other Backward Classes.
         - `GN`: General Category.
         - `ST`: Scheduled Tribes.
         - `SC`: Scheduled Castes.
     - `SubCat`: Subcategory of the seat (if applicable).
       - **Values**:
         - `PH`: PwD (Person with Disability) candidates.
         - `NO`: Non-PwD candidates.
     - `Gender`: Gender-specific seat allocation.
       - **Values**:
         - `B`: Male.
         - `F`: Female.
     - `StCd1`: State code 1.
     - `StCd2`: State code 2.
     - `StCd3`: State code 3.
     - `StCd4`: State code 4.
     - `StCd5`: State code 5.
     - `StCd6`: State code 6.
     - `StCd7`: State code 7.
     - `StCd8`: State code 8.
     - `StCd9`: State code 9.
     - `StCd10`: State code 10.
     - `TSeat`: Total number of seats.

#### 6. **prev_allotment.csv**
   - **Description**: Contains allotment details from previous rounds for each candidate.
   - **Columns**:
     - `RoundNo`: Allotment round number.
     - `Rollno`: Candidate's roll number.
     - `Birth_Cat`: Candidate's birth category.
       - **Values**:
         - `EW`: Economically Weaker Section.
         - `BC`: Other Backward Classes.
         - `GN`: General Category.
         - `ST`: Scheduled Tribes.
         - `SC`: Scheduled Castes.
     - `Rank`: Candidate's rank.
     - `Optno`: Option number representing the candidate's preference.
     - `Instcd`: Institute code of the allotted seat.
     - `Brcd`: Branch code of the allotted seat.
     - `AllottedCat`: Category under which the seat was allotted.
       - **Values**:
         - `SCNO`: Scheduled Castes (Non-PwD).
         - `STNO`: Scheduled Tribes (Non-PwD).
         - `EWNO`: Economically Weaker Section (Non-PwD).
         - `BCNO`: Other Backward Classes (Non-PwD).
         - `OPNO`: General Category (Non-PwD).
         - `SCPH`: Scheduled Castes (PwD).
         - `STPH`: Scheduled Tribes (PwD).
         - `EWPH`: Economically Weaker Section (PwD).
         - `BCPH`: Other Backward Classes (PwD).
         - `OPPH`: General Category (PwD).
     - `AllottedQuota`: Quota under which the seat was allotted.
       - **Values**:
         - `AI`: All India quota.
         - `HS`: Home State quota.
         - `OS`: Other State quota.
         - `GO`: Goa State quota.
         - `LA`: Laddak quota.
         - `JK`: Jammu & Kashmir quota.
     - `AllottedGender`: Gender-specific allotment.
       - **Values**:
         - `B`: Male.
         - `F`: Female.
     - `Flag`: Indicates any special flags or markers related to the allotment.
       - **Values**:
         - `N`: No flag.
         - `P`: Preparatory candidates.
         - `F`: Foreign candidates.
         - `D`: Defence candidates.
     - `SupNumReason`: Reason for any supplementary number assigned.
       - **Values**:
         - `NA`: No flag.
         - `DS`: Defence Service.
         - `FR`: Foreign.
     - `WithDraw`: Indicates if the candidate has withdrawn.
       - **Values**:
         - `N`: Not withdrawn.
         - `Y`: Withdrawn.
     - `RStatus`: Registration status.
       - **Values**:
         - `RT`: Seat retained.
         - `DR`: Dual reporting.
         - `RU`: Retained and upgraded.
         - `RC`: Reported and seat cancelled.
         - `NR`: Not reported.
     - `SStatus`: Seat status.
     - `Status`: Overall status of the allotment.
     - `ADate`: Allotment date.
     - `PIStatus`: Physical reporting status.
