# how to docs

to build

```
make clean html
```

to autobuild

```
$ pip install watchdog
$ watchmedo shell-command \
              --patterns="*.rst" \
              --ignore-pattern='_build/*' \
              --recursive \
              --command='make clean html'

```
