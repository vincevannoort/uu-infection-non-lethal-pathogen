from model import SIRModel
import matplotlib.pyplot as plt
import itertools

color_dict = {
    'Susceptible': '#eeeeee', 
    'Infected': '#ff5e5e',
    'Recovered': '#d6ff37'
}

duration = 2000
model = SIRModel(150, 150, infectivity=0.1, infection_duration = 20, immunity_duration = 20, mutation_probability=0.01, mutation_strength=2)

for i in range(duration):
    model.step()

data = model.datacollector_cells.get_model_vars_dataframe()
data_mid = model.datacollector_meaninfectionduration.get_model_vars_dataframe()

color = [color_dict.get(x, '#333333') for x in data.columns]
title = f'Infection duration: {model.infection_duration}, Immunity duration: {model.immunity_duration}'

data.plot.area(color=color, title=title).legend(loc='upper right')
plt.margins(0)
plt.savefig(f'figures/model-result--single--inf-{model.infection_duration}--imm-{model.immunity_duration}.pdf')

data_mid.plot()
plt.savefig(f'figures/inf-dur-result.pdf')
