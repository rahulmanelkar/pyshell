from subprocess import run
import sys

def ccsh():
    cmd = input("ccsh> ").strip()
    run(cmd,stdin=sys.stdin, stdout=sys.stdout,stderr=sys.stderr)

if __name__=='__main__':
    ccsh()