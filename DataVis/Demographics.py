# imports
import matplotlib.pyplot as plt
import numpy as np

# data for graph
data = {
    "Under 18": 488,
    "18-19": 657,
    "20-21": 412,
    "22-24": 382,
    "25-29": 544,
    "30-34": 558,
    "35-39": 459,
    "40-49": 1058,
    "50-64": 1596,
    "65 & over": 380,
}

# divide data into axes lists
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)

# set layout and style
plt.rcParams.update({"figure.autolayout": True})
plt.style.use("ggplot")

# set up base plot and axes, along with data
fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()

# adjust limits, data labels, and title
ax.set(
    xlim=[0, 1700],
    xlabel="Students",
    ylabel="Age Bracket",
    title="BRCTC Students by Age Bracket",
)

# actually show the thing
plt.show()
