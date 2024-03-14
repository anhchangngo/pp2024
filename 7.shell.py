import os
import subprocess as sp

while True:
    terminal = input("Dat $ ")
    if terminal == "ls":
        sp.run(["ls", "-la"])
    elif terminal == "bc":
        sp.run(["bc"])
    elif terminal == "ps aux | grep term":
        ps_process = sp.Popen(["ps", "aux"], stdout=sp.PIPE)
        grep_process = sp.Popen(["grep", "term"], stdin=ps_process.stdout)
        ps_process.stdout.close()
        grep_process.wait()
    elif terminal.startswith("cd "):
        directory = terminal.split(maxsplit=1)[1]
        try:
            os.chdir(directory)
        except FileNotFoundError:
            print("Not found directory", directory)
    else:
        print("Unsupported command.")

