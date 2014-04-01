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

design philosophies
###################

This page will outline the particular goals rdr would like to achieve, and basic documentation regarding how
said funcionality will be implemented. Specifically in this page, I will plan out how the code will be
basically laid out.

The goal in this specific part is not to imagine a directory structure, but to think of a possible way to
abstract as much code into the core of the application but still allowing space for CMS-specific behaviour.
For example, one of the main goals of this software is to fingerprint CMS, and in order to do so, the
application would need to get a big list of wordpress/drupal/other tar.gz files, extract them into a
particular folder and begin comparing checksums.

rdr will handle only the comparing of checksums, and will require the user to manually get a list of files for
a very simple reason: to attempt to keep the software as simple and make it less error-prone. If rdr attempted
to download the software, then it'd need to know from where to download the software, how to deal with
particularly nasty directory structures, know how to extract the particular compression scheme, and then
finally react to how the folders are stored inside the compressed file.

That is the design philosophy the application will follow: keep functionality to a minimum and usefulness to
a maximum. Many little components interacting with one another.

Other specific points:

* python3 only. python3 is available on most distributions and python2 is the past.
* unit testing >90% test coverage.
* Coding guidelines will be as per the `python philosophy <http://c2.com/cgi/wiki?PythonPhilosophy>`_, which
  is very related to the Security-Assessment's, "don't be a dick".
* The philosophy regarding dependencies is to require as many as humanly possible, and to reinvent the wheel
  as little as possible. All your dependency are belong to us.
