---
layout: post
title:  "Setting up a Python and Postgres development environment using Vagrant"
description: "A guide to setting up a new Vagrant virtual environment with Python and Postgres"
date:   2016-11-19 12:00:00 +0000
canonical: "https://medium.com/jean-marcs-thoughts/setting-up-a-python-and-postgres-development-environment-using-vagrant-97554874c834"
categories: programming
thumbnail: posts/vagrant.png
thumbnail-background: "#277b45"
---

It can always be a little annoying getting a fresh new work environment running. This guide is my attempt to keep track of how to get running as quickly as possible.

We’ll be using Vagrant, so these instructions should work with pretty much every development environment out there. I’m running this on a PC at the moment, but the same guide should work with Mac or Linux environments as well.

## 1. Setting up Vagrant

Start by downloading and installing the latest version of Vagrant. Installation should be pretty straightforward, and at the end you should have access to the *vagrant* command from the CLI.

The default approach is to initialize a bare-bones version of ubuntu and to build it up from there. The way to do this as of now is with the following two commands:

~~~
$ vagrant init hashicorp/precise64
$ vagrant up
~~~

We’ll be doing things a little differently because of Postgres. While it would be totally doable to install Postgres manually after initializing a barebones version of Ubuntu, [the following configuration](https://wiki.postgresql.org/wiki/PostgreSQL_For_Development_With_Vagrant) speeds things up considerably

~~~
# Clone the repository:
$ git clone https://github.com/jackdb/pg-app-dev-vm myapp

# Remove the .git, README, and LICENSE files:
$ cd myapp
$ rm -rf .git README.md LICENSE
$ vagrant up
~~~

You’ll likely want to make a few tweaks to the provided Vagrantfile after everything is set up. After calling…

~~~
$ vagrant halt
~~~

… I went ahead and changed the following two lines

~~~
# Disable original shared folder 
# config.vm.share_folder "bootstrap", "/mnt/bootstrap", ".", :create => true
# Set up new share, mapping vagrant folder to ~ within environment
config.vm.share_folder "home", "/home/vagrant", ".", :create => true
# Disable PostgreSQL Server port forwarding
# config.vm.forward_port 5432, 15432
# Enable web server port forwarding
config.vm.forward_port 8000, 8000
~~~

## 2. Setting up Postgres

Now that Postgres is set up, let’s go about creating a new database and account for it:

~~~
$ sudo su - postgres
$ psql
# CREATE USER app_local WITH PASSWORD 'app_local';
# CREATE DATABASE db_local;
# GRANT ALL PRIVILEGES ON DATABASE db_local TO app_local;
~~~

## 3. Setting up the Python environment

The next step is to install Virtualenv, which simplifies the process of managing Python libraries significantly. Start by installing the required packages

~~~
sudo apt-get install python-pip python-dev build-essential
~~~

Once this is in place, we can go about installing virtualenv

~~~
sudo pip install virtualenv virtualenvwrapper
~~~

We should update pip to the latest version prior to setting up our virtualenv environment

~~~
sudo pip install --upgrade pip
~~~

In order to use virtualenvwrapper, we need to modify our bashrc file. Make sure to keep a copy in case anything goes wrong:

~~~
printf '\n%s\n%s\n%s' '# virtualenv' 'export WORKON_HOME=~/virtualenvs' \
'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
source ~/.bashrc
mkdir -p $WORKON_HOME
~~~

Now we can set up our virtualenv:

~~~
mkvirtualenv venv --always-copy
workon venv
~~~

The *always-copy* flag solves [an issue with vagrant](https://stackoverflow.com/questions/24640819/protocol-error-setting-up-virtualenvironment-through-vagrant-on-ubuntu).

## 4. Final Steps

You’re pretty much good to go at this point. I went ahead and cloned my project into the home directory (which should be whatever folder you set up the Vagrant environment in). I then ran a *pip install -r requirements.txt* command from within the virtual environment.

I had to install a few dependencies before I could get a successful pip install, namely because of my postgres connection library. These package got everything working:

~~~
sudo apt-get install libpq-dev libncurses5-dev
~~~

My particular build also called for a redis server, which I was able to set up in one line:

~~~
sudo apt-get install redis-server
~~~

To keep things as simple as possible, I keep all my development environment variables in my *~/.bashrc* file. This has obvious limitations, but because I am devoting this entire Vagrant environment to one project it shouldn’t cause any issues for me. Here’s what the tail end of my *.bashrc* file looks like:

~~~
workon venv
export DATABASE_URL=postgres://app_local:app_local@localhost/db_local
export REDIS_URL=redis://127.0.0.1:6379/0
export DEBUG=True
~~~

I tend to use [Heroku Local](https://devcenter.heroku.com/articles/heroku-local) or Foreman to handle environment variables when I’m doing anything more complicated.

If you’re dealing with any `npm` packages, you may need to run some extra steps. The version of node that comes with Ubuntu 12.04 is very outdated, so the first step is updating to a stable new version of node.

~~~
sudo apt-get purge nodejs npm
curl -sL https://deb.nodesource.com/setup_4.x | sudo bash -
~~~

If you’re installing node modules into a shared vagrant folder, you will likely run into the [same issue](https://github.com/npm/npm/issues/7308) as seen with the virtualenv install. To solve this, make sure to use the `--no-bin-link` argument

~~~
npm install — no-bin-link
~~~

### Conclusion

That was pretty easy! As you can see, it should take less than an hour to get a complete end-to-end environment set up.

I’d like to thank [Exponential.io](http://exponential.io/blog/2015/02/10/install-virtualenv-and-virtualenvwrapper-on-ubuntu/) and [Postgres](https://wiki.postgresql.org/wiki/PostgreSQL_For_Development_With_Vagrant) for their helpful guides.
