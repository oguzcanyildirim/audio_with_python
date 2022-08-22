# audio_with_python

## Project Definition
The project is thought to create a library which is able to:
   - retrieve audio from the defined default audio input port and save it into a *.wav* file
   - Able to play *.wav* files
   - Push the *.wav* file to telegram messenger and whatsapp.

The last point is *to be implemented*.

The other points are already developed in **managesound.py**. 

## Requirements
Python 3 is needed. The project is built with Python 3.7. 
Additionally wave and pyaudio libraries need to be installed through
```
pip install Wave
pip install PyAudio
```

## Code Usage
To use the code, **audioGet.py** is used which is an example main file.

When the functions are run, be sure to have write permissions to the current folder since it will save your microphone input receive files into **output.wav** in the same directory.
