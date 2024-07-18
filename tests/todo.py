import subprocess

def get_todo_windows():
    applescript = """
    tell application "System Events"
        set todoApp to "Microsoft To Do"
        set todoWindows to (windows of application process todoApp)
        set windowNames to name of every window of application process todoApp
    end tell
    return windowNames
    """
    
    process = subprocess.Popen(['osascript', '-e', applescript], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    
    if process.returncode != 0:
        raise Exception(f"AppleScript error: {stderr.decode('utf-8')}")
    
    window_names = stdout.decode('utf-8').strip().split(", ")
    return window_names

windows = get_todo_windows()
print(windows)
