generic module version establishment
====================================

"Generic Module Version Establishment" or GMVE, is a standard enterprise method for establishing the needs and
particularities of a...

OK, GMVE is not that different from GVE, really. The procedure still consists of getting a bunch of tar files,
putting them in a directory and comparing checksums. On the previous chapter, we executed the following
command:

.. code-block:: bash

    rdr ver_chk --file-online=http://example.com/license.txt --dir=~/extracted_wordpress/

Now we need do the same, except the URL now looks, for example, like this
http://example.com/wp-content/plugins/akismet/readme.txt

This also means that we need to make use of the ``--file-local`` parameter, to avoid the checksum checking
algorithm to use the full path. This would look as follows:

.. code-block:: bash

    rdr ver_chk --file-online=http://nadakedecir.net/wp-content/plugins/akismet/readme.txt
        --file-local=readme.txt --dir=~/extracted_akismet/


Again, the extracted akismet folder structure should look as follows:

.. code-block:: bash

    ~/extracted_akismet/
    ├── akismet.2.5.7
    [..]
    │   ├── readme.txt
    [..]
    ├── akismet.2.5.7.zip
    ├── akismet.2.5.8
    [..]
    │   ├── readme.txt
    [..]
    ├── akismet.2.5.8.zip
    ├── akismet.2.5.9
    [..]
    │   ├── readme.txt
    [..]
    ├── akismet.2.5.9.zip
    ├── akismet.2.6.0
    [..]
    │   ├── readme.txt
    [..]
    └── akismet.2.6.0.zip
    
The procedure will be exactly as described in the previous chapter again, and the result hopefully will be
something similar to what's output below.

.. code-block:: bash

    akismet.2.6.0/license.txt matches sha256 hash starting with 8f6e8b[...]
