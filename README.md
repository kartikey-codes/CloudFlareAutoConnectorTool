# AutoCloudfareConnect

AutoCloudfareConnect is a Python script that allows you to automate the connection to Cloudflare's WARP service using scheduled tasks on Windows.

## Prerequisites

- This version only supports Windows operating system.
- Cloudflare WARP must be installed on the Windows system.

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
   - Run the following commands to create the executable files. The executables will be built in the `dist` folder:
     ```
     pyinstaller --onefile connect_cloudflare.py
     pyinstaller --onefile task_scheduler.py
     ```

4. **Download and Install NSIS:**
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

After installation, follow these steps to use AutoCloudfareConnect:

1. **Run the Setup Executable:**
   - Double-click on `AutoCloudfareConnect_Setup.exe` to run the setup wizard.
   - Follow the instructions in the setup wizard to complete the installation process.

2. **Run Task Scheduler:**
   - Navigate to the folder where AutoCloudfareConnect is installed (default location: `C:\Program Files (x86)\AutoCloudfareConnect`).
   - Run the `task_scheduler.exe` file.
   - The scheduled task will be created automatically to connect to Cloudflare's WARP service daily at the specified time (default is 00:14).

3. **Verification:**
   - Open Windows Task Scheduler.
   - Go to Task Scheduler Library and find the details for the `AutoConnectCloudflare` task.
   - Verify the path of the `connect_cloudflare.exe` in the Actions tab of the Windows Task Scheduler.

