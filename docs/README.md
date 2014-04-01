# how to docs

to build

```
make clean html
```

to autobuild

```
$ pip install watchdog
$ watchmedo shell-command --patterns="*.rst;*.py" --ignore-pattern='build/*' --recursive --command='make clean html'

```
