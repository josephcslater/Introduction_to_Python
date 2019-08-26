
Instructions for Introduction to Scientific Python
==================================================

.. bibliographic fields (which also require a transform):

:Author: Joseph C. Slater
:Address: 201 Clement Hall
          1010 N. Peachtree Avenue
          Tennessee Tech University
          Cookeville, TN 38505
:Contact: joseph.c.slater@gmail.com
:date: $Date: 2019-08-25 19:23:53 +0000 (Sunday, 25 August 2019) $
:status: This is a "work in progress"
:revision: $Revision: 1 $
:version: 1
:copyright: This document has been placed in the public domain. You
            may do with it as you wish. You may copy, modify,
            redistribute, reattribute, sell, buy, rent, lease,
            destroy, or improve it, quote it at length, excerpt,
            incorporate, collate, fold, staple, or mutilate it, or do
            anything else to it that your or anyone else's heart
            desires.
              
**If you can't get this to work, you can do much of** `this class in  mybinder.org`_.

To be able to execute all of the code I will demonstrate during the class, and to be able to write your own, please come prepared by installing Anaconda Python and the Github app per the instructionsin the sections below. 

.. contents:: **Table of Contents**
.. section-numbering::

`What will be covered`_? The rest will happen in class! (See that link, those are the actual class notes).

Installing Python
-----------------

- Students should have `Anaconda Python`_, Python version 3.5, 3.6, or 3.7, installed (64 bit is correct for any reasonably recent machine). **There won't be time to do this at the start of the short class!!!**

I may have an alternative live during the course, but it won't get your machine working!

- When doing this *also install Visual Studio Code*. It is an option near the end.

- Just install anything it asks you about.

- Users should install locally (not for all users) to keep things simple.

- All platforms (Mac, Windows, Linux) will be covered.

Platform Differences
--------------------

Windows Users
~~~~~~~~~~~~~

- Find the Anaconda Prompt application and run it.
- Type ``conda update --all``
- Type ``conda install cython``
- Type ``conda install numba``

Mac Users
~~~~~~~~~

- Find the ``Terminal.app``. It is located in your ``/Applications/Utilities`` folder.
  - Quick tip- command-key space-bar, then type 'Terminal' may launch it if Spotlight is set up correctly.
- Type ``conda update --all``
- Type ``conda install cython``
- Type ``conda install numba``

Linux Users
~~~~~~~~~~~

- Open your favorite terminal and type ``conda update --all``
- Type ``conda install cython``
- Type ``conda install numba``

Installing GitHub Desktop
-------------------------

I will want you to get things during the course from `GitHub <http://github.com>`_.

- Download `GitHub Desktop`_ and install it. You may need to create an account on GitHub.

  Linux Users:

  You will need to use `GitKraken`_.

  - Good News: It's much more powerful.
  - Bad News: It's much more complicated.

- Go to `the repository for this class in your web browser`_.
- You should be able to see a green button that says ``Clone or Download``. ``Clone`` is much better. This will allow you to update it in the future. Download means you reorganize each time. I suggest you create a folder ``GitHub`` in your Documents folder.

Loading and running my course locally
-------------------------------------

Mac Users
~~~~~~~~~

- Open your terminal application.
  - For Mac, look inside your ``Applications`` folder, inside ``Utilities`` and run ``Terminal``
  - On Linux, you likely already know which one you like.
- Move into the appropriate directory
  - Method 1. (Useful to learn, not necessary today)
    - Move into the appropriate directory.
      - This is done using the ``cd`` command. In the ``Finder`` go inside the folder with the cloned repository.
      - You know you are in the right place when you see ``Calc_Review.ipynb``.
      - Hold the ``Command`` key and click on the folder icon at the top of the window. It's to the left of ``Introduction_to_Python``.
      - This is your path. It will look something like ``/MyComputer/Users/Myname/GitHub/Introduction_to_Python``. It depends on a lot of decisions you've made in the past and presently.
      - Get the right names and type ``cd /MyComputer/Users/Myname/GitHub/Introduction_to_Python``.
      - There may be something like ``Documents`` or such embedded. You need to figure this path out.
      - Typing ``ls`` should provide a list of files that include ``Calc_Review.ipynb``
  - Method 2. (Quick way but lacking power)
    - In the GitHub Desktop (app), select the repository ``Introduction_to_Python``.
    - On the right it will provide options, one of which is ``open in terminal``.
    - This, plus the ``pwd`` command (present working directory) can tell you where everything is.
- Type ``jupyter notebook Introduction_to_Python.ipynb``

Linux Users
~~~~~~~~~~~

- Read the Mac instructions and tweak the names for linux. Unfortunately there is no GitHub Desktop for linux

Windows Users
~~~~~~~~~~~~~

- Open ``Anaconda Terminal``
- Move into the appropriate directory
  - Method 1. (Useful to learn, maybe not necessary today)
  - This is done using the ``cd`` command. In the ``File Explorer`` go inside the folder with the cloned repository.
  - You know you are in the right place when you see ``Calc_Review.ipynb``.
  - Near the top of the window you can see the entire path.
  - This is your path. It will look something like ``C:\MyComputer\Users\Myname\GitHub\Introduction_to_Python``. It depends on a lot of decisions you've made in the past and presently.
  - Get the right names and type ``cd C:\MyComputer\Users\Myname\GitHub\Introduction_to_Python``.
  - There may be something like ``Documents`` or such embedded. You need to figure this path out.
  - Typing ``dir`` should provide a list of files that include ``Calc_Review.ipynb``
- Method 2. (Quick way but lacking power)
- In the GitHub Desktop (app), select the repository ``Introduction_to_Python``.
- On the right it will (may- I haven't checked) provide options, one of which is ``open in Anaconda Terminal``.
- This, plus the ``cd`` command (cd both changes directory when there is a directory after it, or tells you the directory if there is not.) can tell you where everything is.
- Type ``jupyter notebook Introduction_to_Python.ipynb``


If we have time, we will learn a little Bokeh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are notes to myself... you might figure them out, you need to know how to hunt paths, though.

``bokeh serve /Users/jslater/Documents/python-dev/bokeh/examples/app/taylor.py``

``jupyter notebook /Users/jslater/Documents/python-dev/bokeh-notebooks/quickstart``

Other Educational Resources
---------------------------
- `Python Plotting With Matplotlib`_
- `Lorena Barba's Numerical Python Mooc`_
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
.. _`4th Edition`_: https://hplgit.github.io/primer.html/doc/pub/half/book.pdf
.. _`A Primer on Scientific Programming with Python`: https://www.amazon.com/Scientific-Programming-Computational-Science-Engineering/dp/3662498863/ref=sr_1_4?ie=UTF8&qid=1542249635&sr=8-4&keywords=scientific+python
.. _`Learning Scientific Programming with Python`: https://www.amazon.com/Learning-Scientific-Programming-Python-Christian/dp/110742822X/ref=sr_1_3?ie=UTF8&qid=1542249635&sr=8-3&keywords=scientific+python
.. _`What will be covered`: https://github.com/josephcslater/Introduction_to_Python/blob/master/Introduction_to_Scientific_Python.ipynb
.. _`class repository`: https://github.com/josephcslater/Introduction_to_Python
.. _`Lorena Barba's Numerical Python Mooc`: https://github.com/numerical-mooc/numerical-mooc
.. _`Python Plotting With Matplotlib`: https://realpython.com/python-matplotlib-guide/#pylab-what-is-it-and-should-i-use-it
.. _`Anaconda Python`: https://www.anaconda.com/download/#download
.. _`GitHub Desktop`: https://desktop.github.com/
.. _`GitKraken`: https://www.gitkraken.com/
.. _`the repository for this class in your web browser`: https://github.com/josephcslater/Introduction_to_Python
.. _`this class in  mybinder.org`: https://mybinder.org/v2/gh/josephcslater/Introduction_to_Python/master
