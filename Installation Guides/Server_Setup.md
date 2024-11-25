
# Server Setup and Maintenance Guide

## Accessing the Server
To connect to the server, use the following SSH command:
```bash
ssh username@ip_address
```
Replace `username` with your server username and `ip_address` with the server's IP address.

---

## Freeing Up Space Caused by Zombie Processes
Zombie processes can consume resources unnecessarily. Use the commands below to free up space by identifying and terminating such processes:

1. **Kill the Process Running `virtualization.py`:**  
   This command finds and terminates the process safely:
   ```bash
   ps -aux | grep /home/it/Desktop/RUN/JAS/virtualization.py | grep -v grep | awk '{print $2}' | xargs -I {} kill -15 {}
   ```

2. **Kill Python 3.12 Processes:**  
   Use the following command to terminate Python 3.12 processes:
   ```bash
   ps -aux | grep /bin/python3.12 | grep -v grep | awk '{print $2}' | xargs -I {} kill -15 {}
   ```

3. **Force Kill if Necessary:**  
   If the processes do not terminate gracefully, use `kill -9` instead of `kill -15`.

---

## Clearing Swap Space
Sometimes, clearing swap space is necessary to improve server performance. Follow these steps:

1. **Check the Current Swap Usage:**  
   Run the command:
   ```bash
   free -m
   ```
   This will display memory and swap usage.

2. **Disable Swap:**  
   Temporarily disable the swap space:
   ```bash
   swapoff -a
   ```

3. **Wait for Memory to Clear:**  
   Wait approximately 30 seconds. Use the `free -m` command periodically to monitor the decrease in swap usage.

4. **Enable Swap:**  
   Re-enable the swap space:
   ```bash
   swapon -a
   ```

---

## Zipping a Folder Recursively
To compress a folder and its contents into a `.zip` file, use the following command:
```bash
zip -r target.zip source_path
```
- Replace `target.zip` with the desired name for the zip file.
- Replace `source_path` with the path to the folder you want to compress.

---

## Notes
- Always ensure you have the necessary permissions to perform these operations.
- Use `kill -9` cautiously as it forcefully terminates processes and might cause data loss.
- Make backups before performing critical operations like clearing swap space or terminating processes.
