import numpy as np
import random

GRID_HEIGHT = 5  
GRID_WIDTH = 5    
NUM_EPISODES = 500
MAX_STEPS = 50

ALPHA = 0.1       
GAMMA = 0.9       
EPSILON = 0.1     


ACTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'STAY']


Q = {}

def init_Q():
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            Q[(row, col)] = {a: 0 for a in ACTIONS}

def choose_action(state):
    if random.uniform(0,1) < EPSILON:
        return random.choice(ACTIONS)
    else:
        return max(Q[state], key=Q[state].get)

def move_agent(state, action):
    row, col = state
    if action == 'UP':
        row = max(0, row - 1)
    elif action == 'DOWN':
        row = min(GRID_HEIGHT - 1, row + 1)
    elif action == 'LEFT':
        col = max(0, col - 1)
    elif action == 'RIGHT':
        col = min(GRID_WIDTH - 1, col + 1)
    return (row, col)

def move_cars(car_positions):
   
    return [(r, (c + 1) % GRID_WIDTH) for (r, c) in car_positions]

def is_collision(agent_pos, car_positions):
    return agent_pos in car_positions

def train():
    init_Q()
    for episode in range(NUM_EPISODES):
        agent_pos = (0, GRID_WIDTH // 2)  
        car_positions = [(2, i) for i in range(GRID_WIDTH)]  
        for step in range(MAX_STEPS):
            action = choose_action(agent_pos)
            next_pos = move_agent(agent_pos, action)
            car_positions = move_cars(car_positions)
            
          
            if next_pos[0] == GRID_HEIGHT - 1:
                reward = 10 
                Q[agent_pos][action] += ALPHA * (reward + GAMMA * 0 - Q[agent_pos][action])
                break
            elif is_collision(next_pos, car_positions):
                reward = -10  
                Q[agent_pos][action] += ALPHA * (reward + GAMMA * 0 - Q[agent_pos][action])
                break
            else:
                reward = -1 
                best_next = max(Q[next_pos], key=Q[next_pos].get)
                Q[agent_pos][action] += ALPHA * (reward + GAMMA * Q[next_pos][best_next] - Q[agent_pos][action])
                agent_pos = next_pos

def test_agent():
    agent_pos = (0, GRID_WIDTH // 2)
    car_positions = [(2, i) for i in range(GRID_WIDTH)]
    for step in range(MAX_STEPS):
        action = max(Q[agent_pos], key=Q[agent_pos].get)
        next_pos = move_agent(agent_pos, action)
        car_positions = move_cars(car_positions)
        
        print(f"Step {step}: Agent at {agent_pos}, Action: {action}")
        
        if next_pos[0] == GRID_HEIGHT - 1:
            print("🎯 Agent reached the goal!")
            break
        if is_collision(next_pos, car_positions):
            print("💥 Agent collided with a car!")
            break
        agent_pos = next_pos

if __name__ == "__main__":
    train()
    print("\n--- Testing agent after training ---")
    test_agent()
