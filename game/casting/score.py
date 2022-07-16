from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()

        self._points1 = 0
        self._points2 = 0

        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points1 += points
        self._points2 += points

        self.set_text(f" Player: {self._points1}                                                                                                             Player: {self._points2}")
    
    def getPoints1(self):
        return self._points1 
    
    def getPoints2(self):
        return self._points2 