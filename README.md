# Python Watcher

This is a very simple python script that watches files. I created this
because `watchmedo` was being too unpredictable while all I wanted to
do was something super simple. So, here it is. The code is extremely
simple and it just waits every seconds to execute the given command.

Here's an example that will watch all [Latex](https://www.latex-project.org/)
files and compile the `document.tex` file whenever any of them change
at 1 second intervals:
```python3
python3.8 watcher.py --pattern \*.tex --command "pdflatex document.tex"
```

If I wanted to run the command given at the start, then I'd run the
following:
```python3
python3.8 watcher.py --pattern \*.tex --command "pdflatex document.tex" --run-on-start
```

This also allows smaller flags so that you don't have to type so many extra
characters. Here's how we can run the same thing above with smaller flags:
```python3
python3.8 watcher.py -p \*.tex -c "pdflatex document.tex" -ros
```

Finally, not sure what to do, just ask for help with:
```python3
python3.8 watcher.py --help
```

Which would display the following:
```
usage: watcher.py [-h] -p PATTERN -c COMMAND [-ros]

This is a simple file watcher program that runs a given command every time any file in the
current diretory that matches a simple given glob pattern changes. The scripts that can be run
with this watcher must be very simple scripts that don't require STDIN.

optional arguments:
  -h, --help            show this help message and exit
  -p PATTERN, --pattern PATTERN
                        a glob pattern to match files in the current directory
  -c COMMAND, --command COMMAND
                        a shell command to run if matched files changed
  -ros, --run-on-start  when given, this will run the shell command when started
```

# LICENSE: UNLICENSE

```
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
```

TL;DR: Do whatever you want I don't care.

