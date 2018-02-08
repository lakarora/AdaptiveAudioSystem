# AdaptiveAudioSystem
The program uses real time microphone monitoring to analyze the current levels of noise in the immediate surroundings. Based on the audio levels, it calculates the optimal volume for output and gradually adjusts the current level to the optimal level automatically.
Currently, this works only for MacOS as the SoundMeter API used in the code is a command line tool itself. To test the code, you need to have python installed on your system. 
Once you have python installed, run the file from the terminal and the program will start adjusting the speaker/headphone volume corresponding to the surrounding noise levels.
