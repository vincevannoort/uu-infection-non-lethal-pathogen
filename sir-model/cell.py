import random
from mesa import Agent

class Cell(Agent):
    '''Description of the grid points of the CA'''

    # Definitions of state variables    
    Susceptible = 1
    Infected = 2
    Recovered = 3
    
    def __init__(self, pos, model, init_state=1):
        '''Create cell in given x,y position, with given initial state'''
        super().__init__(pos,model)
        self.x,self.y = pos
        self.state = init_state
        self.time_counter = 0

        # infection
        self.infectivity = model.infectivity
        self.infection_duration = model.infection_duration

        # immunity
        self.immunity_duration = model.immunity_duration

        # next step
        self.__next_step_cell__ = None;


    def initialise_as_infected(self):
        self.state = self.Infected
        self.time_counter = random.randint(0, self.infection_duration)

    def initialise_as_recovered(self):
        self.state = self.Recovered
        self.time_counter = random.randint(0, self.immunity_duration)

    def step(self):
        '''Compute the next state of a cell'''
        self.__next_step_cell__ = self

        # Susceptibles
        if self.state == self.Susceptible:
            neighbours = self.model.grid.get_neighbors((self.x, self.y), moore=True, include_center=False)

            # Calculate total infection rating based on neighbours
            total_infectivity = 0.0
            for neighbour in neighbours:
                if neighbour.state == self.Infected:
                    total_infectivity += neighbour.infectivity


            # Calculate the infection probability
            infection_probability = 0.0
            if total_infectivity > 0:
                infection_probability = total_infectivity / (total_infectivity + self.model.h_inf)

            if random.random() < infection_probability:
                self.__next_step_cell__.state = self.Infected

                # filter for infected neighbors
                inf_neighbours = [neighbour for neighbour in neighbours if neighbour.state is self.Infected]

                # inherit infection from one of them
                inf_neighbour = random.choice(inf_neighbours)
                self.__next_step_cell__.infectivity = inf_neighbour.infectivity
                self.__next_step_cell__.infectivition_duration = inf_neighbour.infection_duration

                # reset time counter, infection starts now
                self.__next_step_cell__.time_counter = 0

        # Infected
        # Check if the infection duration has been passed, aka: recovering after amount of time being sick
        elif self.state == self.Infected:
            if self.time_counter > self.infection_duration:
                self.set_state(self.Recovered)

        # Recovered
        # Check if the infection duration has been passed, aka: recovering after amount of time being sick
        elif self.state == self.Recovered:
            if self.time_counter > self.immunity_duration:
                self.set_state(self.Susceptible)

    def set_state(self, state):
        self.__next_step_cell__.state = state
        self.__next_step_cell__.time_counter = 0 

    def advance(self): 
        self = self.__next_step_cell__

        # increase time counter for states that need a duration
        if self.state is self.Infected or self.state is self.Recovered:
            self.time_counter += 1

    def __str__(self):
        return f'Cell | infection: {self.infectivity} -> {self._next_infectivity} | infection duration: {self.infection_duration} -> {self._next_infectivition_duration} | time_counter: {self.time_counter}'
