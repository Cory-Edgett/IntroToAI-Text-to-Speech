# IntroToAI-Text-to-Speech
Developer: Jonathan, Stefan, Luis, Cortlan

How to run the code:

Packages needed
	- Tensorflow  1.2.1+
	- Pickle      12.1+
	- pydub       0.12.0+
	- numpy       1.13.1+
	
	Pydub
		- Can be installed from http://pydub.com/ or using "pip install pydub"  
		  or (https://github.com/jiaaro/pydub#installation) for other options
	
Make sure your anaconda environment contains those packages.
There shouldn't be a need to relaunch the tensorflow code in TFLanguageTranslation.py
The model has already been proccessed by us and saved using Pickle. 

Download repository https://github.com/Cory-Edgett/IntroToAI-Text-to-Speech.git

Open TF_code...

execute main.py        (Theres no need for arguments)

After execution, you will be prompt to type any sentence you will like to say. 
Type and press enter.

If you want to exit. Type "exit"
or use Ctrl-C



What does not work?

	- We don't check for non-alphabetic character. Don't try it program will crash!
	- On program execution we get a runtime warning for saving/opening binary music files. (Not needed)
	  Don't worry the program runs even better with the warning. :)
	- Were not able to implement sarcasm into the text-to-speech



	
	
	