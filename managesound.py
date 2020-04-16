import pyaudio
import wave


class SoundManager:
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.RECORD_SECONDS = 10
        self.WAVE_OUTPUT_FILENAME = "output.wav"

    def list_devices(self):
        """List all available microphone devices."""

        for i in range(self.pa.get_device_count()):
            dev = self.pa.get_device_info_by_index(i)
            input_chn = dev.get('maxInputChannels', 0)

            if input_chn > 0:
                name = dev.get('name')
                rate = dev.get('defaultSampleRate')
                print("Index {i}: {name} (Max Channels {input_chn}, Default @ {rate} Hz)".format(
                    i=i, name=name, input_chn=input_chn, rate=int(rate)

                ))
        return 0

    # Plays the sound at the location of the given file name
    # Inputs:
    #   fileName: a sound file to be played
    def sound_play(self, filename):
        """
        Plays the sound at the location of the given file name
        Inputs:
        filename: a sound file to be played
        """
        # mp3 to wav - if input is in mp3 format instead
        # AudioSegment.from_mp3(sound).export(("{}.wav".format(fp.name)), format="wav")

        try:
            openfile = wave.open(filename, "rb")
        except:
            print("ReadFileError: Error occurred when reading the file " + filename)
        else:
            pa = pyaudio.PyAudio()
            stream = pa.open(format=pa.get_format_from_width(openfile.getsampwidth()),
                             channels=openfile.getnchannels(),
                             rate=openfile.getframerate(),
                             output=True)
            data = openfile.readframes(self.CHUNK)
            print("* playing")
            while len(data) > 0:
                # while data != "":
                stream.write(data)
                data = openfile.readframes(self.CHUNK)
            print("* done playing")
            stream.close()
            pa.terminate()

    def retrieve_sound(self):
        """With the default arranged mic this method saves the input in a wav file"""

        stream = self.pa.open(format=self.FORMAT,
                              channels=self.CHANNELS,
                              rate=self.RATE,
                              input=True,
                              frames_per_buffer=self.CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        self.pa.terminate()

        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.pa.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
