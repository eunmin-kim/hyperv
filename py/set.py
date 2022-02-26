from base64 import encode
from concurrent.futures import process
import win32com.shell.shell as shell
from win32com.shell import shellcon
import win32con
import win32process
import win32event
import os
import sys
import io
import subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


class cmd:
    def __init__(self, v):
        self.value = v
        self.check = 'bcdedit'
        self.vb = 'bcdedit /set hypervisorlaunchtype off'
        self.docker = 'bcdedit /set hypervisorlaunchtype auto'

    # def mode_checker(self):
        # result = shell.ShellExecuteEx(
        #     lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+self.check,
        #     nShow=win32con.SW_SHOW)
        # bytes = string.encode(encoding='UTF-8')

        # print(out.decode('cp949'))
        # print(result)
        # sys.stdout.flush()
        # proc = subprocess.Popen(['systeminfo'],stdout=subprocess.PIPE)
        # out, err = proc.communicate()
        # out = out.decode('cp949')
        # out = out.replace(" ","")
        # out = ' '.join(char for char in out if char.isalnum())
        # out = out.split("\n")
        # out = list(map(str,out))
        
        # print(any("Hyper" in out))

    def worker(self):
        if self.value == '0':
                shell.ShellExecuteEx(
                    lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+self.vb)
                print("Virutal Box Mode Set")
                sys.stdout.flush()
        elif self.value == '1':
            shell.ShellExecuteEx(
                lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+self.docker)
            print("Docker Mode Set")
            sys.stdout.flush()


if __name__ == '__main__':
    # if sys.argv[1] == 'Success':
    #     cmds = cmd(sys.argv[1])
    #     cmds.mode_checker()
    # else:
    #     cmds = cmd(sys.argv[1])
    #     cmds.mode_checker()
    #     cmds.worker()
    cmds = cmd(sys.argv[1])
    cmds.worker()
