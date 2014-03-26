#!/bin/bash
# Simple setup.sh for configuring Ubuntu 12.04 LTS EC2 instance
# for headless setup. 

# Install nvm: node-version manager
# https://github.com/creationix/nvm
sudo apt-get install -y git
sudo apt-get install -y curl
curl https://raw.github.com/creationix/nvm/master/install.sh | sh

# Load nvm and install latest production node
source $HOME/.nvm/nvm.sh
nvm install v0.10.12
nvm use v0.10.12

# Install jshint to allow checking of JS code within emacs
# http://jshint.com/
npm install -g jshint

# Install rlwrap to provide libreadline features with node
# See: http://nodejs.org/api/repl.html#repl_repl
sudo apt-get install -y rlwrap

# Install emacs24
# https://launchpad.net/~cassou/+archive/emacs
sudo add-apt-repository -y ppa:cassou/emacs
sudo apt-get -qq update
sudo apt-get install -y emacs24-nox emacs24-el emacs24-common-non-dfsg

# Install Heroku toolbelt
# https://toolbelt.heroku.com/debian
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh

# git pull and install dotfiles as well
cd $HOME
if [ -d ./dotfiles/ ]; then
    mv dotfiles dotfiles.old
fi
if [ -d .emacs.d/ ]; then
    mv .emacs.d .emacs.d~
fi
git clone https://github.com/jaime-e/dotfiles.git
ln -sb dotfiles/.screenrc .
ln -sb dotfiles/.bash_profile .
ln -sb dotfiles/.bashrc .
ln -sb dotfiles/.bashrc_custom .
ln -sf dotfiles/.emacs.d .

#instalar cheerio para html en servidor
npm install cheerio

#instalar restler  http client library
npm install restler

#instalar pip para manejar paquetes de piython
sudo apt-get install python-pip

#instalar mechanize
sudo pip intall mechanize

#instalar beautifulsopup
sudo pip install beautifulsoup4

#instalar igraph
sudo aptitude install build-essential libxml2-dev libglpk-dev libgmp3-dev libblas-dev liblapack-dev libarpack2-dev python-dev

wget http://switch.dl.sourceforge.net/sourceforge/igraph/igraph-0.5.4.tar.gz
wget http://pypi.python.org/packages/source/p/python-igraph/python-igraph-0.5.4.tar.gz
tar xzf python-igraph-0.5.4.tar.gz
tar xzf igraph-0.5.4.tar.gz

cd igraph-0.5.4
./configure
make
sudo make install

echo "export LD_LIBRARY_PATH=/usr/local/lib/" >> ~/.bashrc 
sudo apt-get install radiance
sudo apt-get install graphviz

cd ~/
cd python-igraph-0.5.4
python setup.py build
sudo python setup.py install

#instalar xlrd
sudo pip install xlrd
