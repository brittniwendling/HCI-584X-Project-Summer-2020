# HCI-584X-Project-Summer-2020
HCI 584X Project: Summer 2020, Iowa State University,
Project: Study-based desktop application using Tkinter

Example of a project ReadMe (User’s guide)

Start with a simple description of what your project does. This here gives examples of 2 simple project file/folder structures:

main.py: imports from the stuff module (the local stuff.py file)
run_testpak.py: uses a simple package (called testpak) that can be installed via pip.
Requirements

List anything that the user needs to have to be able to run your program. Be as version-specific as you can b/c this will nail down what you used when it run for you, i.e. that the user can’t expect it to work with older versions. It’s ofc quite possible that this all should still work with newer versions.

Python 3.7 or higher
rich
dill 0.3 or higher
Installation

List what the user needs to do before running your app
for main.py

use pip to install the required third party packages: pip -r requirements.txt
for run_testpak.py

use pip to build and install testpack as a local package and install required packages
open a OS terminal, go into the project root folder and type: pip install . (<- dot!)
Usage

Describe how to run your app

main.py: run it in the project root folder, so it can import from the testpack folder
testpak.py: can be run from any folder once it’s been installed locally
Code Examples

If your project code is meant to be integrated into python code, you should list at least a few usage examples that can be copy/pasted and run. For more complex cases, consider writing a separate tutorial (put it and its code into a separate folder called tutorial).
Here, I’ll just give one of the functions that my package defines:

# use the evenOdd function
from testpak import evenOdd
x = int(input("Enter a number:"))
print(x, "is",  evenOdd(x))
Known issues

List any known bugs and limitations

Acknowledgments

If some project was instrumental in helping you with this project, consider listing it here.

How to markdown?

see https://guides.github.com/features/mastering-markdown/ for a guide on markdown.

Note that images need to be referenced, i.e. you will need to put them into a separate folder, here I’ve put an image into my docs folder:

Alt text for image

