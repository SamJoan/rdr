cms version establishment 
=========================

This functionality is abstract, and is not dependent on any CMS.

Basic usage is as follows:

.. code-block:: bash

    rdr cms_ver --file-online=http://example.com/license.txt --dir=~/extracted_drupals/

This command will look through the "~/extracted_drupals/" directory and search for files same checksum as
``--file-online``, and, if found will output the directory(s) the file was found on.

Here is a detailed description of each parameter, and some other optional parameters:

    --file-online the full URL of the file we want to check against. This could be a standard .txt file or
        some other resources such as .js or .css files, or even images.

    --dir rdr does not handle downloading of wordpress/drupal/whatever files. Instead, the pentester needs to
        download them and place them in a directory with a directory structure that will be described below.

    --file-local the local path to the files, relative to the root of any extracted folder. This is useful to
        specify a path/filename different to the one on file online. If not present, this will be set to the
        path of file-online.

In order to keep it simple as, and to not be tied down to URL structures that don't make sense or change or
other nuisances, the user needs to download and extract the files. The structure required is strictly as
follows:

.. code-block:: bash

        .
        ├── wordpress-3.7
        [...]
        │   └── license.txt
        ├── wordpress-3.7.1
        [...]
        │   └── license.txt
        ├── wordpress-3.7.1.tar.gz
        ├── wordpress-3.7.tar.gz
        ├── wordpress-3.8
        [...]
        │   └── license.txt
        ├── wordpress-3.8.1
        [...]
        │   └── license.txt
        ├── wordpress-3.8.1.tar.gz
        └── wordpress-3.8.tar.gz

Everything that is not a directory will be ignored, and the version establishment algorithm will do as
follows:

# Will get the checksum of ``--file-online`` and hold on to it.
# Open wordpress 3.7. Will then compare the checksum of ``--dir``/wordpress-3.7/``--file-local``
# Repeat for _all_ other directories present.
# Output the directories, if any, that contain a file with that name and checksum.

Some sample output may be

.. code-block:: bash
    wordpress-3.7/license.txt matches sha256 hash starting with 8f6e8b[...]
    wordpress-3.7.1/license.txt matches sha256 hash starting with 8f6e8b[...]

Based on this, you know that the license.txt file belongs to either wordpress 3.7 or wordpress 3.7.1.
