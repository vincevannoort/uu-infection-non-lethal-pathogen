from model import SIRModel
import matplotlib.pyplot as plt
import itertools
import numpy as np

color_dict = {
    'Susceptible': '#eeeeee', 
    'Infected': '#ff5e5e',
    'Recovered': '#d6ff37'
}

color_dict_states = {
    '1': '#eeeeee',
    '2': '#ff5e5e',
    '3': '#d6ff37'
}

# Configuration
duration = 120
visualise_each_x_timesteps = -1
grid_size = 150

model = SIRModel(grid_size, grid_size, infectivity=4.2, infection_duration=70, immunity_duration=100,
                 mutation_probability=0.01, mutation_strength=1, visualise_each_x_timesteps=visualise_each_x_timesteps)

for i in range(duration):
    model.step()

data = model.datacollector_cells.get_model_vars_dataframe()
data_mid = model.datacollector_meaninfectionduration.get_model_vars_dataframe()

color = [color_dict.get(x, '#333333') for x in data.columns]
title = f'Infection duration: {model.infection_duration}, Immunity duration: {model.immunity_duration}'

# plot amount of susceptible, recoveries and infected
data.plot.area(color=color, title=title).legend(loc='upper right')
plt.margins(0)
plt.savefig(f'figures/model-result--single--inf-{model.infection_duration}--imm-{model.immunity_duration}.pdf')

# plot infection duration
data_mid.plot()
plt.savefig(f'figures/inf-dur-result.pdf')

for index, grid in enumerate(model.grids_saved):
    grid = np.reshape(grid, (-1, grid_size))
    plt.figure()
    plt.imshow(grid)
    plt.savefig(f'figures/grids/grid--{index}.pdf')
    plt.close()
