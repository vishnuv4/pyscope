import matplotlib.pyplot as plt
import argparse
import collections
import yaml

parser = argparse.ArgumentParser(description='Signals')
parser.add_argument('file', type=str, help="Name of the signal file")

args = parser.parse_args()
filename = args.file

try:
    with open(filename, "r", encoding="utf-8") as file:
        signals = yaml.safe_load(file)
except FileNotFoundError as exc:
    raise RuntimeError(f"No file called {filename}.yml") from exc

if len(signals) > 4:
    raise RuntimeError("Can't support more than 4 channels")

channel_list = ["ch0", "ch1", "ch2", "ch3"]
if not all(key in channel_list for key in signals.keys()):
    raise RuntimeError("Invalid channel name")

signals = collections.OrderedDict(sorted(signals.items()))

i = 0
for ch in signals:
    signals[ch] = [int(bit) for bit in "".join(signals[ch].split())]
    signals[ch] = [((-2 * i) + k) for k in signals[ch]]
    i += 1

lengths = [len(lst) for lst in signals.values()]
if not all(length is lengths[0] for length in lengths):
    raise ValueError("Signal lengths are not the same")

t = range(lengths[0])

# Each array element corresponds to the value immediately after the grid line

colors = ['xkcd:yellow', 'xkcd:cyan', 'xkcd:neon purple', 'xkcd:bright blue']
plt.figure(figsize=(16.18, 10))
i = 0
for ch in signals:
    plt.step(t, signals[ch], where='pre', color=colors[i])
    i = i + 1

plt.gca().set_facecolor('black')
plt.xlabel('')
plt.ylabel('')
plt.ylim(( -2 * len(signals) + 1), 2)

plt.xticks(ticks=t, labels='')
plt.yticks(ticks=[(-2 * i) for i in range(len(lengths))], labels=[channel for channel in signals.keys()])

plt.grid(True)

plt.show()
