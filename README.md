# Seat Allocation System: Documentation, Setup and Execution Guide

This guide provides detailed documentation and instructions for setting up and running the seat allocation system for JoSAA, CSAB special Rounds, NEUT and Supernumerary Rounds. 

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

- **Codes and code overviews**: All source codes and code explanations are located in the respective folders. There are folders for each round, holding the relevant Jupyter notebooks and `.md` files for explanations.

### Folder Structure:
- **JoSAA_Round1**: This folder contains the files for JoSAA Round 1.
- **JoSAA_Round2+**: This folder holds the files for JoSAA Rounds 2 through 5.
- **CSAB_NEUT**: This folder contains all files related to the CSAB NEUT rounds.
- **CSAB_Supernumerary**: This folder contains all files for handling the CSAB Supernumerary rounds.
- **CSAB_SpecialRounds**: This folder contains all files for handling the CSAB Special rounds.


Each of these folders contains the code necessary to process the respective rounds and a `Code_Overview.md` file to help understand the workflow and logic behind the notebooks.


- **Data**: Due to the confidentiality of the data, we have not provided the data in this repository, the data is stored in the database, if u are authorized, you can get access. While storing the data, make sure to save the data in order and in seperate folders. The data should be organized round-wise and stored in their respective directories. Ensure to reference the proper directory when setting source paths in the notebooks. For undestand schema refer [DATA-SCHEMA](https://github.com/ShubJas/JOSAA-2024-Implementation/blob/main/Data_Table_Schema.md).

## Notebooks Overview

For a detailed explanation of the sequence of notebooks used in the JoSAA/CSAB allocation process, including the inputs, outputs, and the purpose of each notebook across different rounds, please refer to the [IO.md](./IO.md) file.

The `IO.md` file provides an in-depth overview of the workflow for each round, including the special rounds like CSAB and NEUT. It describes the expected inputs and generated outputs for each notebook, as well as the specific role each notebook plays in the allocation process. This documentation is essential for understanding the execution flow and ensuring that each step is performed correctly.

Make sure to consult the `IO.md` file before running the notebooks to avoid any discrepancies and to better understand the overall process.


## General Setup

1. **Open the Round Folder**:
   - Navigate to the specific round folder for which you want to run the allocation system. Each round folder contains the necessary data files and Jupyter notebooks.

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

### CSAB Special Rounds 

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


## Requirements
You can install all the required Python packages using the following command:

```
pip install -r requirements.txt
```



## Support

For any issues or questions regarding the setup or execution of the notebooks, contact [shuaibkuwait.211ec251@nitk.edu.in](mailto:shuaibkuwait.211ec251@nitk.edu.in).
