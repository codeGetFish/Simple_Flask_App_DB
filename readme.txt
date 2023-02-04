After downloading the zip file
Extract all
Open the file in Visual Studio Code
Start a virtual environment 
If you don't have a virtual environment, you can create one by following these steps:
Open the integrated terminal in Visual Studio Code by clicking on View > Terminal or using the keyboard shortcut Ctrl + `` `.
Create a virtual environment by running the following command in the terminal:
python -m venv path/to/venv or windows VSC python -m venv .venv and click ok to the prompt
Replace path/to/venv with the desired path for your virtual environment.
Activate the virtual environment by running the following command:
source path/to/venv/bin/activate
Install the required packages, if you haven't already. To do so, run the following command:
pip install -r requirements.txt
Finally, run the Flask app by executing the following command:
python run.py