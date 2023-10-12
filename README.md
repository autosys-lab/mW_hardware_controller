# MicroWunderland Hardware Controller
This simple python program can be used to control the switches in the MicroWunderland.

## Installation
Clone this repo and install all dependencies with (inside the repo):
```
pipenv install
```
TODO: Instructions to automnatically install into systemd

## Usage
Preferred way is to run on boot via systemd. But to test, you can run the `main.py` manually (UDP backend).

### Environment Variables
Example to manually run with ROS backend:
```
ROS=1 ./main.py
```

| Var   | Desc                                                 | Default   |
|-------|------------------------------------------------------|-----------|
| ROS   | Use ROS2 backend                                     | 0         |
| UDP   | Use UDP backend (will be used if no backend defined) | 0         |
| PORT  | for UDP: Port to listen to                           | 5005      |
| TOPIC | for ROS: Ros topic for the switches (Str msg type)   | /switches |

### Config
Change the config.yaml to change Servo parameters.

TODO: Servo layout and script to test duty cycles

