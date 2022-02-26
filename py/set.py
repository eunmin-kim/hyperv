import win32com.shell.shell as shell
import os
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


class cmd:
    def __init__(self, v):
        self.value = v
        self.check = 'bcedit'
        self.vb = 'bcdedit /set hypervisorlaunchtype off'
        self.docker = 'bcdedit /set hypervisorlaunchtype auto'
    
    def mode_checker(self):
        shell.ShellExecuteEx(
                lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+self.check)

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
    cmds = cmd(sys.argv[1])
    cmds.mode_checker()
    cmds.worker()