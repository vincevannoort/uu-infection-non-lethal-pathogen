from model import SIRModel
import matplotlib.pyplot as plt
import itertools
import time

color_dict = {
    'Recovered': '#d6ff37',
    'Susceptible': '#eeeeee', 
    'Infected': '#ff5e5e',
}

duration = 800
grid_size = 100

models_infection_variation = [
    SIRModel(grid_size, grid_size, infectivity = 1, infection_duration = 10, immunity_duration = 70),
    SIRModel(grid_size, grid_size, infectivity = 1, infection_duration = 40, immunity_duration = 70),
    SIRModel(grid_size, grid_size, infectivity = 1, infection_duration = 70, immunity_duration = 70),
    SIRModel(grid_size, grid_size, infectivity = 1, infection_duration = 100, immunity_duration = 70),
    SIRModel(grid_size, grid_size, infectivity = 1, infection_duration = 130, immunity_duration = 70),
]

models_immunity_variation = [
    SIRModel(grid_size, grid_size, infectivity = 1, infection_duration = 70, immunity_duration = 10),
    SIRModel(grid_size, grid_size, infectivity = 1, infection_duration = 70, immunity_duration = 40),
    SIRModel(grid_size, grid_size, infectivity = 1, infection_duration = 70, immunity_duration = 70),
    SIRModel(grid_size, grid_size, infectivity = 1, infection_duration = 70, immunity_duration = 100),
    SIRModel(grid_size, grid_size, infectivity = 1, infection_duration = 70, immunity_duration = 130),
]

models_equal_variation = [
    # normal configurations
    SIRModel(grid_size, grid_size, infectivity = 1, infection_duration = 10, immunity_duration = 10),
    SIRModel(grid_size, grid_size, infectivity = 1, infection_duration = 40, immunity_duration = 40),
    SIRModel(grid_size, grid_size, infectivity = 1, infection_duration = 70, immunity_duration = 70),
    SIRModel(grid_size, grid_size, infectivity = 1, infection_duration = 100, immunity_duration = 100),
    SIRModel(grid_size, grid_size, infectivity = 1, infection_duration = 130, immunity_duration = 130),
]

models = [ *models_infection_variation, *models_immunity_variation, *models_equal_variation ]
start_time = time.strftime("%Y%m%d-%H%M%S")

# Single plots
for index, model in enumerate(models, start=1):

    for i in range(duration):
        model.step()

    data = model.datacollector_cells.get_model_vars_dataframe()
    color = [color_dict.get(x, '#333333') for x in data.columns]
    title =  f'Infection duration: {model.infection_duration}, Immunity duration: {model.immunity_duration}'

    print(type(data))
    print(data)
    data.plot.area(color=color, title=title, lw=3).legend(loc='upper right')
    plt.margins(0)
    plt.xlabel('Time')
    plt.ylabel('Population fraction')
    plt.savefig(f'figures/{start_time}-single-{index}.pdf')
    print(f'Single plot done for: {title}')


# Python magic to zip them
models_for_sub_plot = list(zip(models_infection_variation, models_immunity_variation, models_equal_variation))
models_for_sub_plot = list(itertools.chain.from_iterable(models_for_sub_plot))

# Big plot
fig, axes = plt.subplots(nrows=5, ncols=3, figsize=(15,15))
plt.subplots_adjust(wspace=0.3, hspace=0.3)
for index, ax in enumerate(axes.reshape(-1)):
    # check if the plot can fit in the model
    if index >= len(models_for_sub_plot):
        continue

    model = models_for_sub_plot[index]
    for i in range(duration):
        model.step()
        
    data = model.datacollector_cells.get_model_vars_dataframe()
    color = [color_dict.get(x, '#333333') for x in data.columns]
    title = f'Infection duration: {model.infection_duration}, Immunity duration: {model.immunity_duration}'
    print(f'Sub plot done for: {title}')
    # plot as single graph
    data.plot.area(color=color, title=title, lw=3, ax=ax).legend(loc='upper right')
plt.savefig(f'figures/{start_time}-all.pdf', dpi=100)
