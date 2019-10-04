# ann dynamical systems

For my master thesis i need to approximate the dynamical behaviour of an airplane. The artifical neural networks will be saved here.

I use google colab as my development environment which is a extension on Jupyter Notebooks. But it will also run in a normal jupyter enviroment.

## google colab
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CrowdSalat/ann-dynamical-systems/blob/master/explore_xplane_data.ipynb)

## jupyter notebook

### usage

In project folder:

1. activate the enviroment: ``source env/bin/activate``
2. start the jupyter notebook: ``jupyter notebook``

*Further pip statements will be in the jupyter notebooks. Alternativly use ``pip3 install -r requirements.txt``* *. The requirements file was created with: ``pip freeze > requirements.txt``*

### installation

In this installation example jupyter will be installed inside of a virtual enviroment.

So if not installed, install pip3 and virtualenv:

1. ``sudo apt-get install python3-pip``
2. ``sudo pip3 install virtualenv``

*Use sudo before pip or it wont appear on the PATH*  

To create virtualenv and install jupyter execute the following commands in the project folder:

1. create virtualenv:   ``virtualenv env``
2. Activate it with:    ``source env/bin/activate``
3. Install Jupyter:     ``pip3 install jupyter``
