from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess


# kills the gphoto2 process opened by gvfs
def killgPhoto2Process():
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()

    # search for running process and pass the pid
    for line in out.splitlines():
        if b'gvfsd-gphoto2' in line:
            pid = int(line.split(None, 1)[0])
            os.kill(pid, signal.SIGKILL)


session_name = 'pyLapse_Test'

shot_date = datetime.now().strftime('%Y%m%d')
shot_time = datetime.now().strftime('%Y%m%d-%H%M%S')

triggerCommand = ['--trigger-capture']
downloadCommand = ['--get-all-files']

folder_name = shot_date
download_location = '/home/leyd/Pictures/Timelapse' + folder_name

