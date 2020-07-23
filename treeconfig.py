class TreeConfig:
    def __init__(self):
        self.angle_module = 15             # módulo do angulo para calculo a cada passo do crescimento
        self.angle_before = -30            # angulo inicial após o primeiro tronco
        self.levels = 25                   # profundidade máxima das ramificações
        self.d = -150                      # distância inicial do passo da ramificação                                     
        self.random_range = 2              # aleatoriedade do multiplicador de angulo de cada passo
        self.width = .75
        self.tree_number = 1
        self.slow_drawing = False
        self.tree_cache = []
