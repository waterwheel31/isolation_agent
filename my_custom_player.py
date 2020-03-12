
from sample_players import DataPlayer
import math


class CustomPlayer(DataPlayer):
    """ Implement your own agent to play knight's Isolation

    The get_action() method is the only required method for this project.
    You can modify the interface for get_action by adding named parameters
    with default values, but the function MUST remain compatible with the
    default interface.

    **********************************************************************
    NOTES:
    - The test cases will NOT be run on a machine with GPU access, nor be
      suitable for using any other machine learning techniques.

    - You can pass state forward to your agent on the next turn by assigning
      any pickleable object to the self.context attribute.
    **********************************************************************
    """
    
    def distance(self, loc1, loc2):
        
        x1 = loc1 // 13 
        y1 = loc1 % 13
        x2 = loc2 // 13
        y2 = loc2 % 13
        
        #print('loc1:', loc1, 'x:', x1, 'y:', y1, 'loc2:', loc2, 'x:', x2, 'y:', y2)
    
        dis = math.sqrt((x1 - x2)**2 + (y1 - y2) **2)
        return dis
        
      
    def wall_distance(self, loc1):
        
        x1 = loc1 // 13 
        y1 = loc1 % 13
    
        left = x1 
        right = 13 - x1 
        up = y1 
        bottom = 10 - y1
    
        dis = min(left, right, up, bottom) + 1
        
        #print(x1, y1, dis)
        
        return dis
    
    
    
    def score(self, state):
        own_loc = state.locs[self.player_id]
        own_liberties = state.liberties(own_loc)
      
        opp_loc = state.locs[1 - self.player_id]
        opp_liberties = state.liberties(opp_loc)
        
        own_liberties_unique = [x for x in own_liberties if x not in opp_liberties]
          
        second_liberties = []
      
    
        for next_step in own_liberties_unique:
            
            second_liberty = state.liberties(next_step)
            second_liberties.extend(second_liberty)
        
        second_liberties = set(second_liberties)
        
        distances = 0
        distances_opp = 0
        
        for loc in second_liberties:
            dis_opp = self.distance(loc, opp_loc)
            distances += dis_opp
           
        
        for loc in opp_liberties:
            dis_opp = self.distance(loc, own_loc)
            distances_opp += dis_opp  
        
 
        
        score = distances / (distances_opp + 0.001)
        
        return score
    
    
    def get_action(self, state):
        """ Employ an adversarial search technique to choose an action
        available in the current state calls self.queue.put(ACTION) at least

        This method must call self.queue.put(ACTION) at least once, and may
        call it as many times as you want; the caller will be responsible
        for cutting off the function after the search time limit has expired.

        See RandomPlayer and GreedyPlayer in sample_players for more examples.

        **********************************************************************
        NOTE: 
        - The caller is responsible for cutting off search, so calling
          get_action() from your own code will create an infinite loop!
          Refer to (and use!) the Isolation.play() function to run games.
        **********************************************************************
        """
        # TODO: Replace the example implementation below with your own search
        #       method by combining techniques from lecture
        #
        # EXAMPLE: choose a random move without any search--this function MUST
        #          call self.queue.put(ACTION) at least once before time expires
        #          (the timer is automatically managed for you)
        import random
        
        #print("state:", state)
        
        #print('action:')
        
        self.queue.put(max(state.actions(), key=lambda x: self.score(state.result(x))))
