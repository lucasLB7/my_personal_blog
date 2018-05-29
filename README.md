# BLENDER FENDER
- Made by : Lucas Lambert
- plucaslambert@gmail.com

Get started with Blender CGI.
A community based blog that focuses on tutorials for blender
Final vesrion will have a User rating system to allow users with good content to be "rewarded for their participation"

## FUNCTIONALITY

A user can visit the app and view tutorials as well as comment on them **without having to sign up or register**.
Only a registered user can create new tutorials.

First time visit (**not registered**):

![alt text](/app/static/images/scrn-shot1.png)

A user can view comments directly on screen, no need to sign in.

**click on view tutorial to go to the tutorial page**

![alt text](/app/static/images/ss2.png)

**To create tutorials:**
You first need to REGISTER:
![alt text](/app/static/images/register.png)

Then you need to log in

![alt text](/app/static/images/login.png)

Now you have access to the create new tutorials portal

![alt text](/app/static/images/adminportal.png)
![alt text](/app/static/images/createPost.png)


The app is **under development** and in pre Alpha stages. Thank you for your **understanding** and sorry for the bugs. 


## Getting Started

Installing dependancies & requirements to run this app:

To install dependancies, simply run:

```pip3 install requirements.txt```

**This will run pip to install the flask/requirements**


### Prerequisites

- Python 3.6.2
- Python flask
- Linux based OS
- PIP installer
- Git hub

### Installing

Clone from git hub repository:
In dev phases USE this branch TRY.


First, install python pip:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

-clone the following repository: **https://github.com/lucasLB7/my_personal_blog/tree/backup**

Once cloned I would advice setting up a virtual environment using **virtualenv**.
Then run the virtual environment using:

```
source venv/bin/activate
```
After activating the virtual env, you need to make sure all dependancies are installed:

run in command prompt:

```
pip3 install requirements.txt
```

Install the above mentioned Prerequisites following the pip install model.

Finally, run the app localy by using the command:
```
python3 manage.py server
```
__this will launch a local server__ you can visit the app on: __localhost:5000__


## Running the tests
```python 
python  manage.py test`
```

## Live Demo
click on this link [blenderfenderapp](https://blenderfenderapp.herokuapp.com)

## Built With

* [python](https://www.python.org/) - Logic language
* [flask](http://flask.pocoo.org/) - Framework for python
* [SQLAlchemy](https://www.sqlalchemy.org/) - Used to generate database

## Contributing

If you notice any bugs or errors in the app, please contact me on:
- plucaslambert@gmail.com


## Versioning

I used [Github](http://github.com/) for versioning.  

## Authors

* **Lucas Lambert** - *Initial work* - [pitchit](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Moringa instructure
* Flask documentation
* Google

