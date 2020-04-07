import random

from mesa import Model
from mesa.time import SimultaneousActivation # updating scheme for synchronous updating
from mesa.time import RandomActivation # for asynchronous updating
from mesa.space import SingleGrid # spatial grid
from mesa.datacollection import DataCollector # Data collection, to plot mean infectivity
import numpy as np

from cell import Cell # Function that describes behaviour of single cells

# Computes the mean infection duration in all infected individuals
def compute_mean_infduration(model):
    infs = [cell.infection_duration for cell in model.schedule.agents if cell.state == cell.Infected]
    if len(infs) is 0:
        return 0
    mean_inf = sum(infs)/len(infs)
    #model.mean_inf_duration_list.append(mean_inf)
    #if len(model.mean_inf_duration_list)>100:
        #print('Mean of infection duration(past 100 iterations):' + str(np.mean(model.mean_inf_duration_list[-100:])))
    return mean_inf

# Computes the fraction of cells filled with an S individual
def fracS(model):
    nS = len([cell.state for cell in model.schedule.agents if cell.state == cell.Susceptible])
    if (nS == 0):
        return 0
    return nS / len(model.schedule.agents)

# Computes the fraction of cells filled with an I individual
def fracI(model):
    nI = len([cell.state for cell in model.schedule.agents if cell.state == cell.Infected])
    if (nI == 0):
        return 0
    return nI / len(model.schedule.agents)

# Computes the fraction of cells filled with an R individual
def fracR(model):
    nR = len([cell.state for cell in model.schedule.agents if cell.state == cell.Recovered])
    if (nR == 0):
        return 0
    return nR / len(model.schedule.agents)

class SIRModel(Model):
    '''Description of the model'''
    
    def __init__(self, width, height, infectivity=2.0, infection_duration = 10, immunity_duration = 15, mutation_probability=0, mutation_strength=10, visualise_each_x_timesteps=-1):
        # Set the model parameters
        self.infectivity = infectivity       # Infection strength per infected individual
        self.infection_duration = infection_duration # Duration of infection
        self.immunity_duration = immunity_duration  # Duration of infection
        
        #mutations
        self.mutation_probability = mutation_probability 
        self.mutation_strength = mutation_strength
        #self.mean_inf_duration_list = []

        percentage_starting_infected = 0.01
        percentage_starting_recovered = 0.01
       
        self.visualise_each_x_timesteps = visualise_each_x_timesteps
        self.grid = SingleGrid(width, height, torus=False)
        self.schedule = SimultaneousActivation(self)
        for (contents, x, y) in self.grid.coord_iter():
            # Place randomly generated individuals
            rand = random.random()
            cell = Cell((x,y), self)

            # place random infected cells with a chance
            if rand < percentage_starting_infected:
                cell.initialise_as_infected()

            # place random infected cells with a chance
            elif rand < percentage_starting_infected + percentage_starting_recovered:
                cell.initialise_as_recovered()

            self.grid.place_agent(cell, (x,y))
            self.schedule.add(cell)

        # Add data collector, to plot the number of individuals of different types
        self.datacollector_cells = DataCollector(model_reporters={
            "Infected": fracI,
            "Recovered": fracR,
            "Susceptible": fracS,
        })

        # Add data collector, to plot the mean infection duration
        self.datacollector_meaninfectionduration = DataCollector(model_reporters={"Mean_inf_duration": compute_mean_infduration})

        # collects grids per amount of time steps
        self.grids_saved = []
        
        self.running = True

    def get_grid_cells(self):
        return np.array([cell.state for cell in self.schedule.agents])

    def step(self):
        # collect grids for running without browser
        if self.visualise_each_x_timesteps != -1:
            if self.schedule.time % self.visualise_each_x_timesteps == 0:
                print(f'timestep: {self.schedule.time}, saved grid.')
                self.grids_saved.append(self.get_grid_cells())

        self.datacollector_cells.collect(self)
        self.datacollector_meaninfectionduration.collect(self)

        self.schedule.step()
    
