from model import SIRModel
import matplotlib.pyplot as plt
from matplotlib import colors
import time
import itertools
import math
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

cmap = colors.ListedColormap(['#eeeeee', '#ff5e5e', '#d6ff37'])
color_dict = { 'Susceptible': '#eeeeee', 'Infected': '#ff5e5e', 'Recovered': '#d6ff37' }

# Configuration
duration = 125 * 3000
visualise_each_x_timesteps = 125
grid_size = 120

model = SIRModel(
    width=grid_size,
    height=grid_size,
    infectivity=1,
    infection_duration=70,
    immunity_duration=130,
    mutation_probability=0.1,
    mutation_strength=0.1,
    visualise_each_x_timesteps=visualise_each_x_timesteps)

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

multipage = PdfPages(f'figures/grid-{grid_size}-{duration}-{visualise_each_x_timesteps}-{time.strftime("%Y%m%d-%H%M%S")}.pdf')

# print(math.ceil((duration / visualise_each_x_timesteps) / 25))
# print(np.array_split(np.arange(35.0), 2))

for index_grids, grids in enumerate(np.array_split(model.grids_saved, math.ceil((duration / visualise_each_x_timesteps) / 25))):
    fig, axes = plt.subplots(nrows=5, ncols=5, figsize=(15, 15))
    plt.subplots_adjust(wspace=0.3, hspace=0.3)

    fig.suptitle(f'Infectivity: {model.infectivity} \nInfection duration: {model.infection_duration} \nImmunity duration: {model.immunity_duration}', fontsize=24)
    for index_axes, ax in enumerate(axes.reshape(-1)):
        try:
            grid = grids[index_axes]
            grid = np.reshape(grid, (-1, grid_size))
            ax.set_title(f'iteration: {index_grids * 25 * visualise_each_x_timesteps + index_axes * 25}')
            ax.imshow(grid, cmap=cmap, interpolation='none')
        except IndexError:
            break

    multipage.savefig()

multipage.close()

