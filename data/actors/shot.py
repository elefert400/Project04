## @file shot.py
#  Source file for shot object
#
#  Project: Galaga Clone
#  Author: Py Five
#  Created: 10/17/18

from .. import setup, actor


## @class Shot
#  @brief Implements Actor base class as Shot object
class Shot(actor.Actor):

    ## Constructor
    #  @param image, surface object with Shot image
    #  @param player, Player object that fired the shot
    def __init__(self, player):
        #actor.Actor.__init__(self, setup.IMAGES['missile1'])
        actor.Actor.__init__(self, setup.IMAGES['torpedo'])
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top - 5

    # Updates the shot object
    def update(self):
        self.rect.top = self.rect.top - 10

    ## Checks for collisions
    #  @param actor, check collisions with this actor
    #  @returns bool, True if collision is detected; false, otherwise
    def collision_check(self, actor):
        return self.rect.colliderect(actor.rect)
