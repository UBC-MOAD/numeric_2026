# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
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

# %% [markdown] trusted=true
# # Student installs
#
# **If you already have conda or anaconda installed, skip to `Git install` below**
#
#
#
# ## For MacOS new installs
#
#
# 1. Download miniconda from  https://docs.conda.io/en/latest/miniconda.html  -- choose the correct `Miniconda3 MacOSX 64-bit pkg` file for your Mac (Intel chip or new M1/M2 Silicon) from the menu and run it, agreeing to the licences and accepting all defaults. You should install for "just me"
#
# 2. To test your installation, open a fresh terminal window and at the prompt type `which conda` (unless you are using zsh.  In that case use `whence -p conda`).  You should see something resembling the following output, with your username instead of `phil`:
#
# ```
# % which conda
# /Users/phil/opt/miniconda3/bin/conda
# ```
#
# ## For Windows new installs
#
# 1. Download miniconda from  https://docs.conda.io/en/latest/miniconda.html  -- choose the `Miniconda3 Windows 64-bit`. download from the menu and run it, agreeing to the licences and accepting all defaults.
#
# The installer should suggest installing in a path that looks like:
#
# ```
# C:\Users\phil\Miniconda3
# ```
#
# 2. Once the install completes hit the windows key and start typing `anaconda`.  You should see a shortcut that looks like:
#
# ```
# Anaconda Powershell Prompt
# (Miniconda3)
# ```
#
# **Note that Windows comes with two different terminals `cmd` (old) and `powershell` (new).  Always select the powershell version of the anaconda terminal**
#
# 3. Select the short cut.  If the install was successful you should see something like:
#
# ```
# (base) (Miniconda3):Users/phil>
# ```
# with your username substituted for phil.
#
# Some useful troubleshooting websites if you have issues getting conda installed on windows: 
# https://stackoverflow.com/questions/54501167/anaconda-and-git-bash-in-windows-conda-command-not-found
# https://stackoverflow.com/questions/44597662/conda-command-is-not-recognized-on-windows-10
#
# ## Git install
#
# Inside your powershell or MacOs terminal, install git using conda:
#
# ```
# conda install git
# ```
#
# and then set it up
#
# ```
# git config --global user.name "Phil"
# git config --global user.email phil@example.com
# ```
#
# ## Github account
#
# To use the course materials and to work collaboratively for the project, you will need a github account.  Sign up for a free account at https://github.com if you don't already have one - you will need to use the same address you configured git for above. 
#
# Once you have your github account, you will need to set up a secure way to connect. If you think you might use github a lot, we recommend setting up an ssh connection - this is a longer set-up process, but then quicker each time you want to connect to git. Follow the instructions here: 
#
# https://docs.github.com/en/authentication/connecting-to-github-with-ssh
#
# A quicker set-up is to create a Personal Access Token. Follow the instructions here:
# https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic
#
# Once you have a personal access token, you can enter it instead of your password when performing Git operations over HTTPS (see https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#using-a-personal-access-token-on-the-command-line). 
#
# ## Fork the course repository into your github account
#
# Now go to the course website at https://github.com/rhwhite/numeric_2024 and fork the repository.  The 'fork' button is on the upper right. This creates a 'fork' or copy of the current status of the repository in your account. 
#
# You now have your own fork of the course repository and should be taken to that page.  Its name will be YourGitHubId/numeric_2024
#
# ## Setting up the course repository
#
# In the terminal, change directories to your home directory (called `~` for short) and make a new directory
# called `repos` to hold the course notebook repository.  Change into `repos` and clone the course (do change YourGitHubId to your actual git hub id):
#
# ```
# cd ~
# mkdir repos
# cd repos
# git clone https://github.com/YourGitHubId/numeric_2024.git
# ```
#
# ## Creating the course environment
#
# In the terminal, execute the following commands:
#
# ```
# cd numeric_2024
# conda env create -f envs/environment.yaml
# conda activate numeric_2024
# ```
#
# ## Opening the notebook folder and working with lab 1
#
# To make it possible to pull down changes to the repository (for example, as I write this section only lab1 and lab2 are available) you need to work in a copy of the notebook.  So always copy the notebook to a new name. See below an example for lab1.  I suggest you use your name rather than phil!
#
# ```
# cd ~/repos/numeric_2024/notebooks
# cp lab1/01-lab1.ipynb lab1/phil-lab1.ipynb
# jupyter lab
# ```
#

# %% trusted=true
