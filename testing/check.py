import pyaudio 
import time

chunk = 4096
audio_format = pyaudio.paInt16
channels = 2
rate_of_transfer = 10000
data = []

p = pyaudio.PyAudio()

for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    if (dev['name'] == 'Stereo Mix (Realtek Audio)' and dev['hostApi'] == 0):
        dev_index = dev['index']
        print(dev_index)
    else:
        print("not found")

# this records the voices and sounds then play it back after time is up.
# can heard that it is fragmented, need to do mutltithread to hear it properly.
for i in range(30):
    stream = p.open(format=audio_format, channels=channels, rate=rate_of_transfer, input=True, output=True, frames_per_buffer=chunk, input_device_index=dev_index)
    stream2 = p.open(format=audio_format, channels=channels, rate=rate_of_transfer, input=True, output=True, frames_per_buffer=chunk)
    data.append(stream.read(4096))
    data.append(stream2.read(4096))
    print(i)
print("done recording")

time.sleep(0.1)

for x in range(len(data)):
    stream.write(data[x])

# p = pyaudio.PyAudio()
# host_info = p.get_host_api_info_by_index(0)    
# device_count = host_info.get('deviceCount')
# devices1 = []

# # iterate between devices:
# for s in range(0, device_count):
#     device1 = p.get_device_info_by_index(s)
#     devices1.append(device1)

# for x in range(len(devices1)):
#     print(devices1[x])