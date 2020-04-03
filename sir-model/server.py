from mesa.visualization.modules import CanvasGrid
from mesa.visualization.modules import ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from model import SIRModel

''' Portrayal function: defines the portrayal of the cells '''
def portrayCell(cell):
    assert cell is not None
    portrayal = {"Shape": "rect",
                 "w": 1,
                 "h": 1,
                 "Filled": "true",
                 "Layer": 1,
                 "Color": "white"} # Default colour, used for empty cells.
    if cell.state == cell.Susceptible:
        portrayal["Color"] = "grey"
    elif cell.state == cell.Infected:
        portrayal["Color"] = "red"
    elif cell.state == cell.Recovered:
        portrayal["Color"] = "blue"

    return portrayal


''' Construct the simulation grid, all cells displayed as 5x5 squares '''
gridwidth = 150 # Change these parameters to change the grid size
gridheight = 150

# Make a grid to plot the population dynamics
grid = CanvasGrid(portrayCell, gridwidth, gridheight, 5*gridwidth, 5*gridheight)
# Make a chart for plotting the density of individuals
chart1 = ChartModule([
    {"Label": "Infected", "Color": "red"}, 
    {"Label": "Recovered", "Color": "blue"}, 
    {"Label": "Susceptible", "Color": "grey"}],
    data_collector_name='datacollector_cells')
# Let chart plot the mean infection time
chart2 = ChartModule([{"Label": "Mean_inf_duration", "Color": "Black"}], data_collector_name='datacollector_meaninfectionduration')


''' Launch the server that will run and display the model '''
server = ModularServer(SIRModel,
                       [grid, chart1, chart2],
                       "SIR-model",
                       {"width": gridwidth, "height": gridheight, "infectivity": 0.1, "infection_duration": 5, "immunity_duration": 5, "mutation_probability": 0.01, "mutation_strength": 2})
