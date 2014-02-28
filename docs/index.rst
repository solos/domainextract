.. domainextract documentation master file, created by
   sphinx-quickstart on Fri Feb 28 21:19:06 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

domainextract文档
=========================================

目录:
========

.. toctree::
    :maxdepth: 2


根据域名获取前缀、根域名
--------------------------
    
.. code-block:: python

    import domainextract
    domain = 'del.icio.us'
    print domainextract.extract(domain)

根据url获取域名
--------------------------

.. code-block:: python

    import domainextract
    url = 'http://del.icio.us'
    print domainextract.extract_domain(url):


根据url获取根域名
--------------------------
 
.. code-block:: python

    import domainextract
    url = 'http://del.icio.us'
    print extract_rootdomain(url):


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
