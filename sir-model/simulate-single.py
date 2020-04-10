from model import SIRModel
import matplotlib.pyplot as plt
from matplotlib import colors
import time
import itertools
import math
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

cmap = colors.ListedColormap(['#eeeeee', '#ff5e5e', '#d6ff37'])
color_dict = {'Susceptible': '#eeeeee',
              'Infected': '#ff5e5e', 'Recovered': '#d6ff37'}

# Configuration
duration = 100 * 50
visualise_each_x_timesteps = 100
grid_size = 120

model = SIRModel(
    width=grid_size,
    height=grid_size,
    infectivity=1,
    infection_duration=130,
    immunity_duration=70,
    mutation_probability=0.1,
    mutation_strength=1,
    visualise_each_x_timesteps=visualise_each_x_timesteps)

start_time = time.strftime("%Y%m%d-%H%M%S")

for i in range(duration):
    model.step()
    if i % 100 == 0:
        print(i)

data = model.datacollector_cells.get_model_vars_dataframe()
data_mid = model.datacollector_meaninfectionduration.get_model_vars_dataframe()

color = [color_dict.get(x, '#333333') for x in data.columns]
title = f'Infection duration: {model.infection_duration}, Immunity duration: {model.immunity_duration}'

# plot: amount of susceptible, recoveries and infected
data.plot.area(color=color, title=title).legend(loc='upper right')
plt.margins(0)
plt.savefig(f'figures/{start_time}-graph.pdf')

# plot: infection duration
data_mid.plot()
plt.savefig(f'figures/{start_time}-infection.pdf')

# plot: grid
multipage = PdfPages(f'figures/{start_time}-grids.pdf')

for index_grids, grids in enumerate(np.array_split(model.grids_saved, math.ceil((duration / visualise_each_x_timesteps) / 25))):
    fig, axes = plt.subplots(nrows=5, ncols=5, figsize=(15, 15))
    plt.subplots_adjust(wspace=0.3, hspace=0.3)

    fig.suptitle(
        f'Infectivity: {model.infectivity} \nInfection duration: {model.infection_duration} \nImmunity duration: {model.immunity_duration}', fontsize=24)
    for index_axes, ax in enumerate(axes.reshape(-1)):
        try:
            grid = grids[index_axes]
            grid = np.reshape(grid, (-1, grid_size))
            ax.set_title(f'iteration: {index_grids * visualise_each_x_timesteps * 25 + index_axes * visualise_each_x_timesteps}')
            ax.imshow(grid, cmap=cmap, interpolation='none')
        except IndexError:
            break

    multipage.savefig()

multipage.close()


# Save first 10 frames
for index, grid in enumerate(model.grids_saved[:10]):
    grid = np.reshape(grid, (-1, grid_size))
    plt.figure()
    plt.imshow(grid, cmap=cmap, interpolation='none')
    plt.title(f'Infectivity: {model.infectivity}, Infection duration: {model.infection_duration}, Immunity duration: {model.immunity_duration}\niteration: {index * visualise_each_x_timesteps}')
    plt.savefig(f'figures/{start_time}-spatial-start-{index}.pdf')
    plt.close()

# Save last 10 frames
for index, grid in enumerate(model.grids_saved[-10:]):
    grid = np.reshape(grid, (-1, grid_size))
    plt.figure()
    plt.imshow(grid, cmap=cmap, interpolation='none')
    plt.title(f'Infectivity: {model.infectivity}, Infection duration: {model.infection_duration}, Immunity duration: {model.immunity_duration}\niteration: {duration - 10 * visualise_each_x_timesteps + index * visualise_each_x_timesteps}')
    plt.savefig(f'figures/{start_time}-spatial-end-{index}.pdf')
    plt.close()
