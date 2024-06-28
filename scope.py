import matplotlib.pyplot as plt

num_graphs = 4
signals = [[] for _ in range(num_graphs)]
pads = [[] for _ in range(num_graphs)]

# The spaces don't mean anything, just grouped for convenience
signals[0] = " 0101 1011 0000 0000 0110 1001 0000 0000 1010 1101 0000 0000 1010 1100 0000 0000"
signals[1] = " 0000 0000 0110 1101 0000 0000 0011 0100 0000 0000 0101 1100 0000 0000 0010 0001"
signals[2] = " 1010 1010 1010 1010 1010 1010 1010 1010 1010 1010 1010 1010 1010 1010 1010 1010"
signals[3] = " 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000"
pads[0] = 5 * [0]
pads[1] = 5 * [0]
pads[2] = 5 * [0]
pads[3] = 5 * [1]

for i in range(num_graphs):
    signals[i] = pads[i] + [int(bit) for bit in "".join(signals[i].split())] + pads[i]
    signals[i] = [((2 * i) + k) for k in signals[i]]

if not all(len(signal) is len(signals[0]) for signal in signals):
    raise ValueError("Signal lengths different")

t = range(len(signals[0]))

# Each array element corresponds to the value immediately after the grid line

colors = ['yellow', 'cyan', 'purple', 'blue']
plt.figure(figsize=(15, 6))
for i in range(num_graphs):
    plt.step(t, signals[i], where='pre', color=colors[i])

plt.gca().set_facecolor('black')
plt.xlabel('')
plt.ylabel('')
plt.ylim(-0.5, (2 * num_graphs) + 0.5)

plt.xticks(ticks=t, labels='')
plt.yticks(ticks=[0,2], labels='')

plt.grid(True)

plt.show()
