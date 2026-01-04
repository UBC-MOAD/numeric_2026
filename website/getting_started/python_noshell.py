# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:percent
#     notebook_metadata_filter: all,-language_info,-toc,-latex_envs
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Other Resources #
#
# ## Books and tutorials
#
#   - We will be referring to Phil Austin's version of  David Pine's Introduction to Python:
#     http://phaustin.github.io/pyman.  The notebooks for each chapter are included
#     in the [numeric_students/pyman](https://github.com/phaustin/numeric_students/tree/downloads/pyman) folder.
#   - If you are new to python, I would recommend you also go over the
#     following short ebook in detail:
#       - Jake Vanderplas' [Whirlwind tour of
#         Python](https://github.com/jakevdp/WhirlwindTourOfPython/blob/f40b435dea823ad5f094d48d158cc8b8f282e9d5/Index.ipynb)
#         is available both as a set of notebooks which you can clone from
#         github or as a free ebook:
#         <http://www.oreilly.com/programming/free/a-whirlwind-tour-of-python.csp>
#           - to get the notebooks do:
#             
#             git clone <https://github.com/jakevdp/WhirlwindTourOfPython>
#   - We will be referencing chapters from:
#       - A Springer ebook from the UBC library: [Numerical
#         Python](https://login.ezproxy.library.ubc.ca/login?qurl=https%3a%2f%2flink.springer.com%2fopenurl%3fgenre%3dbook%26isbn%3d978-1-4842-0554-9)
#           - with code on github:
#             
#             git clone
#             <https://github.com/jrjohansson/numerical-python-book-code>
#   - Two other texts that are available as a set of notebooks you can
#     clone with git:
#       - <https://github.com/fangohr/introduction-to-python-for-computational-science-and-engineering>
#       - <https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/Index.ipynb>
#   - My favorite O'Reilly book is:
#       - [Python for Data
#         Analysis](http://shop.oreilly.com/product/0636920023784.do)
#   - Some other resources:
#       - If you know Matlab, there is [Numpy for Maltab
#         users](http://wiki.scipy.org/NumPy_for_Matlab_Users)
#       - Here is a [python
#         translation](http://nbviewer.jupyter.org/gist/phaustin/1af744215e51562d010b9f6a19c0724c)
#         by [Don
#         MacMillen](http://blogs.siam.org/from-matlab-guide-to-ipython-notebook/)
#         of [Chapter 1 of his matlab
#         guide](http://clouds.eos.ubc.ca/~phil/courses/atsc301/downloads_pw/matlab_guide_2nd.pdf)
#       - [Numpy beginners
#         guide](http://www.packtpub.com/numpy-mathematical-2e-beginners-guide/book)
#       - [Learning
#         Ipython](http://www.packtpub.com/learning-ipython-for-interactive-computing-and-data-visualization/book)
#       - [The official Python
#         tutorial](http://docs.python.org/tut/tut.html)
#       - [Numpy
#         cookbook](http://www.packtpub.com/numpy-for-python-cookbook/book)
#       - A general computing introduction: [How to think like a computer
#         scientist](http://www.openbookproject.net/thinkcs/python/english3e)
#         with an [interactive
#         version](http://interactivepython.org/courselib/static/thinkcspy/index.html)
#       - [Think Stats](http://greenteapress.com/wp/think-stats-2e/)
#       - [Think Bayes](http://greenteapress.com/wp/think-bayes/)

# %% [markdown]
# ## Optional: VScode ##
#
# If you are more familiar with jupyter notebooks, you may wish to explore running them on your laptop (instead of in Jupyter Open). VSCode is a code editor, which many people find helps them code better, debug faster, and keep good coding practices. Some of the strengths of VSCode for editing notebooks include its real editor powers: spellchecking and multiple corrections. We will not go through VSCode in much detail in this course, but here are some resources if you are interested, and you are welcome to ask us: 
#
# ### Install vscode from https://code.visualstudio.com/download
#
# Install the command line version as well. On windows, this should be done as part of the install.  On MacOS, you need to open the vscode command pallette (&#8984;shift-P) and type
# ```
# Shell Command: Install code in PATH
# ```
#
# once that is done, you should be able to start vscode from the command line in a particular
# folder by typing:
#
# ```
# code .
# ```
#
# ### Suggested Extensions 
#
# On the left you will see four boxes, one moved up.  Here you can add extensions.  You will need some just to run notebooks etc.  We suggest:
# - Python
# - Pylance (this one installed with Python for me)
# - Jupyter (again came with Python for me)
# - C/C++
# - Clipboard
# - Code Spell Checker
# - Gitlens
#
# ### Notebooks 
#
# The notebooks (labs) for this course are not VSCode ready - if you do use VScode for the labs, you will see non-rendered pieces.  Technology changes and we are always behind.
#
# ###  Features 
#
# Some of the super features of editing in VScode including:
# - code colouring
# - built in information on functions
# - click on variable, see everywhere it is used
# - checks alignment (whitespace)
# - marks changes you've made
# - typo in variable leading to undefined
# - undefined function: colour changes to white
# - making a change, then using the git integration to save, stage and commit
#

# %%
