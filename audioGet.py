from managesound import SoundManager

sound_manager = SoundManager()

sound_manager.list_devices()

#sound_manager.retrieve_sound()

sound_manager.sound_play("output.wav")
