import covidsimulation.common.health_states as health_states

class Agent(object):

    def __init__(self, age_group, health_outcome, incubation_time, days_exposed=0, days_with_symptoms=0, health_state=health_states.susceptible):

        self.age_group = age_group

        self.health_state = health_state
        self.health_outcome = health_outcome

        self.days_exposed = days_exposed
        self.days_with_symptoms = days_with_symptoms

        self.incubation_time = incubation_time

        self.confirmed_case = False

    def cycleDisease(self, sim):
        # use the cycle function for the current health state
        Agent._CYCLE_DISEASE_MAP[self.health_state](self, sim)

        # If infected, increase days of exposure
        if self.health_state == health_states.incubated or self.health_state in health_states.infectious_states:
            self.days_exposed += 1

        # If with symptoms, increase days with symptoms
        if self.health_state in health_states.symptomatic_states:
            self.days_with_symptoms += 1

    def _cycleNoAction(self, sim):
        return

    def _cycleIncubated(self, sim):
        # If contaminated and half the incubation period has passed, becomes asymptomatic
        # TODO why does this happen? why not decide after the full incubation period whether to go asymp or symp?
        if self.days_exposed >= (self.incubation_time / 2): 
            self.health_state = health_states.asymptomatic

    def _cycleAsymptomatic(self, sim):
        
        if self.health_outcome == health_states.asymptomatic:
            
            # outcome is asymptomatic, become immune after fixed period of time
            # TODO 7 is a "magic" number, should be a parameter or a constant which we can verify the source of
            if self.days_exposed >= (self.incubation_time + 7):
                self.health_state = health_states.immune

        else:
            # advance the disease after the incubation period
            if self.days_exposed >= self.incubation_time:
                self.health_state = health_states.symptomaticLight

    def _cycleSymptomaticLight(self, sim):

        if self.health_outcome == health_states.symptomaticLight:
        
            # outcome is light symptoms, become immune after configured number of days
            # TODO why the 0 index? unimplemented thing? if its different times depending on path, separate params is clearer
            if self.days_with_symptoms >= sim.t_discharge[0]:
                self.health_state = health_states.immune
        
        else:
            # advance the disease
            self.health_state = health_states.symptomaticMedium
        
    def _cycleSymptomaticMedium(self, sim):
       
        if self.health_outcome == health_states.symptomaticMedium:
            
            # outcome is medium symptoms, become immune after configured number of days
            # TODO why the 0 index? unimplemented thing? if its different times depending on path, separate params is clearer
            if self.days_with_symptoms >= sim.t_discharge[0]:
                self.health_state = health_states.immune

        else:
            # If need go to the hospital, intern after configured number of days
            if self.days_with_symptoms >= sim.t_hospital:
                
                # individual seeks medical help and becomes a confirmed case
                # TODO is this how we should model this, should it be a parameter?
                self.confirmed_case = True

                # hospital non ICU
                if self.health_outcome == health_states.hospital:
                    self.health_state = health_states.hospital

                # ICU required
                else:
                    self.health_state = health_states.ICU


    def _cycleHospital(self, sim):
        # If in the hospital and alive, leaves after configured number of days immune
        if self.days_with_symptoms >= sim.t_discharge[1]:
            self.health_state = health_states.immune

    def _cycleICU(self, sim):
        
        # after configured number of days in ICU, go into recovery or death
        if self.days_with_symptoms >= sim.t_discharge[2]:
            if self.health_outcome == health_states.ICU:
                self.health_state = health_states.hospital

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
