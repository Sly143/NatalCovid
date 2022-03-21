import covidsimulation.common.health_states as health_states

class Agent(object):

    def __init__(self, age_group, health_outcome, incubation_time, neighborhood=None, days_exposed=0, days_with_symptoms=0, days_in_icu=0, agentLayers=[], health_state=health_states.susceptible):

        self.age_group = age_group

        self.health_state = health_state
        self.health_outcome = health_outcome

        self.days_exposed = days_exposed
        self.days_with_symptoms = days_with_symptoms
        self.days_in_icu = days_in_icu

        self.incubation_time = incubation_time
        self.contaminated = False

        self.confirmed_case = False
        self.getInfectedInLayer = False
        self.dayInfected = False
        self.countDayContaminated = 0
        
        self.neighborhood = int(neighborhood)
        self.agentLayers = ["home"]
        self.health_stateStats = [0 for i in range(health_states.NUM_INTERNAL_STATES)]
    
    def cycleDisease(self, sim):
        # Use the cycle function for the current health state
        Agent._CYCLE_DISEASE_MAP[self.health_state](self, sim)

        # Set contaminated False to health states: susceptible, immune, dead, symptomaticMedium, hospital, ICU
        if self.health_state in health_states.noTransmission_health_state:
            self.contaminated = False

        # If infected, increase days of exposure
        if self.health_state == health_states.incubated or self.health_state in health_states.infectious_states:
            self.days_exposed += 1

        # If with symptoms, increase days with symptoms
        if self.health_state in health_states.symptomatic_states:
            self.health_stateStats[self.health_state] += 1
            self.days_with_symptoms += 1            

        # If health state is ICU or Dead, increase count of days in ICU
        if self.health_state == health_states.ICU or self.health_state == health_states.dead:
            self.days_in_icu +=1
    

    def _cycleNoAction(self, sim):
        return

    def _cycleIncubated(self, sim):
        
        # Count number of days in this health state
        self.health_stateStats[self.health_state] += 1

        # If days exposed to disease >= 4 days, become contaminated and can contaminate other agents
        if (self.incubation_time / 2) >= 4:
            self.contaminated = True
        
        # If contaminated and half the incubation period has passed, becomes asymptomatic
        # TODO why does this happen? why not decide after the full incubation period whether to go asymp or symp?
        if self.days_exposed >= (self.incubation_time / 2): 
            self.health_state = health_states.asymptomatic

    def _cycleAsymptomatic(self, sim):
        
        # Count number of days in this health state
        self.health_stateStats[self.health_state] += 1
        
        if self.health_outcome == health_states.asymptomatic:
            
            # If days exposed to disease >= 2 days, become contaminate agent
            if self.days_exposed >= 2:
                self.contaminated = True
            
            # If days exposed to disease >= incubation time + 7 - 2 days, don't longer can contaminate other agents
            if self.days_exposed >= ((self.incubation_time + 7)-2):
                self.contaminated = False
            
            # Outcome is asymptomatic, become immune after fixed period of time
            # TODO 7 is a "magic" number, should be a parameter or a constant which we can verify the source of
            if self.days_exposed >= (self.incubation_time + 7):
                self.health_state = health_states.immune
        else:
            # Advance the disease after the incubation period
            if self.days_exposed >= self.incubation_time:
                self.health_state = health_states.symptomaticLight

    def _cycleSymptomaticLight(self, sim):

        if self.health_outcome == health_states.symptomaticLight:
            # Passed days with symptoms, become contaminated agent
            if self.days_with_symptoms <= (sim.t_discharge[0]/2):
                self.contaminated = True
            
            # Passed days with symptoms, no longer spread the disease
            if self.days_with_symptoms > (sim.t_discharge[0]/2):
                self.contaminated = False

            # outcome is light symptoms, become immune after configured number of days
            # TODO why the 0 index? unimplemented thing? if its different times depending on path, separate params is clearer
            if self.days_with_symptoms >= sim.t_discharge[0]:
                self.health_state = health_states.immune
        
        else:
            # Advance the disease
            self.health_state = health_states.symptomaticMedium
        
    def _cycleSymptomaticMedium(self, sim):

        if self.health_outcome == health_states.symptomaticMedium:
            # Outcome is medium symptoms, become immune after configured number of days
            # TODO why the 0 index? unimplemented thing? if its different times depending on path, separate params is clearer

            # If days with symptoms >= time of t_discharge[1] + 1 days (1 day for symptomatic light)
            if self.days_with_symptoms >= sim.t_discharge[1] + 1:
                self.health_state = health_states.immune

        else:
            # If need go to the hospital
            self.health_state = health_states.hospital

    def _cycleHospital(self, sim):

        # If in the hospital and alive, leaves after configured number of days immune
        if self.health_outcome == health_states.hospital: 
                        
            # individual seeks medical help and becomes a confirmed case
            self.confirmed_case = True

            # If days with symptoms >= time on hospital + 2 days (1 day for Symptomatic Light and 1 for Medium)
            if self.days_with_symptoms >= sim.t_hospital + 2:
                self.health_state = health_states.immune
        
        # ICU required
        if self.health_outcome == health_states.ICU or self.health_outcome == health_states.dead:
            self.health_state = health_states.ICU


    def _cycleICU(self, sim):

        # If days in ICU >= ICU time required + 2 (1 day for Symptomatic Medium and 1 for Hospital)
        if self.days_in_icu >= sim.t_discharge[2]+3:
            
            # After configured number of days in ICU
            # Go to immune state
            if self.health_outcome == health_states.ICU:
                self.health_state = health_states.immune

            # Go to death state
            elif self.health_outcome == health_states.dead:
                self.health_state = health_states.dead


    _CYCLE_DISEASE_MAP = {
        health_states.susceptible: _cycleNoAction,
        health_states.immune: _cycleNoAction,
        health_states.dead: _cycleNoAction,
        health_states.incubated: _cycleIncubated,
        health_states.asymptomatic: _cycleAsymptomatic,
        health_states.symptomaticLight: _cycleSymptomaticLight,
        health_states.symptomaticMedium: _cycleSymptomaticMedium,
        health_states.hospital: _cycleHospital,
        health_states.ICU: _cycleICU
    }
