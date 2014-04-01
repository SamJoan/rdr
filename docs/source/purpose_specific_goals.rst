specific goals
==============

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

Other specific requirements are > 90% test coverage. Coding guidelines will be as per the `python philosophy
<http://c2.com/cgi/wiki?PythonPhilosophy>`_, which is very related to the Security-Assessment's, "don't be a
dick".


