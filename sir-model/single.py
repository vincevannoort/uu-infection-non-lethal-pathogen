from model import SIRModel
import matplotlib.pyplot as plt
from matplotlib import colors
import itertools
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

color_dict = {
    'Susceptible': '#eeeeee',
    'Infected': '#ff5e5e',
    'Recovered': '#d6ff37'
}

# Configuration
duration = 1000
visualise_each_x_timesteps = 25
grid_size = 150

model = SIRModel(
    width=grid_size,
    height=grid_size,
    infectivity=4.2,
    infection_duration=70,
    immunity_duration=100,
    mutation_probability=0,
    mutation_strength=1,
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


multipage = PdfPages(
    f'figures/grid-{grid_size}-{duration}-{visualise_each_x_timesteps}.pdf')
cmap = colors.ListedColormap(['#eeeeee', '#ff5e5e', '#d6ff37'])
for index, grid in enumerate(model.grids_saved):
    grid = np.reshape(grid, (-1, grid_size))
    print(grid)
    # plt.figure()
    # plt.imshow(grid, cmap=cmap, interpolation='none')
    # plt.title(
    #     f'inf dur: {model.infection_duration}, imm dur: {model.immunity_duration}, step: {index*visualise_each_x_timesteps}.')
    # multipage.savefig()
    # plt.close()
multipage.close()
