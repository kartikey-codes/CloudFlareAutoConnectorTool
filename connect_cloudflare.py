import subprocess

def connect_to_warp():
    subprocess.run(['warp-cli.exe', 'connect'])

# Call the function to connect to WARP
connect_to_warp()
