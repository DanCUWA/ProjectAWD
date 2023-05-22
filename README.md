# GameMaster

A text-based chat application for the CITS3403 project
Welcome to GameMaster, you will be playing a text-based adventure, where you can build your character and explore a endless worlds.

## Getting Started

To follow this guide, we will assume that you will be using wsl or a linux based terminal

### Prerequisites

Before starting, ensure that `python3` and `pip` are installed on your system before commencing.

To check, run the following commands separately in your terminal

```
python3 --version
pip --version
```

If you do not have `python3` or `pip` installed, you can install them by running the following commands separately:

```
sudo apt update && upgrade
sudo apt install python3 python3-pip
```

This will update your package manager, and you can use `python3` and `pip` to create and manage a virtual environments and install packages and dependencies.

### Making the virtual environment

After ensuring that you have python3 and pip installed. You'll need to create a virtual environment.

Run the following command:

```
python3 -m venv venv
```

After it has finished installing, run:

```
source venv/bin/activate
```

to activate the virtual environment
(afterwards, `(venv)` should appear at the front of the command line)

### Installing the requirements

Once you have created and activated the virtual environment. You will need to install the requirements needed

Run this command:

```
pip install -r requirements.txt
```

## Starting the game

### Testing

Testing for the application is done primarily by pytest.
In order to run the tests, simply navigate to the root directory in your venv and run the following:

```
pytest
```

Or to see full coverage, run

```
pytest --cov=app tests/
```

### Creating the database

Required to initialize the database

Run these commands line by line:

```
flask db migrate
flask db upgrade
```

To see the database schema, view models.py in the app directory.

### Running The Website

In order to run the web server locally, all the steps above should be followed, and make sure you are in the virtual environment before running the following line.
to start the website, run this:

```
flask run
```

This should start the server on `http://localhost:5000`. Which can be accessed in the browser

## Gameplay

### Instructions

When in the game rooms, you can create a room with a maximum of 4 people, and you can choose either a default scenario or make your own scenario

Once the room is entered, there will be a start button on the top of the screen, the game won't start until it pressed. So any messages inputted will be ignored.

### Example of Gameplay

If you were to input "My character is name Mick, and i am a knight". The game will respond with attributes associated with knight.

The game response will vary depending on the user's input, the more vague you are, the more information the game has to make up.

## Authors

Daniel Cheng - 23126543 - [DanCUWA](https://github.com/DanCUWA)

Tony Nguyen - 23090585 - [Tony-Nguyen0](https://github.com/Tony-Nguyen0)

Peter Le - 23193249 - [petaa1](https://github.com/petaa1)

Adi Budhavaram - 23086947 - [adibud](https://github.com/adibud)

## Acknowledgments

ChatGPT

This project utilizes ChatGPT, an AI model developed by OpenAI

Model: ChatGPT

Model version: GPT-3.5-turbo

Model Source : OpenAI API (https://openai.com)

Model reference: https://openai.com/blog/chatgpt/

Model license: OpenAI API Terms of Service

## External Images

- https://icon-library.com/images/multiple-people-icon/multiple-people-icon-17.jpg
- https://cdn.icon-icons.com/icons2/390/PNG/512/hood_39094.png
- https://cdn-icons-png.flaticon.com/512/114/114433.png
- https://1.bp.blogspot.com/-3dJaGBCMKbA/VqcFiK9zO1I/AAAAAAAAW9Y/xCakJ-OxsS8/s640/quantum_stars.gif
- https://mir-s3-cdn-cf.behance.net/project_modules/fs/dc82fb44263453.580dd1bf77b62.jpg
- https://i.ytimg.com/vi/DyBDy8urs1Q/maxresdefault.jpg
- https://d3d00swyhr67nd.cloudfront.net/w800h800/collection/CDN/WELL/CDN_WELL_L_30887-001.jpg

(All other images are created locally by Tony Nguyen)

## Contributions

### Daniel Cheng

- Flask set up and structure initialisation
- Basic GPT request-response architecture
- Database set up
  > Model and schema initialisation
- Created routes
- Created route handlers
- Socketio
  > Multi-client communication
  > Implementation of different rooms
- Profile Page
  > Initial design
  > Functionality
- Pytest
- Css styling
- Refactoring from basic setup to MVC
- Refactoring from single MVC to blueprint MVC
- Form creation
- Login/signup set up
- Password Hashing

### Tony Nguyen

- Initial Web Game Concept
- front end template set up
- base html
- Game rooms
- Css styling
- Intro page
- Graphics/images
- Prompts for GPT
- Welcome Page
- chatroom page
- Setting page
- Database set up
- Routing
- Animation
- Form creation

### Peter Le

- Login set up
- Login Page
- Database set up
- Routing
- GPT implementation
- Setting Page
- Css Styling
- Pytest
- Custom settings
- Account settings

### Adi Budhavaram
