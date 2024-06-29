import json
import matplotlib.pyplot as plt
import argparse
import collections

parser = argparse.ArgumentParser(description='Signals')
parser.add_argument('file', type=str, help="Name of the signal file")

args = parser.parse_args()
filename = args.file

try:
    with open(filename, "r", encoding="utf-8") as file:
        signals = json.load(file)
except FileNotFoundError:
    raise RuntimeError("Make sure your probes are connected. No signal found.")

if len(signals) > 4:
    raise RuntimeError("Buy a better oscilloscope with more than 4 channels.")

channel_list = ["ch0", "ch1", "ch2", "ch3"]
if not all(key in channel_list for key in signals.keys()):
    raise RuntimeError("I don't know what that is but it isn't a channel.")

signals = collections.OrderedDict(sorted(signals.items()))

i = 0
for ch in signals:
    signals[ch] = [int(bit) for bit in "".join(signals[ch].split())]
    signals[ch] = [((2 * i) + k) for k in signals[ch]]
    i += 1

lengths = [len(lst) for lst in signals.values()]
if not all(length is lengths[0] for length in lengths):
    raise ValueError("Signal lengths are not the same")

t = range(lengths[0])

# Each array element corresponds to the value immediately after the grid line

colors = ['yellow', 'cyan', 'purple', 'blue']
plt.figure(figsize=(15, 6))
i = k = 0
for ch in signals:
    plt.step(t, signals[ch], where='pre', color=colors[k])
    i = i + 1
    k = i % 4

plt.gca().set_facecolor('black')
plt.xlabel('')
plt.ylabel('')
plt.ylim(-0.5, (2 * i) + 0.5)

plt.xticks(ticks=t, labels='')
plt.yticks(ticks=[0,2], labels='')

plt.grid(True)

plt.show()
