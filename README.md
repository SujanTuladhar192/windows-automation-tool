\# Windows Automation Tool



A simple Python-based utility that automates common Windows system maintenance tasks like cleaning temp files, backing up documents, and checking system resource usage.



---



\## Features



\- Clean temporary files (`%TEMP%` directory)

\- Show current:

&nbsp; - CPU usage

&nbsp; - RAM usage

&nbsp; - Disk usage

&nbsp; - OS platform/version

\- Backup user's `Documents` folder to Desktop

\- Launch Windows Task Manager directly



---



\## Requirements



\- Python 3.x

\- Python Standard Libraries:

&nbsp; - `os`

&nbsp; - `shutil`

&nbsp; - `subprocess`

&nbsp; - `platform`

\- Third-party Library:

&nbsp; - `psutil`  

&nbsp;   Install it with:



&nbsp;   ```bash

&nbsp;   pip install psutil

&nbsp;   ```



---



\## How to Run



1\. Clone or download this repository

2\. Open terminal in the project folder

3\. Run:



```bash

python main.py



