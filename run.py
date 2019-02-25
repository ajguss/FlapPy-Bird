import time
import arcade
import threading
from flappy import Game
from brain import QLearningTable

class myThread (threading.Thread):
   def __init__(self):
      print("Creating main thread")
      threading.Thread.__init__(self)
   def run(self):
      print ("Starting Main")
      main()
      print ("Exiting Main")
class myThread2 (threading.Thread):
   def __init__(self):
      print("Creating arcade thread")
      threading.Thread.__init__(self)
   def run(self):
      print ("Starting Arcade")
      arcade.run()()
      print ("Exiting Arcade")

def main():
    time.sleep(5)
    for episode in range(10000):
        max = 0
        time.sleep(1)
        print("Iteration: " + str(episode))
        observation = game.reset()
        observation_ = game.reset()
        while True:
            time.sleep(.2)
            action = RL.choose_action(str(observation))
            observation_, reward, done = game.ML_move(action)
            if(reward > max):
                max = reward
            #print(str(observation) + " R" + str(reward))
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                print(max)
                break
if __name__ == "__main__":
    game = Game(288, 512)
    game.setup()
    reward = 0
    done = False
    RL = QLearningTable(actions=list(range(game.n_actions)))
    
    #arcade.run()
    #start_new_thread(main,())
    thread1 = myThread()
    #thread2 = myThread2()
    thread1.start()
    #thread2.start()
    arcade.run()

