import time
import constants
from BaseClass import basic_setup

class PerformanceMonitor():
    def __init__(self):
        self.time = 0
        self.frames = 0
        self.fps = 1
        self.janela = basic_setup.janela
        self.mouse = basic_setup.mouse
        self.teclado = basic_setup.teclado


    def measure_fps(self, janela):
        self.frames += 1
        self.time += janela.delta_time()


        if self.time > 0.5:
            self.fps = self.frames / self.time
            # print("FPS: ", fps)
            self.frames = 0
            self.time = 0
        
        text = "FPS:" + str(round(self.fps, 2))
        self.janela.draw_text(text, constants.WINDOW_WIDTH - 200, constants.WINDOW_HEIGHT - 100, 30, (255, 255, 255))

        
        desired_fps = constants.desired_fps


        #limita o fps de acordo com o desejado
        if self.janela.delta_time() < 1.0/desired_fps:
            # print("FPS maior que o desejado")
            time.sleep((1.0/desired_fps - self.janela.delta_time()))