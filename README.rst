.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

=================
collective.rating
=================

This product provides a behaviors that if assigned to a content type make this
votable.

Features
--------

- For the votable content there is a viewlet that showing the average grade for object
  and offers the possibility for users to votable that content.

- It is possible manage the number of stars with which we want to vote for the various
  content through a specific control panel.

- It is possible for single object manage the number of stars to show and whether make it or no not votable

Installation
------------

Install collective.rating by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.rating


and then running ``bin/buildout``



Dependencies
------------

This product has been tested on Plone 5.1


Credits
-------

Developed with the support of `Regione Emilia Romagna <http://www.regione.emilia-romagna.it/>`_;

Regione Emilia Romagna supports the `PloneGov initiative <http://www.plonegov.it/>`_.


Authors
-------

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.it/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/
