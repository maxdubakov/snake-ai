SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 480

GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRID_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

map_direction = {0: UP, 1: LEFT, 2: RIGHT, 3: DOWN}

replay_best_plays = False
speed = 500
is_human_playing = False
training = True
first_time_training = False
display = True
load = True
number_of_games = 500
save_period = 50

weights_path = '/home/max/IdeaProjects/snake_evolution_refactored_1/models/weights/weights5.h5'
learning_rate = 0.0005
gamma = 0.9
neurons_each_layer = (24, 16)
batch_size = 1000

reward_for_closer_to_food = 5
reward_for_away_from_food = -3
reward_for_eating = 20
reward_for_dying = -30

snake_color = (255, 255, 255)
food_color = (255, 0, 0)
surface_color1 = (59, 59, 59)
surface_color2 = (41, 41, 41)
text_color = (255, 255, 255)
text_background_color = (0, 0, 0)
font_size = 30

highlight_score_lower_limit = 30
highlights_path = '/home/max/IdeaProjects/snake_evolution_refactored_1/models/highlights/highlights.pkl'
