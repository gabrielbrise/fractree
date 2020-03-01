class TreeConfig:
    def __init__(self):
        self.angle_module = 15             # módulo do angulo para calculo a cada passo do crescimento
        self.angle_before = -30            # angulo inicial após o primeiro tronco
        self.old_x = 775                   # coordenada x inicial
        self.old_y = 730                   # coordenada y inicial
        self.levels = 25                   # profundidade máxima das ramificações
        self.d = -150                      # distância inicial do passo da ramificação
        self.random_range = 2              # aleatoriedade do multiplicador de angulo de cada passo
        self.width = .75
        self.tree_number = 1
        self.slow_drawing = False
        self.tree_cache = []
                                           # espessura inicial do tronco


    # def initialize():
    #     angle_module = 15             # módulo do angulo para calculo a cada passo do crescimento
    #     angle_before = -30            # angulo inicial após o primeiro tronco
    #     old_x = 725                   # coordenada x inicial
    #     old_y = 675                   # coordenada y inicial
    #     levels = 25                   # profundidade máxima das ramificações
    #     d = -150                      # distância inicial do passo da ramificação
    #     random_range = 2              # aleatoriedade do multiplicador de angulo de cada passo
    #     start_twig_w = levels / 1.75  # espessura inicial do tronco
    #     return angle_module, angle_before, old_x, old_y, levels, d, random_range, start_twig_w