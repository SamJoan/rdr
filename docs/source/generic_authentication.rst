authentication
==============

Authentication is a misterious beast, and it can be performed in many different ways:

* Cookies.
* URL Parameters.
* Headers.
* Parameters in POST requests.

And on top of that, sometimes it's a pain in the ass to identify what kind of authentication a server wants (I
am looking at you ``WWW-Authenticate: Negotiate``). 

The only way of managing authentication in ``rdr`` is to route all traffic through an intercepting proxy and having it
modify the requests so as to make them authenticated. This can be done using ZAP, Burp or Fiddler. 

You can set the proxy using the `http_proxy and https_proxy
<https://wiki.archlinux.org/index.php/proxy_settings>`_ environment variables. If your proxy is evil and
intercepts and does all other sorts of malicious stuff to the requests rdr sends through and receives, you can
pass the ``--no-verify-ssl`` flag to rdr in order for it to stop bitching.


