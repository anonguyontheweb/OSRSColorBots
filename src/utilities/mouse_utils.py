import pyautogui as pag
import numpy as np


class MouseUtils():

    def move_to(self, point: tuple, duration=0.5, variance=0):
        '''
        Moves mouse to a point on screen with a random movement pattern.
        Args:
            point: x, y tuple of the destination point
            duration: duration of the movement
            variance: maximum pixel variance in final x and y position
        '''
        tweens = [pag.easeOutBounce, pag.easeInBounce, pag.easeInBack,
                  pag.easeInCirc, pag.easeInCubic, pag.easeInElastic,
                  pag.easeInExpo, pag.easeInOutBounce, pag.easeInOutQuad,
                  pag.easeInOutQuart, pag.easeInQuart, pag.easeInQuint,
                  pag.easeInOutBack, pag.easeOutSine]
        tween = tweens[np.random.randint(0, len(tweens))]
        x, y = point
        if variance != 0:
            x += np.random.randint(-variance, variance)
            y += np.random.randint(-variance, variance)
        pag.moveTo(x, y, duration=duration, tween=tween)

    def click(self):
        pag.click()