import subprocess
import time

class DeviceController:
    def __init__(self, adb_path='adb'):
        self.adb_path = adb_path

    def run_adb_command(self, command):
        full_cmd = [self.adb_path] + command.split()
        try:
            result = subprocess.run(full_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
            if result.returncode == 0:
                return result.stdout.strip()
            else:
                print(f"ADB command failed: {' '.join(full_cmd)}\nError: {result.stderr.strip()}")
                return None
        except subprocess.TimeoutExpired:
            print(f"ADB command timed out: {' '.join(full_cmd)}")
            return None

    def is_device_connected(self):
        output = self.run_adb_command('devices')
        if output:
            lines = output.split('\n')
            # Skip header line
            for line in lines[1:]:
                if 'device' in line:
                    return True
        return False

    def launch_app(self, package_name, activity_name):
        # Start app activity
        command = f'shell am start -n {package_name}/{activity_name}'
        return self.run_adb_command(command)

    def stop_app(self, package_name):
        command = f'shell am force-stop {package_name}'
        return self.run_adb_command(command)
    
    def simulate_tap(self, x, y):
        command = f'shell input tap {x} {y}'
        return self.run_adb_command(command)

    def simulate_swipe(self, x1, y1, x2, y2, duration_ms=500):
        command = f'shell input swipe {x1} {y1} {x2} {y2} {duration_ms}'
        return self.run_adb_command(command)

    def get_current_focused_app(self):
        command = 'shell dumpsys window windows | grep -E \"mCurrentFocus\"'
        output = self.run_adb_command(command)
        if output:
            return output
        return None

    def get_logcat(self, filter_tag=None, max_lines=100):
        cmd = f'shell logcat -d -t {max_lines}'
        if filter_tag:
            cmd += f' | grep {filter_tag}'
        return self.run_adb_command(cmd)

if __name__ == "__main__":
    # Simple self-test
    dc = DeviceController()
    if dc.is_device_connected():
        print("Device is connected.")
        # Example: launch the recorder app (replace with real package/activity)
        print(dc.launch_app('com.example.recorderapp', 'com.example.recorderapp.MainActivity'))
        time.sleep(5)
        print(dc.get_current_focused_app())
        print(dc.simulate_tap(100, 200))
        print(dc.get_logcat(filter_tag="RecorderApp"))
        print(dc.stop_app('com.example.recorderapp'))
    else:
        print("No device connected.")
