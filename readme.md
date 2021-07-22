#CDSE - Client
A package to make a implementation to CDSE - core.
This package allows you to focus on the prediction model implementation.
The rest will be handled by the client.

#Getting started
Don't clone this repo directly! Instead, start you own project and use git submodule to include this package.

In your repo run: 
- git submodule add https://<you-username-here>@bitbucket.org/maastro/cdse-client.git client

This will create a new folder called "client" in you project.
Copy the client/example.Dockerfile and client/pipfile to your root and remove the "example" prefix.
Also create a new file (for example called main.py) in the root of your project and connect your prediction model like 
demonstrated in client/example.py.

To install packages needed for the client, run the command:
- Pipenv install

Now check the dockerfile CMD command, it needs to point to your created file in root.
After that you can build the image and upload it to a public docker registry.
