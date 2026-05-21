# Python Live Url Tracker

This project was created with gemini AI. This project was made to test live url tracking to use for tracking projects where url needs to be collected automatically.
![hippo](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXMyOWliZWVtMGoyenpidGw4eWlsbHVwbWltZWpjN20yZzd5aWlzYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hmVy6WTCyGofvfe8Xa/giphy.gif)


# Dependencies
This program uses javascript, html, and python.  
Additional python dependencies are:  
- flask
- flask-cors

# System Requirements
This program is currently first tested on Debian OS and on a Chromium browser.  
Testing for other systems will be done in the future.


# How to Install the Program
Clone the repository into a directory of choice
```
git clone https://github.com/5000adel/python-live-url-tracker.git
cd python-live-url-tracker
```
  
Before running the program, a browser extension is required, which is included in the repository inside the "**extension**" folder.

### Importing the Extension
-  Navigate to your browser extension settings
- Turn on developer mode
- Click "Load unpacked" to import extension
- Navigate to where you installed the project repository
- Select the "**extension**" folder, then import.

Now that you have imported the extension, you should enable it and it should run in the background.

### Running the Program Itself
On the previous instructions where we cloned the repository.
```
git clone https://github.com/5000adel/python-live-url-tracker.git
cd python-live-url-tracker
```
Here are the steps that preceed it after setting up the extension.
```
python server.py
```
Make sure that the python dependencies are installed.  
If you haven't installed them yet:
```
python3 -m pip install flask flask-cors
```
