from model import SIRModel
import matplotlib.pyplot as plt
import itertools

color_dict = {
    'Susceptible': '#eeeeee', 
    'Infected': '#ff5e5e',
    'Recovered': '#d6ff37'
}

duration = 100
model = SIRModel(100, 100, infection_duration = 15, immunity_duration = 15)

for i in range(duration):
    model.step()

data = model.datacollector_cells.get_model_vars_dataframe()
color = [color_dict.get(x, '#333333') for x in data.columns]
title = f'Infection duration: {model.infection_duration}, Immunity duration: {model.immunity_duration}'

data.plot.area(color=color, title=title).legend(loc='upper right')
plt.margins(0)
plt.savefig(f'figures/model-result--single--inf-{model.infection_duration}--imm-{model.immunity_duration}.pdf')
print(f'Single plot done for: {title}')
