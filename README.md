# Seat Allocation System: Setup and Execution Guide

This guide provides detailed instructions for setting up and running the seat allocation system for JoSAA, CSAB special Rounds, NEUT and Supernumerary Rounds. 

### Fork and Clone the JOSAA-2024-Implementation repo

Click Fork button (top right) to establish a cloud-based fork.

```
git clone YOUR_PERSONAL_FORK_URL
```

## Pre-requisites

Before you begin, ensure the following are installed on your system:

- **Python 3.x**: Make sure you have Python 3.x installed. You can download it from the [official Python website](https://www.python.org/downloads/).

- **Jupyter Notebook**: Install Jupyter Notebook to run the provided `.ipynb` files:
```
  pip install jupyterlab
```
-  **Pandas**: Install pandas for  data manipulation tasks:
```
  pip install pandas
```



## Code and Data Organization

- **Code**: All source code is located in the `codes` directory. This directory contains subfolders for each round, holding the relevant Jupyter notebooks.

- **Data**: The data for the year 2024, organized round-wise, is stored in the `JoSAA_CSAB_2024` directory. Ensure to reference this directory when setting source paths in the notebooks. For undestand schema refer [DATA-SCHEMA](https://github.com/ShubJas/JOSAA-2024-Implementation/blob/main/Data_Table_Schema.md).

## General Setup

1. **Open the Round Folder**:
   - Navigate to the specific round folder within the `codes` directory for which you want to run the allocation system. Each round folder contains the necessary data files and Jupyter notebooks.

2. **Change Source Paths**:
   - Inside the Jupyter notebooks, update the paths to the source data files. These paths are typically defined at the beginning of each notebook. Ensure that they point to the correct file locations on your system.

## Running the Notebooks

Follow the steps below based on the round type you are processing:

### JoSAA Rounds (Rounds 1 to 5)

Run the following Jupyter notebooks in the order specified to process the JoSAA rounds:

1. **merit_extended.py**:
   - This notebook prepares and processes the merit list extended with additional candidate details required for the allocation.

2. **virtualization.ipynb**:
   - Processes virtualization of the merit list to handle different categories and subcategories of seats.

3. **allocationReader.ipynb**:
   - Reads and finalizes the allocation results, applying the logic defined for seat allocation and constraints.

### CSAB Special Rounds (Rounds 7 and 8)

For the CSAB special rounds, follow this sequence:

1. **virtualization.ipynb**:
   - Similar to the JoSAA rounds, this notebook handles the virtualization required for the special rounds.

2. **allocationReader.ipynb**:
   - Finalizes the allocation for CSAB special rounds, focusing on handling the unique rules and constraints applicable to these rounds.

## Additional Notes

- Ensure that you check the outputs of each notebook for errors or warnings that might need attention.
- The sequence of running the notebooks is crucial. Do not alter the order unless you are familiar with the process dependencies.

## Data Schema

For detailed information on the data schema, please refer to the [DATA-SCHEMA](https://github.com/ShubJas/JOSAA-2024-Implementation/blob/main/Data_Table_Schema.md).


## Support

For any issues or questions regarding the setup or execution of the notebooks, contact [shuaibkuwait.211ec251@nitk.edu.in](mailto:shuaibkuwait.211ec251@nitk.edu.in).
