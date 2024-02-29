# AutoCloudfareConnect

AutoCloudfareConnect is a Python script that allows you to automate the connection to Cloudflare's WARP service using scheduled tasks on Windows.

## Installation

To install and run AutoCloudfareConnect, follow these steps:

1. **Fork and Clone the Repository:** 
   - Fork this repository on GitHub to your own account.
   - Clone the forked repository to your local machine:
     ```
     git clone https://github.com/your-username/AutoCloudfareConnect.git
     ```

2. **Install PyInstaller:**
   - Ensure you have Python installed on your system.
   - Open a command prompt or terminal and navigate to the cloned repository folder.
   - Run the following command to install PyInstaller:
     ```
     pip install pyinstaller
     ```

3. **Build Executables:**
   - Once PyInstaller is installed, navigate to the repository folder in the command prompt or terminal.
   - Run the following commands to create the executable files:
     ```
     pyinstaller --onefile connect_cloudflare.py
     pyinstaller --onefile task_scheduler.py
     ```

4. **Download NSIS (Nullsoft Scriptable Install System):**
   - Download and install NSIS from [https://nsis.sourceforge.io/Download](https://nsis.sourceforge.io/Download).

5. **Add NSIS to System Variables (Optional):**
   - If NSIS is not added to the system variables, you need to add it manually to execute the scripts.
   - Add the NSIS installation directory to the system PATH variable.

6. **Build Setup Executable:**
   - Run the following command in the command prompt or terminal to build the setup executable:
     ```
     makensis AutoCloudfareConnect.nsi
     ```

## Usage

Once you have the setup executable (`AutoCloudfareConnect_Setup.exe`), follow these steps to use the software:

1. **Run the Setup Executable:**
   - Double-click on `AutoCloudfareConnect_Setup.exe` to run the setup wizard.

2. **Follow Installation Instructions:**
   - Follow the instructions in the setup wizard to complete the installation process.

3. **Setup Scheduled Task:**
   - After installation, the scheduled task will be created automatically to connect to Cloudflare's WARP service daily at the specified time (default is 00:14).

## Script Details

The `task_scheduler.py` script creates a scheduled task on Windows to execute the `connect_cloudflare.exe` executable daily at the specified time.

```python
import subprocess

def create_scheduled_task(task_name, script_path, start_time):
    # Construct PowerShell commands to create the scheduled task
    ps_commands = [
        f"$taskTrigger = New-ScheduledTaskTrigger -Daily -At '{start_time}'",
        "$taskSettings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries:$true -DontStopIfGoingOnBatteries:$true -StartWhenAvailable:$true -DontStopOnIdleEnd:$false -RunOnlyIfNetworkAvailable:$false",
        f"$taskAction = New-ScheduledTaskAction -Execute '{script_path}'",
        f"Register-ScheduledTask -TaskName '{task_name}' -Action $taskAction -Trigger $taskTrigger -Settings $taskSettings"
    ]
    
    # Execute PowerShell commands
    ps_script = "\n".join(ps_commands)
    subprocess.run(["powershell", "-Command", ps_script], check=True)

if __name__ == "__main__":
    task_name = "AutoConnectCloudflare"
    script_path = r"C:\Program Files (x86)\AutoCloudfareConnect\connect_cloudflare.exe"
    start_time = "00:14"
    
    create_scheduled_task(task_name, script_path, start_time)
