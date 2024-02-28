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