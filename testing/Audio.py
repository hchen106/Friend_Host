import pyaudio
import time

#variables
chunk = 4096
audio_format = pyaudio.paInt16
channels = 2
rate_of_transfer = 43000

#find stereo Mix automaticlly
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    if (dev['name'] == 'Stereo Mix (Realtek Audio)' and dev['hostApi'] == 0):
        dev_index = dev['index']
        print(dev_index)
    else:
        print("not found")

# will need to do mutithreaded for this to work properly
# testing done in check.py instead
while 1 :
    record_output = p.open(format = audio_format, 
                    channels = channels, 
                    rate = rate_of_transfer,
                    input = True,
                    frames_per_buffer = chunk,
                    input_device_index = dev_index)
    record_microphone = p.open(format = audio_format, 
                    channels = 1, 
                    rate = rate_of_transfer,
                    input = True,
                    frames_per_buffer = chunk)
    #i = i + 1
    
    playing = p.open(format = audio_format, 
                    channels = channels, 
                    rate = rate_of_transfer,
                    output = True,
                    frames_per_buffer = chunk)
    playing2 = p.open(format = audio_format, 
                    channels = 1, 
                    rate = rate_of_transfer,
                    output = True,
                    frames_per_buffer = chunk)

    #print("microphone working")

    data_output = record_output.read(4096)
    # print("finish output")
    data_microphone = record_microphone.read(4096)
    # print("finish microphone")
    time.sleep(0.1)

    playing.write(data_output)
    playing2.write(data_microphone)
    


