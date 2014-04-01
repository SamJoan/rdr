purpose
=======

while penetration testing CMSs it is very frequent to have to do tasks that are very repetitive, error prone
and boring. One example of these is when we encounter an application that has deleted the application
changelog, or otherwise wisely made the file unavailable to download, and we need to identify what version of
the software is currently installed.

The process is very manual: 

* Search the web root for a file (CHANGELOG.txt, main.js) in the webroot that we can download.
* Download the latest version of the software and compare checksums.
* if checksums match, stop and review. Otherwise repeat from step 2.

It is my personal view that one should never work hard, and this process is slow and tedious. Another thing
that needs to be done manually is to fingerprint the CMS's plugins, and check if those are up to date. The
process is similar to the above.

As well as that, I will be maintaining a compilation of (preferably written in a very simple DSL using
PyParsing) reliable exploits, possibly unauthenticated. Which brings us to authentication: rdr will not be
handling authentication. It will however accept an optional parameter for using an upstream proxy.

In short, I would like rdr to be a very simple tool that will behave transparently through simple behaviour,
good documentation, unit-tests and good code quality.

