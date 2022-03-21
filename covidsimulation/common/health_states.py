    # ========================================================================
    #	  					Health states legend
    # Susceptible - No exposure to the disease
    # Immune - Had the disease and recovered
    # Dead - Had the disease and died
    # Incubated - Exposed to the disease but not yet exhibiting symptoms
    # Asymptomatic - 
    # Symptomatic light
    # Symptomatic medium
    # Hospital # TODO is this a relevent health state or a statement of location
    # ICU
susceptible = 0
immune = 1
dead = 2
incubated = 3
asymptomatic = 4
symptomaticLight = 5
symptomaticMedium = 6
hospital = 7
ICU = 8

symptomatic_states = [symptomaticLight, symptomaticMedium, hospital, ICU]
infectious_states = [asymptomatic] + symptomatic_states
health_outcomes = infectious_states + [dead] # order matters for the probability distribution in init_model

NUM_INTERNAL_STATES = 9



