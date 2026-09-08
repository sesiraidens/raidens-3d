"""
Modulo de design 3D para robotica.

Contem funcoes para gerar pecas 3D usando OpenSCAD
e calcular propriedades mecanicas.
"""
import math


class Peca3D:
    """
    Classe base para pecas 3D.
    """
    
    def __init__(self, nome, material="PLA"):
        self.nome = nome
        self.material = material
        self.cor = "gray"
        
    def gerar_openscad(self):
        """Gera codigo OpenSCAD da peca."""
        raise NotImplementedError
        
    def salvar_scad(self, caminho):
        """Salva codigo OpenSCAD em arquivo."""
        codigo = self.gerar_openscad()
        with open(caminho, 'w') as f:
            f.write(codigo)
        print(f"Salvo: {caminho}")
        
    def calcular_volume(self):
        """Calcula volume em cm3."""
        raise NotImplementedError
        
    def calcular_peso(self):
        """Calcula peso em gramas."""
        densidades = {
            "PLA": 1.24,
            "ABS": 1.04,
            "PETG": 1.27,
            "TPU": 1.21,
            "Nylon": 1.14
        }
        densidade = densidades.get(self.material, 1.24)
        volume = self.calcular_volume()
        return volume * densidade


class SuporteSensor(Peca3D):
    """
    Suporte para sensor ultrassonico HC-SR04.
    """
    
    def __init__(self, largura=60, altura=30, profundidade=20):
        super().__init__("Suporte Ultrassonico")
        self.largura = largura
        self.altura = altura
        self.profundidade = profundidade
        
    def gerar_openscad(self):
        """Gera codigo OpenSCAD."""
        return f"""
// Suporte para Sensor Ultrassonico HC-SR04
// RAIDENS - SESI 192

largura = {self.largura};
altura = {self.altura};
profundidade = {self.profundidade};

difference() {{
    // Base
    cube([largura, profundidade, 4]);
    
    // Furos para sensor
    translate([largura/4, profundidade/2, -1])
        cylinder(d=16, h=6, $fn=30);
    translate([3*largura/4, profundidade/2, -1])
        cylinder(d=16, h=6, $fn=30);
}}

// Laterais
translate([0, 0, 4])
    cube([4, profundidade, altura]);
translate([largura-4, 0, 4])
    cube([4, profundidade, altura]);
"""
        
    def calcular_volume(self):
        """Calcula volume."""
        base = self.largura * self.profundidade * 0.4
        laterais = 2 * 4 * self.profundidade * self.altura
        return (base + laterais) / 1000


class SuporteCamera(Peca3D):
    """
    Suporte para camera Raspberry Pi.
    """
    
    def __init__(self, largura=40, altura=30, profundidade=25):
        super().__init__("Suporte Camera")
        self.largura = largura
        self.altura = altura
        self.profundidade = profundidade
        
    def gerar_openscad(self):
        """Gera codigo OpenSCAD."""
        return f"""
// Suporte para Camera Raspberry Pi
// RAIDENS - SESI 192

largura = {self.largura};
altura = {self.altura};
profundidade = {self.profundidade};

difference() {{
    // Base
    cube([largura, profundidade, 3]);
    
    // Furo central para lente
    translate([largura/2, profundidade/2, -1])
        cylinder(d=12, h=5, $fn=30);
    
    // Furos de fixacao
    translate([5, 5, -1])
        cylinder(d=2.5, h=5, $fn=20);
    translate([largura-5, 5, -1])
        cylinder(d=2.5, h=5, $fn=20);
    translate([5, profundidade-5, -1])
        cylinder(d=2.5, h=5, $fn=20);
    translate([largura-5, profundidade-5, -1])
        cylinder(d=2.5, h=5, $fn=20);
}}

// Suporte para lente
translate([largura/2, profundidade/2, 3])
    difference() {{
        cylinder(d=18, h=5, $fn=30);
        cylinder(d=12, h=6, $fn=30);
    }}
"""
        
    def calcular_volume(self):
        """Calcula volume."""
        base = self.largura * self.profundidade * 0.3
        cilindro = math.pi * (9**2) * 0.5
        return (base + cilindro) / 1000


class CarcacaRobo(Peca3D):
    """
    Carcaca principal do robo.
    """
    
    def __init__(self, comprimento=200, largura=150, altura=50):
        super().__init__("Carcaca Robo")
        self.comprimento = comprimento
        self.largura = largura
        self.altura = altura
        
    def gerar_openscad(self):
        """Gera codigo OpenSCAD."""
        return f"""
// Carcaca Principal do Robo
// RAIDENS - SESI 192

comprimento = {self.comprimento};
largura = {self.largura};
altura = {self.altura};
espessura = 3;

difference() {{
    // Base
    hull() {{
        translate([10, 10, 0]) cylinder(r=10, h=espessura, $fn=30);
        translate([comprimento-10, 10, 0]) cylinder(r=10, h=espessura, $fn=30);
        translate([10, largura-10, 0]) cylinder(r=10, h=espessura, $fn=30);
        translate([comprimento-10, largura-10, 0]) cylinder(r=10, h=espessura, $fn=30);
    }}
    
    // Furos de fixacao
    for (x = [20, comprimento-20]) {{
        for (y = [20, largura-20]) {{
            translate([x, y, -1])
                cylinder(d=3, h=espessura+2, $fn=20);
        }}
    }}
}}

// Laterais
translate([0, 0, espessura]) {{
    // Lateral esquerda
    cube([espessura, largura, altura]);
    // Lateral direita
    translate([comprimento-espessura, 0, 0])
        cube([espessura, largura, altura]);
    // Lateral frontal
    translate([0, 0, 0])
        cube([comprimento, espessura, altura]);
    // Lateral traseira
    translate([0, largura-espessura, 0])
        cube([comprimento, espessura, altura]);
}}

// Suportes internos
translate([comprimento/2-10, 10, espessura])
    cube([20, 3, altura/2]);
translate([comprimento/2-10, largura-13, espessura])
    cube([20, 3, altura/2]);
"""
        
    def calcular_volume(self):
        """Calcula volume."""
        base = self.comprimento * self.largura * 0.3
        laterais = 2 * (self.comprimento + self.largura) * 0.3 * self.altura
        return (base + laterais) / 1000


class Roda(Peca3D):
    """
    Roda para robo.
    """
    
    def __init__(self, diametro=65, largura=26, dentes=20):
        super().__init__("Roda")
        self.diametro = diametro
        self.largura = largura
        self.dentes = dentes
        
    def gerar_openscad(self):
        """Gera codigo OpenSCAD."""
        return f"""
// Roda para Robo
// RAIDENS - SESI 192

diametro = {self.diametro};
largura = {self.largura};
dentes = {self.dentes};
raio = diametro/2;

difference() {{
    // Eixo da roda
    cylinder(d=diametro, h=largura, $fn=60);
    
    // Furo central para eixo
    translate([0, 0, -1])
        cylinder(d=8, h=largura+2, $fn=20);
    
    // Furos de reducao de peso
    for (i = [0:dentes-1]) {{
        angulo = i * 360 / dentes;
        translate([raio*0.6*cos(angulo), raio*0.6*sin(angulo), -1])
            cylinder(d=8, h=largura+2, $fn=20);
    }}
}}

// Pneu (cilindro externo)
translate([0, 0, 2])
    difference() {{
        cylinder(d=diametro+4, h=largura-4, $fn=60);
        cylinder(d=diametro, h=largura-3, $fn=60);
    }}
"""
        
    def calcular_volume(self):
        """Calcula volume."""
        cilindro = math.pi * (self.diametro/2)**2 * self.largura
        furos = self.dentes * math.pi * 4**2 * self.largura
        return (cilindro - furos) / 1000


def gerar_conjunto_peca(peca, caminho_saida):
    """
    Gera arquivo .scad com todas as pecas.
    
    Args:
        peca: Objeto Peca3D
        caminho_saida: Caminho do arquivo .scad
    """
    codigo = f"""/*
 * {peca.nome}
 * Material: {peca.material}
 * Gerado por: raidens-3d
 * RAIDENS - SESI 192
 */

{peca.gerar_openscad()}
"""
    with open(caminho_saida, 'w') as f:
        f.write(codigo)
    print(f"Arquivo gerado: {caminho_saida}")
    print(f"Volume estimado: {peca.calcular_volume():.2f} cm3")
    print(f"Peso estimado: {peca.calcular_peso():.2f}g")
