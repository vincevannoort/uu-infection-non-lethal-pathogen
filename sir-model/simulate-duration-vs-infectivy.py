from model import SIRModel
import matplotlib.pyplot as plt
import itertools
import time
import numpy as np

color_dict = {
    'Infected': '#ff5e5e',
    'Susceptible': '#eeeeee',
    'Recovered': '#d6ff37'
}

duration = 5000
# duration = 5000
grid_size = 100

models = [
    SIRModel(grid_size, grid_size, infectivity=0.1, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.125, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.15, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.175, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.2, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.225, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.25, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.275, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.3, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.325, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.35, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.375, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.4, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.425, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.45, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.475, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.5, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.525, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.55, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.575, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.6, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.625, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.65, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.675, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.7, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.725, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.75, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.775, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.9, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.925, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.95, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=0.975, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.0, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.125, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.15, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.175, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.1, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.125, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.15, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.175, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.2, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.225, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.25, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.275, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.3, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.325, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.35, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.375, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.4, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.425, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.45, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.475, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
    SIRModel(grid_size, grid_size, infectivity=1.5, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1),
]
# models = list()
# for infectivity in np.arange(0.1, 1.5, 0.1):
#     models.append(SIRModel(grid_size, grid_size, infectivity=infectivity, infection_duration=70, immunity_duration=130, mutation_probability=0.1, mutation_strength=1))

start_time = time.strftime("%Y%m%d-%H%M%S")

# Single plots
duration_values = list()
infectivity_values = list()
for index, model in enumerate(models, start=1):

    for i in range(duration):
        model.step()
        if i % 100 == 0 and i > 0:
            print(i)

    # data = model.datacollector_cells.get_model_vars_dataframe()
    infection_duration = model.datacollector_meaninfectionduration.get_model_vars_dataframe()
    infection_duration_value = infection_duration.tail(1)['Mean_inf_duration'].item()
    duration_values.append(infection_duration_value)
    infectivity_values.append(model.infectivity)

plt.plot(infectivity_values, duration_values)
plt.ylabel('Mean evolved infection duration')
plt.xlabel('Infectivity')
plt.savefig(f'figures/{start_time}-duration-vs-infectivy.pdf')
