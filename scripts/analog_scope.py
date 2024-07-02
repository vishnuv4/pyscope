import matplotlib.pyplot as plt
import numpy as np
import collections
import scripts.error as error


######################################################################
def generate_signal():
    """
    Modify the analog signal here and return it as a dict
    The keys of the dict must be ch0, ch1, ch2, or ch3
    """

    arr1 = np.sin(np.linspace(0, 8 * np.pi, 200))
    arr2 = 2 * np.sin(np.linspace(0, 8 * np.pi, 200))

    signals = {}
    signals["ch0"] = np.cos(np.linspace(0, 50 * np.pi, 400))
    signals["ch1"] = np.linspace(0,10,400) % 2
    signals["ch2"] = np.concatenate([arr1, arr2])
    return signals

######################################################################

if __name__ == "__main__":

    output_signal = generate_signal()

    if len(output_signal) > 4:
        error.fatal("Can't support more than 4 channels")

    channel_list = ["ch0", "ch1", "ch2", "ch3"]
    if not all(key in channel_list for key in output_signal.keys()):
        error.fatal("Invalid channel name")

    lengths = [len(lst) for lst in output_signal.values()]
    i = 0
    if not all(length == lengths[0] for length in lengths):
        for val in output_signal.values():
            print(f"{i}: {lengths[i]}")
            i += 1

        error.fatal("Signal lengths are not the same")

    output_signal = collections.OrderedDict(sorted(output_signal.items()))

    displacement = 2
    keys = list(output_signal.keys())
    for i in range(len(keys)-1):
        displacement = abs(min(output_signal[keys[i]])) + abs(max(output_signal[keys[i+1]])) + 2

    t = range(lengths[0])
    i=0
    for ch in output_signal:
        output_signal[ch] = [((-displacement * i) + k) for k in output_signal[ch]]
        i += 1

    # Each array element corresponds to the value immediately after the grid line

    colors = ['xkcd:yellow', 'xkcd:cyan', 'xkcd:neon purple', 'xkcd:bright blue']
    plt.figure(figsize=(16.18, 10))
    i = k = 0
    for ch in output_signal:
        plt.plot(t, output_signal[ch], color=colors[k])
        i = i + 1
        k = i % 4

    plt.gca().set_facecolor('black')
    plt.xlabel('')
    plt.ylabel('')
    plt.ylim(min(output_signal[list(output_signal.keys())[-1]]) - 2, max(output_signal[list(output_signal.keys())[0]]) + 2)

    plt.xticks(ticks=np.linspace(0, lengths[0], 50), labels='')
    plt.yticks(ticks=[(-displacement * i) for i in range(len(lengths))], labels=[channel for channel in output_signal.keys()])

    plt.grid(True)

    plt.show()
