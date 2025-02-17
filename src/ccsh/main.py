from subprocess import run
import sys

def ccsh():
    """Implementation of the shell. Runs forever till exit command is used."""
    while True:
        cmd = input("ccsh> ").strip()
        if cmd == "exit":
            sys.exit(0)
        run(cmd,stdin=sys.stdin, stdout=sys.stdout,stderr=sys.stderr)
    

if __name__=='__main__':
    ccsh()