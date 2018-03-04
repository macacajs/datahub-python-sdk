DataHub Python Client
=====================

.. image:: https://img.shields.io/coveralls/macacajs/datahub-python-sdk/master.svg?style=flat-square
    :target: https://coveralls.io/github/macacajs/datahub-python-sdk

.. image:: https://img.shields.io/travis/macacajs/datahub-python-sdk/master.svg?style=flat-square
    :target: https://travis-ci.org/macacajs/datahub-python-sdk

.. image:: https://img.shields.io/pypi/v/datahub-python-sdk.svg?style=flat-square
    :target: https://pypi.python.org/pypi/datahub-python-sdk

.. image:: https://img.shields.io/pypi/pyversions/wd.svg?style=flat-square
    :target: https://pypi.python.org/pypi/datahub-python-sdk/

.. image:: https://img.shields.io/pypi/dd/wd.svg?style=flat-square
    :target: https://pypi.python.org/pypi/datahub-python-sdk/

Intro
-----

datahub-python-sdk is a Python client implemented most of the APIs to control DataHub Service.

Homepage
--------
`datahub-python-sdk’s documentation. <//macacajs.github.io/datahub-python-sdk>`_

Examples
--------

.. code-block:: python

   datahub = DataHub(hostname = '127.0.0.1', port = '9200')

   datahub.switchScene(hub='sample', pathname='test1', data={ 'currentScene': 'scene1' })

   datahub.switchAllScenes(hub='sample', data={ 'currentScene': 'default' })

Changelog
---------
Details changes for each release are documented in the `HISTORY.rst <HISTORY.rst>`_.

Contributing
------------

`See CONTRIBUTING.rst <./CONTRIBUTING.rst>`_

License
-------
`MIT <http://opensource.org/licenses/MIT>`_
