Standalone thumbnailer engine based on sorl-thumbnail.

Features at a glance
====================

- Python 3 support
- Storage support
- Pluggable Engine support for Pillow
- Pluggable Key Value Store support (redis)
- Pluggable Backend support
- Dummy generation (placeholders)
- Flexible, simple syntax, generates no html
- CSS style cropping options
- Back smart cropping, and remove borders from the images when cropping
- Margin calculation for vertical positioning
- Alternative resolutions versions of a thumbnail

Read more in `the documentation (latest version) <http://sorl-thumbnail.rtfd.org/>`_

Developers
==========

|jazzband|

This is a `Jazzband <https://jazzband.co>`_ project. By contributing you agree to 
abide by the `Contributor Code of Conduct <https://jazzband.co/about/conduct>`_ 
and follow the `guidelines <https://jazzband.co/about/guidelines>`_.

Feel free to create a new Pull request if you want to propose a new feature.
If you need development support or want to discuss with other developers
join us in the channel #sorl-thumnbnail at freenode.net or Gitter.

For releases updates and more in deep development discussion use our mailing list
in Google Groups.

- IRC Channel: irc://irc.freenode.net/#sorl-thumbnail

- Gitter: https://gitter.im/jazzband/sorl-thumbnail

- Mailing List: sorl-thumbnail@googlegroups.com https://groups.google.com/d/forum/sorl-thumbnail

Tests
-----
The tests should run with tox and pytest. Running `tox` will run all tests for all environments.
However, it is possible to run a certain environment with `tox -e <env>`, a list of all environments
can be found with `tox -l`. These tests require the dependencies of the different engines defined in
the documentation. It is possible to install these dependencies into a vagrant image with the
Vagrantfile in the repo.

User Support
============

If you need help using sorl-thumbnail browse http://stackoverflow.com/questions/tagged/sorl-thumbnail
and posts your questions with the `sorl-thumbnail` tag.


How to Use
==========

Low level API
-------------

You can use the 'get_thumbnail'::

    from sorl.thumbnail_standalone import ThumbnailBackend

    thumbnailer = ThumbnailBackend({
        ...settings dict...
    })
    im = thumbnailer.get_thumbnail(my_file, '100x100', crop='center', quality=99)
    delete(my_file)

See more examples in the section `Low level API examples`_ in the Documentation
