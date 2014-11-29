# Fabric Scripts

This is a group of [Python Fabric](http://www.fabfile.org/) scripts to interact with Ubuntu servers, in particular [Vagrant](https://www.vagrantup.com/) and EC2 instances.

I grew tired of copying files around for each project (and then losing track of what was updated where), and did a bit of research on how to use [submodules in Git](http://git-scm.com/book/en/v2/Git-Tools-Submodules) (which is pretty straight forward).

I am far from being a SysAdmin, and that is reflected in the quality of the scripts, but in some cases they are doing the trick (for my customers at least).

The way in which I use them is to add this project as a submodule in git, and then create a fabfile.py in my parent directory with the content: 

```python
from fabric_scripts import scripts
```
Then, when I do a `fab -l` in my directory, I get a list in the form of:

```
EduardoMacBookPro:vagrant_research eduardoshanahan$ fab -l

Available commands:	

	scripts.call_vagrant                        Contact a Vagrant instance
	scripts.development.tools.install           Get some tools
	scripts.docker.install                      Install Docker.io
```

# Tools that I use in my development machine

* Python 2.7

Make sure that you aim to the right version. In the Mac I managed to have three different 2.7* versions, and who knows which one is being used each time. Now and then I do a cleanup and remove what I don't think I need, but somehow more versions appears after a while. The problem is that some Python tools (like pip, or Fabric) sometimes get assigned to the wrong version, and doesn't work although they are installed. Specifying the path usually sort the problem, but it is only a hack. Ubuntu is a lot more stable.

`python --version` should say something like `Python 2.7.8`
`which python` will tell you where is the binary, something like `/usr/local/bin/python`

* Python-dev

In some cases (as in Suse machines) the python-dev package has to be installed for Pip to compile. 

* [Python Pip](http://pip.readthedocs.org/en/latest/installing.html)

Pip is a Python package manager. It basically makes your life easier when you need some third party tool. Installation instructions are on the link.

`pip --version` should answer `pip 1.5.6 ...`

* [Virtual Box](http://www.virtualbox.org/manual/ch01.html#intro-installing)

[Download a version](https://www.virtualbox.org/wiki/Downloads) for your operating system and install it as any other application. Install the extension pack too (it will be asked the first time you run the UI).

After being installed, create a machine using the user interface, to make sure that VB is working fine (this step will require an ISO file for an operating system). You should be able to start and stop the instance, and to connect to it. If you are confident, you can skip the test and jump straigth to Vagrant, but if something bombs you will have to come back and ensure that VirtualBox is working properly.

* [Vagrant](https://docs.vagrantup.com/v2/installation/)

Vagrant creates and fire up instances using Virtual Box. It is easy to configure and cheap in machine resources (I run between three to five instances most of the day in an I7/8GB Mac without troubles)

`vagrant version` should answer with `Vagrant 1.6.5` or more.

* [Pip](http://pip.readthedocs.org/en/latest/installing.html)

Just follow the instrucctions on the page.


* [Boto](https://pypi.python.org/pypi/boto/)

`pip install boto' should be enough.

* [Python Fabric](http://www.fabfile.org/installing.html)

I installed Fabric using pip (`pip install fabric`). After all is done, a call for `fab --version` should answer `Fabric 1.10.0 or newer`.

After all the tools are installed, we are going to script the whole deployment makingFabric scripts. In the case of Vagrant, after the machine is fired up, you can install tools automatically, and doing that will require extra Vagrant tools. With an Ubuntu host, you might need a [plugin](https://github.com/wutali/vagrant-fabric) to do provisioning from Fabric

This covers all the basic tools we are going to use. Lets talk tomorrow to see if there are any problems during installation.


## [Vagrant plugin](https://github.com/wutali/vagrant-fabric)

To have the machine doing automatic provisioning, we will probably need a plugin in Vagrant to understand how to work with Fabric. After checking that everything works as expected between VirtualBox, Vagrant and Fabric, run the following command:

`vagrant plugin install vagrant-fabric`

## Working with the Vagrant machine

With all the tools installed, and the code retrieved from git:

`cd /code/deployment/vagrant`
`vagrant up`

should be working for a while, and eventually finish with a message about mounting shared folders.

If there are no big errors (right now I am getting two warnings about Virtual Box Guest Additions, although I am sure that is ok in my machine), you should be able to do an

`vagrant ssh' and get a shell session to the new machine. 

`ls` should show the directory `code`, because the vagrantfile is saying that the `/code` directory are shared with the virtual instance. `exit` will get you back in your local machine.

As a first step into deployment, lets try `fab vagrant install_tools`.
