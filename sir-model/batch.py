from model import SIRModel
import matplotlib.pyplot as plt
import itertools

color_dict = {
    'Susceptible': '#eeeeee', 
    'Infected': '#ff5e5e',
    'Recovered': '#d6ff37'
}

duration = 100

models_infection_variation = [
    SIRModel(100, 100, infection_duration = 5, immunity_duration = 15),
    SIRModel(100, 100, infection_duration = 10, immunity_duration = 15),
    SIRModel(100, 100, infection_duration = 15, immunity_duration = 15),
    SIRModel(100, 100, infection_duration = 25, immunity_duration = 15),
    SIRModel(100, 100, infection_duration = 50, immunity_duration = 15),
]

models_immunity_variation = [
    SIRModel(100, 100, infection_duration = 15, immunity_duration = 5),
    SIRModel(100, 100, infection_duration = 15, immunity_duration = 10),
    SIRModel(100, 100, infection_duration = 15, immunity_duration = 15),
    SIRModel(100, 100, infection_duration = 15, immunity_duration = 25),
    SIRModel(100, 100, infection_duration = 15, immunity_duration = 50),
]

models_equal_variation = [
    # normal configurations
    SIRModel(100, 100, infection_duration = 5, immunity_duration = 5),
    SIRModel(100, 100, infection_duration = 10, immunity_duration = 10),
    SIRModel(100, 100, infection_duration = 15, immunity_duration = 15),
    SIRModel(100, 100, infection_duration = 25, immunity_duration = 25),
    SIRModel(100, 100, infection_duration = 50, immunity_duration = 50),
]

models = [ *models_infection_variation, *models_immunity_variation, *models_equal_variation ]

# Single plots
for index, model in enumerate(models, start=1):

    for i in range(duration):
        model.step()

    data = model.datacollector_cells.get_model_vars_dataframe()
    color = [color_dict.get(x, '#333333') for x in data.columns]
    title = f'Infection duration: {model.infection_duration}, Immunity duration: {model.immunity_duration}'

    data.plot.area(color=color, title=title).legend(loc='upper right')
    plt.margins(0)
    plt.savefig(f'figures/model-result--inf-{model.infection_duration}--imm-{model.immunity_duration}.pdf')
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
    data.plot.area(color=color, title=title, ax=ax).legend(loc='upper right')
plt.savefig(f'figures/model-result--all.pdf', dpi=100)