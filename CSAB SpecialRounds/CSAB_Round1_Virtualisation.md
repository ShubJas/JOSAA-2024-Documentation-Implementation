# CSAB Round 1 Virtualisation
## Code Snippet 1: Importing Libraries

In this section of the code, the following libraries are imported:
- `pandas`: for data manipulation and analysis.
- `time`: for time-related functions.
- `concurrent.futures.ProcessPoolExecutor`: for parallel processing.
- `dask.dataframe`: for processing large datasets efficiently.

The script also starts a timer using `time.time()` to track the full execution time.

### Code:
    
        import pandas as pd
        import time
        from concurrent.futures import ProcessPoolExecutor
        import dask.dataframe as dd

        start_full = time.time()
    
