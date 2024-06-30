import matplotlib.pyplot as plt
import numpy as np
import collections

signals = {}

######################################################################
'''
Modify the signals here
'''

signals["ch0"] = np.sin(np.linspace(0, 2 * np.pi, 80))
signals["ch1"] = np.cos(np.linspace(0, 2 * np.pi, 80))
signals["ch2"] = np.sin(np.linspace(0, 2 * np.pi, 40))

######################################################################

if len(signals) > 4:
    raise RuntimeError("Can't support more than 4 channels")

channel_list = ["ch0", "ch1", "ch2", "ch3"]
if not all(key in channel_list for key in signals.keys()):
    raise RuntimeError("Invalid channel name")

lengths = [len(lst) for lst in signals.values()]
if not all(length is lengths[0] for length in lengths):
    raise ValueError("Signal lengths are not the same")

signals = collections.OrderedDict(sorted(signals.items()))

t = range(lengths[0])
i=0
for ch in signals:
    signals[ch] = [((-2 * i) + k) for k in signals[ch]]
    i += 1

# Each array element corresponds to the value immediately after the grid line

colors = ['xkcd:yellow', 'xkcd:cyan', 'xkcd:neon purple', 'xkcd:bright blue']
plt.figure(figsize=(15, 6))
i = k = 0
for ch in signals:
    print(ch)
    print(signals[ch])
    print('\n')
    plt.plot(t, signals[ch], color=colors[k])
    i = i + 1
    k = i % 4

plt.gca().set_facecolor('black')
plt.xlabel('')
plt.ylabel('')
print(list(signals.keys())[0])
print(list(signals.keys())[-1])
plt.ylim(min(signals[list(signals.keys())[-1]]) - 2, max(signals[list(signals.keys())[0]]) + 2)

plt.xticks(ticks=t, labels='')
plt.yticks(ticks=[(-2 * i) for i in range(len(lengths))], labels=[channel for channel in signals.keys()])

plt.grid(True)

plt.show()
