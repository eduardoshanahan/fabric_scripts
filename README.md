# Fabric Scripts

This is a group of [Python Fabric](http://www.fabfile.org/) scripts to interact with Ubuntu servers, in particular [Vagrant](https://www.vagrantup.com/) and EC2 instances.

I grew tired of copying files around for each project (and then losing track of what was updated where), and did a bit of research on how to use [submodules in Git](http://git-scm.com/book/en/v2/Git-Tools-Submodules) (which is pretty straight forward).

I am far from being a SysAdmin, and that is reflected in the quality of the scripts, but in some cases they are doing the trick (for my customers at least).

The way in which I use them is to add this project as a submodule in git, and then create a fabfile.py in my parent directory with the content

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
