from model import SIRModel
import matplotlib.pyplot as plt
from matplotlib import colors
import itertools
import numpy as np

color_dict = {
    'Susceptible': '#eeeeee',
    'Infected': '#ff5e5e',
    'Recovered': '#d6ff37'
}

# Configuration
duration = 2000
visualise_each_x_timesteps = 100
grid_size = 200

model = SIRModel(grid_size, grid_size, infectivity=4.2, infection_duration=70, immunity_duration=70,
                 mutation_probability=0.1, mutation_strength=5, visualise_each_x_timesteps=visualise_each_x_timesteps)

for i in range(duration):
    model.step()

data = model.datacollector_cells.get_model_vars_dataframe()
data_mid = model.datacollector_meaninfectionduration.get_model_vars_dataframe()

color = [color_dict.get(x, '#333333') for x in data.columns]
title = f'Infection duration: {model.infection_duration}, Immunity duration: {model.immunity_duration}'

# plot amount of susceptible, recoveries and infected
data.plot.area(color=color, title=title).legend(loc='upper right')
plt.margins(0)
plt.savefig(
    f'figures/model-result--single--inf-{model.infection_duration}--imm-{model.immunity_duration}.pdf')

# plot infection duration
data_mid.plot()
plt.savefig(f'figures/inf-dur-result.pdf')


cmap = colors.ListedColormap(['#eeeeee', '#ff5e5e', '#d6ff37'])
for index, grid in enumerate(model.grids_saved):
    grid = np.reshape(grid, (-1, grid_size))
    plt.figure()
    plt.imshow(grid, cmap=cmap)
    plt.savefig(f'figures/grids/grid--{index}.pdf')
    plt.close()
