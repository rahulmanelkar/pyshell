from subprocess import run
import sys

def ccsh():
    while True:
        cmd = input("ccsh> ").strip()
        if cmd == "exit":
            sys.exit(0)
        run(cmd,stdin=sys.stdin, stdout=sys.stdout,stderr=sys.stderr)
    

if __name__=='__main__':
    ccsh()