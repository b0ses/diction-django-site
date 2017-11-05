# Developer Setup

Really I don't expect other developers for this project but I like to have this process saved for future projects.

## Text Editors
Text editors I use, you can use whatever:

* Python Backend: [PyCharm](https://www.jetbrains.com/pycharm/)

Good, you can change text documents. Whoopie do. 

## Git

You can use whatever git interface of your choosing. I like:
 
* command-line for more functionality
* [GitHub Desktop](https://desktop.github.com/) for usual committing

Clone the latest `dev` branch.

## Python and VirtualEnv

Let's get Django setup. To do that, you need Python3. If you don't have Python3 and you're working off an OS that doesn't automatically provide it, [get it]((https://www.python.org/)). Make sure `pip3` is included.

Got Python? Cool, let's move on. Let's get a virtualenv setup.

    > pip3 install virtualenv virtualenvwrapper
    > cd /wherever/you/cloned/the/dev/branch/personal-website-django/

Let's save some hassle in the future. First, let's figure out where that `virtualenvwrapper` got installled.

    > which virtualenvwrapper.sh
    > which python3

Then get and setup [direnv](https://direnv.net/). Make a `.envrc` file in this directory and add the following lines to it.

    export WORKON_HOME=~/.virtualenvs
    export VIRTUALENVWRAPPER_PYTHON=/python3/location
    source /virtualenvwrapper.sh/location/

Then source it and make your virtual environment:

    > source .envrc
    > mkvirtualenv --python=/usr/local/bin/python3 personal-website-django

Running `python` in this environment should point to python3, here are the commands you need in the future.

    > cd /wherever/you/cloned/the/dev/branch/personal-website-django/
    > workon personal-website-django
    Do whatever, then to get out of it
    > deactivate

While we're at it, let's add this directory to the `PYTHONPATH`:

    > add2virtualenv /wherever/you/cloned/the/dev/branch/personal-website-django

## Django

Cool, let's actually get into the project. Install the requirements:

    > pip3 install -r requirements.txt

And give it a whirl,

    > python manage.py runserver

And checkout `http://localhost:8000`. Congrats, we have a Django Hello World.

To be continued...
