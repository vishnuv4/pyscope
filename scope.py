import json
import sys
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Signals')
parser.add_argument('file', type=str, help="Name of the signal file")

args = parser.parse_args()
filename = args.file

try:
    with open(filename, "r", encoding="utf-8") as file:
        signals = json.load(file)
except FileNotFoundError:
    raise RuntimeError("Signal not found!")

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
