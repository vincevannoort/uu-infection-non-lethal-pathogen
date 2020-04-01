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
gridwidth = 100 # Change these parameters to change the grid size
gridheight = 100

# Make a grid to plot the population dynamics
grid = CanvasGrid(portrayCell, gridwidth, gridheight, 5*gridwidth, 5*gridheight)
# Make a chart for plotting the density of individuals
chart = ChartModule([
    {"Label": "Infected", "Color": "red"}, 
    {"Label": "Recovered", "Color": "blue"}], 
    {"Label": "Susceptible", "Color": "grey"},
    data_collector_name='datacollector_cells')
# Let chart plot the mean infection time
#chart = ChartModule([{"Label": "Mean_infduration", "Color": "Black"}], data_collector_name='datacollector_meaninfectionduration')


''' Launch the server that will run and display the model '''
server = ModularServer(SIRModel,
                       [grid, chart],
                       "SIR-model",
                       {"width": gridwidth, "height": gridheight})
