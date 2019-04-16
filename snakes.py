class Snake:
    """A dangerous and/or harmless serpent."""
    pass


class Cobra(Snake):
    """Definitely dangerous, yup."""
    
    def bite(self, other):
        """Deliver a dose of venom."""
        return other + " is now very sick"
    

    
class BoaConstrictor(Snake):
    """This one gives really good hugs."""
    
    def squeeze(self, other):
        """Give a hug."""
        return other + " does not like to be hugged like that."
        

    
class BoatConstrictor(BoaConstrictor):
    """Loose snakes sink ships?"""
    pass