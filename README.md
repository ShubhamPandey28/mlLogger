# mlLogger
A commandline attempt to organise my data science projects.

# Installation

Clone the repository

``` git clone https://github.com/ShubhamPandey28/mlLogger.git ```

Go to the cloned directory

```cd mlLogger```

Run

```sudo python3 setup.py install```

# Note 

At the first run it will ask your mysql details. Fill as per your likes.


# Usage

Creating a workspace

```mlLogger workspace create```


Deleting a workspace

```mlLogger workspace delete <worskspace name>```


Listing all the workspaces running on your machine

```mlLogger workspace show```


# Near future upgrades

This is it untill now. There's a lot plugins which planned tobe included in future.

Right now mlLogger only supports python virtualisation using ```virtualenv```. In future it is planned to virtualise using ```docker``` which will allow to containerise the data science working environment.


# Most urgent thing

The name(mlLogger) is a bit funcky right now. I wasn't able to come up with a good name. Please help me out.
