.. image:: https://mybinder.org/badge.svg
    :target: https://mybinder.org/v2/gh/josephcslater/Introduction_to_Python/master?urlpath=lab

Instructions for Introduction to Scientific Python
==================================================

.. bibliographic fields (which also require a transform):

:Author: Joseph C. Slater
:Address: Cookeville, TN 38505
:Contact: joseph.c.slater@gmail.com
:date: 2026-09-25
:status: 2026 version
:version: 2.0
:copyright: This document has been placed in the public domain. You
            may do with it as you wish. You may copy, modify,
            redistribute, reattribute, sell, buy, rent, lease,
            destroy, or improve it, quote it at length, excerpt,
            incorporate, collate, fold, staple, or mutilate it, or do
            anything else to it that your or anyone else's heart
            desires.

Run the notebooks in your browser with `this class in mybinder.org`_ or `do this class in Jupyter Lab`_. The repository contains multiple notebooks; select the one you want after the environment launches.

Quick Start
-----------

1. **Easiest**: click the *launch Binder* badge above to run the notebooks in your browser with nothing to install.

2. **Recommended for beginners**: install `Anaconda Python`_ and `GitHub Desktop`_, clone `the repository for this class in your web browser`_, then run::

       conda env create --file environment.yml
       conda activate introduction-to-python
       jupyter lab Introduction_to_Scientific_Python.ipynb

   **Full, platform-by-platform instructions (Windows/Mac/Linux) are in** `docs/SETUP.rst`_. Read that first if anything above is unclear or does not work.

3. **Alternative for users comfortable with terminals**: install `uv`_, clone the repository, and follow the `uv setup instructions`_ in `docs/SETUP.rst`_. Anaconda is easier for beginners because it provides a guided installer, Anaconda Prompt, and the compiler support used by this course.

See `What will be covered`_ for the course notes and `topics.rst`_ for the list of topics.

Other Educational Resources
---------------------------
- `Python Plotting With Matplotlib`_
- `Lorena Barba's Numerical Python MOOC`_
- `SciPy Lecture Notes`_
- `Generic Python Introduction`_
- `SciPy Cookbook`_

Recommended Books
-----------------
- `Learning Scientific Programming with Python`_ - Christian Hill
- `A Primer on Scientific Programming with Python`_ - Hans Petter Langtangen (`4th Edition`_)

.. _`SciPy Cookbook`: https://scipy-cookbook.readthedocs.io/
.. _`Generic Python Introduction`: https://github.com/guntukukamal/Good-python-reference
.. _`SciPy Lecture Notes`: https://github.com/scipy-lectures/scipy-lecture-notes
.. _`4th Edition`: https://hplgit.github.io/primer.html/doc/pub/half/book.pdf
.. _`A Primer on Scientific Programming with Python`: https://www.amazon.com/Scientific-Programming-Computational-Science-Engineering/dp/3662498863/ref=sr_1_4?ie=UTF8&qid=1542249635&sr=8-4&keywords=scientific+python
.. _`Learning Scientific Programming with Python`: https://www.amazon.com/Learning-Scientific-Programming-Python-Christian/dp/110742822X/ref=sr_1_3?ie=UTF8&qid=1542249635&sr=8-3&keywords=scientific+python
.. _`What will be covered`: https://github.com/josephcslater/Introduction_to_Python/blob/master/Introduction_to_Scientific_Python.ipynb
.. _`topics.rst`: topics.rst
.. _`docs/SETUP.rst`: docs/SETUP.rst
.. _`Lorena Barba's Numerical Python MOOC`: https://github.com/numerical-mooc/practical-numerical-methods
.. _`Python Plotting With Matplotlib`: https://realpython.com/python-matplotlib-guide/#pylab-what-is-it-and-should-i-use-it
.. _`Anaconda Python`: https://www.anaconda.com/download
.. _`uv`: https://docs.astral.sh/uv/getting-started/installation/
.. _`uv setup instructions`: docs/SETUP.rst#alternative-setup-with-uv
.. _`GitHub Desktop`: https://desktop.github.com/
.. _`the repository for this class in your web browser`: https://github.com/josephcslater/Introduction_to_Python
.. _`this class in mybinder.org`: https://mybinder.org/v2/gh/josephcslater/Introduction_to_Python/master
.. _`do this class in Jupyter Lab`: https://mybinder.org/v2/gh/josephcslater/Introduction_to_Python/master?urlpath=lab
