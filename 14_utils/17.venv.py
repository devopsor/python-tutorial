# When developing Python applications, there is only one version of Python3 installed on the system: 3.10. 
# All third-party packages will be pipinstalled into the Python3 site-packages directory.

# If we want to develop multiple applications at the same time, then these applications will share a Python, which is Python 3 
# installed on the system. What if app A needs jinja 2.7 and app B needs jinja 2.6?

# In this case, each application may need to have its own "independent" Python runtime environment. 
# A venv is used to create an "isolated" Python runtime environment for an application.