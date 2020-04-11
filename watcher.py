import argparse
import glob
import os
import subprocess
import time


SLEEP_TIME_SEC = 1.0


def run_bash_command(command: str) -> subprocess.CompletedProcess:
    """
    Runs the bash command without interfering with stdout, stderr,
    and stdin. If any of those are needed, this will NOT handle it.
    """
    return subprocess.run(command.split(" "))


def run_watcher(pattern: str, command: str, run_on_start: bool=False) -> None:
    """
    For every files that match the given glob pattern, this will,
    every SLEEP_TIME, check whether any of those files changed. If
    any changed, then it would run the command given.

    If run_on_start is given, the bash command will run at the very
    beginning before starting to watch for changes.
    """
    if run_on_start:
        run_bash_command(command)

    files = {
        fname: os.path.getmtime(fname)
        for fname in glob.glob(pattern)
        if os.path.isfile(fname)
    }

    while True:
        time.sleep(SLEEP_TIME_SEC)

        # figure out files with new times
        new_files = {}
        for fname, lasttime in files.items():
            newtime = os.path.getmtime(fname)
            if newtime == lasttime:
                continue
            new_files[fname] = newtime

        # batch the runs so that we run only once if any file changed
        if len(new_files) != 0:
            _ = run_bash_command(command)
            files.update(new_files)


def parser() -> argparse.ArgumentParser:
    """ Creates a parser using argparse """

    parser = argparse.ArgumentParser(description=(
        "This is a simple file watcher program that runs a given command "
        "every time any file in the current diretory that matches a simple "
        "given glob pattern changes. The scripts that can be run with this "
        "watcher must be very simple scripts that don't require STDIN. "
    ))

    parser.add_argument(
        "-p", "--pattern",
        type=str,
        help="a glob pattern to match files in the current directory",
        required=True,
    )
    parser.add_argument(
        "-c", "--command",
        type=str,
        help="a shell command to run if matched files changed",
        required=True,
    )
    parser.add_argument(
        "-ros", "--run-on-start",
        action="store_true",
        help="when given, this will run the shell command when started",
    )

    return parser


if __name__ == "__main__":
    args = parser().parse_args()
    run_watcher(args.pattern, args.command, run_on_start=args.run_on_start)

