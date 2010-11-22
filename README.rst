==============================
Django CMS ImageKit
==============================

CMS ImageKit exposes `django-imagekit <http://hg.driscolldev.com/django-imagekit>`_'s image processing and caching functionality within `Django CMS <http://www.django-cms.org/>`_.

Currently in development - DO NOT USE for production sites!

NOTE: Requires fix for django-cms issue #588 (hopefully in trunk soon).
      *** also waiting on update to django-imagekit
      
Features
========

* Named "presets" define image processing rules.
* Content editors select which preset to display image with
* Picutre plugin extends and replaces the django-cms Picture plugin to add an imagekit preset.
* Roll-your-own - abstract base class allows you to roll your own plugin for any class with an ImageField (sample app included)
* Built on top of the lightweight, extensible `django-imagekit <http://hg.driscolldev.com/django-imagekit>`_ module.

Dependencies
============

* django-cms 2.1+
* django-imagekit 0.3.4+ *** 
* python 2.5+

License
=======
    Copyright (C) 2010  Driftwood Cove Designs
    See the `LICENSE <http://github.com/powderflask/cms-imagekit/blob/master/LICENSE>`_ for more details
    
You are free to copy, use, or modify this software in any way you like, but please provide attribution to the original author with a link to:
https://github.com/powderflask/cms-imagekit

Author
------
`Driftwood Cove Designs <http://designs.driftwoodcove.ca>`_

Known Issues
============

see: https://github.com/powderflask/cms-imagekit/issues


Installation
============

From PyPI
---------

not yet - sorry.

Manual Download
---------------

You can download a zipped archive from http://github.com/powderflask/cms-imagekit/downloads.

Unzip the file you downloaded. Then go in your terminal and ``cd`` into the unpacked folder. Then type ``python setup.py install`` in your terminal.

Configuration
-------------
Add the base module and one or more plugins to your ``INSTALLED_APPS`` in settings.py::

    INSTALLED_APPS = (..., 
        'cms_imagekit.plugins.*',  # installs all imagekit plugins
    )  

OR  pick and choose::

    INSTALLED_APPS = (...,
        'cms_imagekit.plugins.picture',  # use this instead of 'cms.plugins.picture'
    )
                 
Don't forget to syncdb.

Templates
---------
Recommended to use the app_directories template loader::

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        ...
    )

If you aren't using the app_directories template loader, you will need to add the
templates to your TEMPLATE_DIRS settings.  The templates are at::

   cms_imagekit/plugins/<plugin-name>/templates

and can be overridden by adding a "cms_imagekit" folder to your project templates directory.
    

Settings
========

* CMS_IKPICTURE_SPECS - module defining the ImageSpec presets for the picture plugin.
  default defines a 100x100 preset named "thumbnail" 
      CMS_IKPICTURE_SPECS = 'cms_imagekit.plugins.picture.defaults'

Presets
=======
A preset defines a set of image processing operations, which might include scaling,
cropping, etc.
Currently, all presets are defined in code by defining django-imagekit ImageSpec classes.
(see `documentation <http://hg.driscolldev.com/django-imagekit/wiki/Home>`_).

Future
------
It should be possible to add ability to define new Presets through the Django Admin interface.


Kudos
=====

* inspired by the fabulous imagecache module in Drupal  http://drupal.org/project/imagecache
* built upon the extensible django-imagekit http://hg.driscolldev.com/django-imagekit
