Detailed Setup Instructions
===========================

This document covers the full, step-by-step installation and platform-specific
instructions referenced from the main `README.rst`_. If you just want the
quick start (or would rather run everything in the cloud), see the README
first.

.. contents:: **Table of Contents**
.. section-numbering::

Installing Scientific Python
-----------------------------

I may have an alternative live during the course, but it won't get your machine working!

1. Students should have `Anaconda Python`_, Python version 3.7 or later installed (64 bit is correct for any reasonably recent machine). **There won't be time to do this at the start of the short class!!!**

2. When doing this *also install Visual Studio Code* if the option is available. It is an option near the end. If not, don't worry about it. It's not necessary.

3. Just install anything it asks you about.

4. Users **must install locally (not for all users)** to keep things simple. *There is no benefit in installing for all users unless you truly have multiple people using the same machine. There is a cost of installing for all users- later updates and installations are much harder.*

Installing `GitHub Desktop`_ (you'll need this to get my notes)
-----------------------------------------------------------------

- **Windows and Mac**: Download `GitHub Desktop`_ and install it. You may need to create an account on `GitHub.com`_ .

- **Linux users**: Follow the MacOS instructions. The Mac is unix too. [#]_

  - You will need to use `GitKraken`_.

    - Good News: It's much more powerful.

    - Bad News: It's much more complicated.

    - I need to leave it to you to read up on how to use it. I'll try to add instructions later.

- Go to `the repository for this class in your web browser`_.

- You should be able to see a green button that says ``Clone or Download``. ``Clone``. **You do not want download as it will prevent me from being able to help you should things go wrong.** This will allow you to update it in the future. Download means you start from scratch each time.

- Please allow `GitHub Desktop`_ to **create the folder GitHub in your Documents folder. Trust me. You will want it there eventually, and moving it later creates a lot of unnecessary headaches.** If you really dig in, you can figure it out. I have. I didn't do this on my personal machine and still regret it. There is NO benefit to not going with the default. **GO WITH THE DEFAULT LOCATION**.


Platform Differences
----------------------

Fundamentally, theses instructions are the same. The challenge is most users may not have used a terminal before.
Further, Anaconda sets up your terminal to work well for you.

These are step-by-step to walk you through what needs to happen in the terminal for each platform.

Alternative Setup with uv
~~~~~~~~~~~~~~~~~~~~~~~~~~

The Anaconda setup above is recommended for beginners. Anaconda provides a
guided installer, Anaconda Prompt, and the compiler support needed by the
Fortran notebook cells. The ``uv`` setup is a good alternative if you are
already comfortable using a terminal and virtual environments.

Install `uv`_ using its `installation instructions`_, then open a terminal in
the repository directory and run::

  uv venv --python 3.12

Activate the virtual environment. On macOS or Linux, run::

  source .venv/bin/activate

On Windows PowerShell, run::

  .venv\Scripts\Activate.ps1

Install the project dependencies and launch Jupyter Lab::

  uv pip install -r requirements-uv.txt
  jupyter lab Introduction_to_Scientific_Python.ipynb

The ``%%fortran`` notebook cells also require a system ``gfortran`` compiler.
Installing that compiler is a separate operating-system task when using
``uv``; the Anaconda environment handles it through ``environment.yml``.

Windows Users
~~~~~~~~~~~~~~

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
- Type ``conda env create --file environment.yml``
- Type ``conda activate introduction-to-python``

- Get to this directory when you want to run the course material (maybe now, maybe later) and type:

  - ``jupyter notebook Introduction_to_Scientific_Python.ipynb``, or for a more sophisticated environment,

  - ``jupyter lab Introduction_to_Scientific_Python.ipynb`` (interaction is less reliable, I've found).


Mac Users
~~~~~~~~~~

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

- Type ``conda env create --file environment.yml``
- Type ``conda activate introduction-to-python``

- Get to this same directory when you want to run the course material (maybe now, maybe later) and type one of:

  - ``jupyter notebook Introduction_to_Scientific_Python.ipynb``, or for a more sophisticated environment,

  - ``jupyter lab Introduction_to_Scientific_Python.ipynb`` (interaction is less reliable, I've found).

- I've found that some Mac configurations have problems. See `setting up an environment`_ which shows how to do this for an environment named ``controls``. You will want to name it something like ``latest``, as in *I always update ot the latest versions here*.

Troubleshooting
---------------

``findfont: Font family '...' not found`` warnings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you see repeated ``findfont: Font family 'xkcd'/'Comic Sans MS'/...
not found`` messages when running the ``plt.xkcd()`` demo, this is
harmless: it just means matplotlib could not find a comic-style font on
your system (or in its own font cache) and fell back to the default
font for text. The notebook already silences these messages for you.
The characteristic hand-drawn, wobbly-line look of ``plt.xkcd()`` does
not depend on the font at all, so the plot itself is unaffected either
way.

If you would like the plot *text* to also render in a comic-style font,
install a font such as `xkcd Script`_ or ``Comic Sans MS`` on your
system, then delete matplotlib's font cache folder (run
``python -c "import matplotlib; print(matplotlib.get_cachedir())"`` to
find it) and restart the kernel so matplotlib notices the new font.

.. _`xkcd Script`: https://github.com/ipython/xkcd-font

If we have time, we will learn a little Bokeh (probably not, but I can dream)
--------------------------------------------------------------------------------

These are notes to myself. You might figure them out, you need to know how to hunt paths, though.

``bokeh serve /Users/jslater/Documents/python-dev/bokeh/examples/app/taylor.py``

``jupyter notebook /Users/jslater/Documents/python-dev/bokeh-notebooks/quickstart``

.. _`README.rst`: ../README.rst
.. _`Anaconda Python`: https://www.anaconda.com/download
.. _`uv`: https://docs.astral.sh/uv/getting-started/installation/
.. _`installation instructions`: https://docs.astral.sh/uv/getting-started/installation/
.. _`GitHub Desktop`: https://desktop.github.com/
.. _`GitKraken`: https://www.gitkraken.com/
.. _`the repository for this class in your web browser`: https://github.com/josephcslater/Introduction_to_Python
.. _`setting up an environment`: https://github.com/josephcslater/Tennessee_Tech_ECE_3210_public/blob/master/controls_environment.rst
.. _`GitHub.com`: https://github.com/join

.. [#] In fact, linux isn't actually unix.
