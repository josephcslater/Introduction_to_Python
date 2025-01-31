.. image:: https://mybinder.org/badge.svg
    :target: https://mybinder.org/v2/gh/josephcslater/Introduction_to_Python/master?urlpath=lab

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
   :target: https://saythanks.io/to/joseph.c.slater@gmail.com

Instructions for Introduction to Scientific Python
==================================================

.. bibliographic fields (which also require a transform):

:Author: Joseph C. Slater
:Address: | Tennessee Tech University
          | Cookeville, TN 38505
:Contact: joseph.c.slater@gmail.com
:date: Date: 2019-08-25 19:23:53 +0000 (Sunday, 25 August 2019)
:status: This is a "work in progress"
:version: 1
:copyright: This document has been placed in the public domain. You
            may do with it as you wish. You may copy, modify,
            redistribute, reattribute, sell, buy, rent, lease,
            destroy, or improve it, quote it at length, excerpt,
            incorporate, collate, fold, staple, or mutilate it, or do
            anything else to it that your or anyone else's heart
            desires.

**If you can't get this to work, you can do much of** `this class in  mybinder.org`_. There is more than one notebook (ends with ``.ipynb``) in the repository. Once the virtual machine launches, select the one you are interested in.

**WARNING**: Failure to put thing in the right place will very likely result in you not being able to make sense of the rest of the instructions and getting a working system in time. **Please install things in the expected locations!**

**More full-featured, you can** `do this class in Jupyter Lab`_.

How did I do this? `binder`_.

To be able to execute all of the code I will demonstrate during the class, and to be able to write your own, please come prepared by installing `Anaconda Python`_ and `Github Desktop`_ per the instructions in the sections below.

.. contents:: **Table of Contents**
.. section-numbering::

`What will be covered`_? The rest will happen in class! (See that link, those are the actual class notes).

Installing Scientific Python
----------------------------

I may have an alternative live during the course, but it won't get your machine working!

1. Students should have `Anaconda Python`_, Python version 3.7 or later installed (64 bit is correct for any reasonably recent machine). **There won't be time to do this at the start of the short class!!!**

2. When doing this *also install Visual Studio Code* if the option is available. It is an option near the end. If not, don't worry about it. It's not necessary.

3. Just install anything it asks you about.

4. Users **must install locally (not for all users)** to keep things simple. *There is no benefit in installing for all users unless you truly have multiple people using the same machine. There is a cost of installing for all users- later updates and installations are much harder.*

Installing `GitHub Desktop`_ (you'll need this to get my notes)
---------------------------------------------------------------

- **Windows and Mac**: Download `GitHub Desktop`_ and install it. You may need to create an account on `GitHub.com`_ .

- **Linux users**: Follow the MacOS instructions. The Mac is unix too. [#]_

  - You will need to use `GitKraken`_.

    - Good News: It's much more powerful.

    - Bad News: It's much more complicated.

    - I need to leave it to you to read up on how to use it. I'll try to add instructions later.

- Go to `the repository for this class in your web browser`_.

- You should be able to see a green button that says ``Clone or Download``. ``Clone``. **You do not want download as it will prevent me from being able to help you should things go wrong.** This will allow you to update it in the future. Download means you start from scratch each time.

- Please allow the`GitHub Desktop`_ to **create the folder GitHub in your Documents folder. Trust me. You will want it there eventually, and moving it later creates a lot of unnecessary headaches.** If you really dig in, you can figure it out. I have. I didn't do this on my personal machine and still regret it. There is NO benefit to not going with the default. **GO WITH THE DEFAULT LOCATION**.


Platform Differences
--------------------

Fundamentally, theses instructions are the same. The challenge is most users may not have used a terminal before.
Further, Anaconda sets up your terminal to work well for you.

These are step-by-step to walk you through what needs to happen in the terminal for each platform.

Windows Users
~~~~~~~~~~~~~

- Find the Anaconda Prompt application and run it. Answer *yes* to all prompts. Don't do anything it advises against.
- Type ``conda update --all``
- Open ``Anaconda Prompt``
- You need to get to the right directory in ``Anaconda Prompt``. There are two methods. The first is better long-term. The second is faster to get started. It's about learning the command line.

  - Method 1. (Useful to learn, maybe not necessary today)

    - Move into the appropriate directory.

      - This is done using the ``cd`` command. In the ``File Explorer`` go inside the folder with the cloned repository.

      - You know you are in the right place when you see ``Calc_Review.ipynb``.

      - Near the top of the window you can see the entire path.

      - This is your path. It will look something like ``C:\MyComputer\Users\Myname\GitHub\Introduction_to_Scientific_Python``. It depends on a lot of decisions you've made in the past and presently. You can right click and copy this path.

      - Get the right names and type ``cd `` *path from above*. This is all one line. The *path from above* is exactly what you read off the top of your window two bullets above.

      - Typing ``dir`` should provide a list of files that include ``Calc_Review.ipynb``

  - Method 2. (Quick way but lacking power)

    - In the `GitHub Desktop`_ (app), select the repository ``Introduction_to_Python``.

    - On the right it will (may- I haven't checked) provide options, one of which is ``open in Anaconda Prompt``.

    - This, plus the ``cd`` command (cd both changes directory when there is a directory after it, or tells you the directory if there is not.) can tell you where everything is.
- Type ``conda env update --file environment.yml``

- Get to this directory when you want to run the course material (maybe now, maybe later) and type:

  - ``jupyter notebook Introduction_to_Scientific_Python.ipynb``, or for a more sophisticated environment,

  - ``jupyter lab Introduction_to_Scientific_Python.ipynb`` (interaction is less reliable, I've found).


Mac Users
~~~~~~~~~

- Find the ``Terminal.app``. It is located in your ``/Applications/Utilities`` folder. Answer *yes* to all prompts.

  - Quick tip- command-key space-bar, then type 'Terminal' may launch it if Spotlight is set up correctly.

- Type ``conda update --all``
- Open your terminal application.

  - For Mac, look inside your ``Applications`` folder, inside ``Utilities`` and run ``Terminal``

  - On Linux, you likely already know which one you like (or why are you using Linux?).

- Move into the appropriate directory

  - Method 1. (Useful to learn, not necessary today)

    - Move into the appropriate directory.

      - This is done using the ``cd`` command. In the ``Finder`` go inside the folder with the cloned repository.

      - You know you are in the right place when you see ``Calc_Review.ipynb``.

      - Hold the ``Command`` key and click on the folder icon at the top of the window. It's to the left of ``Introduction_to_Python``.

      - This is your path. It will look something like ``/MyComputer/Users/Myname/GitHub/Introduction_to_Python``. It depends on a lot of decisions you've made in the past and presently.

      - Get the right names and type ``cd /MyComputer/Users/Myname/GitHub/Introduction_to_Python``.

      - There may be something like ``Documents`` or such embedded. You need to figure this path out.

      - Typing ``ls`` should provide a list of files that include ``Calc_Review.ipynb`` and ``Introduction_to_Scientific_Python.ipynb``.

  - Method 2. (Quick way but lacking power)

    - In the `GitHub Desktop`_ (app), select the repository ``Introduction_to_Python``. (sorry- I have some inconsistencies where "Scientific" is missing. I cannot fix them without breaking things.)

    - On the right it will provide options, one of which is ``open in terminal``.

    - This, plus the ``pwd`` command (present working directory) can tell you where everything is.

- Type ``conda env update --file environment.yml``

- Get to this same directory when you want to run the course material (maybe now, maybe later) and type one of:

  - ``jupyter notebook Introduction_to_Scientific_Python.ipynb``, or for a more sophisticated environment,

  - ``jupyter lab Introduction_to_Scientific_Python.ipynb`` (interaction is less reliable, I've found).

- I've found that some Mac configurations have problems. See `setting up an environment`_ which shows how to do this for an environment named ``controls``. You will want to name it something like ``latest``, as in *I always update ot the latest versions here*.

If we have time, we will learn a little Bokeh (probably not, but I can dream)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are notes to myself. You might figure them out, you need to know how to hunt paths, though.

``bokeh serve /Users/jslater/Documents/python-dev/bokeh/examples/app/taylor.py``

``jupyter notebook /Users/jslater/Documents/python-dev/bokeh-notebooks/quickstart``

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

.. _`binder`: https://mybinder.org
.. _`SciPy Cookbook`: https://scipy-cookbook.readthedocs.io/
.. _`Generic Python Introduction`: https://github.com/guntukukamal/Good-python-reference
.. _`SciPy Lecture Notes`: https://github.com/scipy-lectures/scipy-lecture-notes
.. _`4th Edition`: https://hplgit.github.io/primer.html/doc/pub/half/book.pdf
.. _`A Primer on Scientific Programming with Python`: https://www.amazon.com/Scientific-Programming-Computational-Science-Engineering/dp/3662498863/ref=sr_1_4?ie=UTF8&qid=1542249635&sr=8-4&keywords=scientific+python
.. _`Learning Scientific Programming with Python`: https://www.amazon.com/Learning-Scientific-Programming-Python-Christian/dp/110742822X/ref=sr_1_3?ie=UTF8&qid=1542249635&sr=8-3&keywords=scientific+python
.. _`What will be covered`: https://github.com/josephcslater/Introduction_to_Python/blob/master/Introduction_to_Scientific_Python.ipynb
.. _`class repository`: https://github.com/josephcslater/Introduction_to_Python
.. _`Lorena Barba's Numerical Python MOOC`: https://github.com/numerical-mooc/numerical-mooc
.. _`Python Plotting With Matplotlib`: https://realpython.com/python-matplotlib-guide/#pylab-what-is-it-and-should-i-use-it
.. _`Anaconda Python`: https://www.anaconda.com/download/#download
.. _`GitHub Desktop`: https://desktop.github.com/
.. _`GitKraken`: https://www.gitkraken.com/
.. _`the repository for this class in your web browser`: https://github.com/josephcslater/Introduction_to_Python
.. _`this class in mybinder.org`: https://mybinder.org/v2/gh/josephcslater/Introduction_to_Python/master
.. _`do this class in Jupyter Lab`: https://mybinder.org/v2/gh/josephcslater/Introduction_to_Python/master?urlpath=lab
.. _`setting up an environment`: https://github.com/josephcslater/Tennessee_Tech_ECE_3210_public/blob/master/controls_environment.rst
.. _`GitHub.com`: https://github.com/join

.. [#] In fact, linux isn't actually unix.
