EXPECTED_BAKE_TIME = 40

def bake_time_remaining(done):
    return EXPECTED_BAKE_TIME-done

def preparation_time_in_minutes(layers):
    PREPARATION_TIME = layers*2
    return PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    total_time = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return total_time
