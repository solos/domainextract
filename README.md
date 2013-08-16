domainextract
=============

extract domain from url or domain


About
------------

domainextract is a sub/root domain extracter.


Install
------------

pip install domaintldextract or pip install https://github.com/solos/pydnspod/tarball/master


Usage
------------
    import domaintldextract as dextr
    url = 'http://www.baidu.com'
    domain = dextr.extract_domain(url)
    root_domain = dextr.extract_rootdomain(url)
    print dextr.extract(domain)

License
-----------
    MIT
