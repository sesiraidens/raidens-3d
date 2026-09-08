<div align="center">

<img src="https://sesiraidens.github.io/portifolio/assets/logo_color-aNRVU26Y.png" width="80">

# raidens-3d

Design e geracao de pecas 3D para robos usando OpenSCAD.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![OpenSCAD](https://img.shields.io/badge/OpenSCAD-F80000?style=flat)
![License](https://img.shields.io/badge/License-MIT-d9333b?style=flat)
![Status](https://img.shields.io/badge/Status-Active-2ea043?style=flat)

</div>

---

## Sobre

O **raidens-3d** fornece classes para gerar pecas 3D parametrizadas para robos. Gera arquivos OpenSCAD prontos para impressao 3D.

---

## Estrutura

`
raidens-3d/
├── src/
│   ├── pecas.py          # Gerador de pecas
│   └── __init__.py
├── examples/
│   ├── gerar_suporte.py
│   └── gerar_carcaca.py
└── README.md
`

---

## Pecas Disponiveis

### SuporteSensor

Suporte para sensor ultrassonico HC-SR04.

`python
from src.pecas import SuporteSensor

suporte = SuporteSensor(largura=60, altura=30)
suporte.salvar_scad("suporte_sensor.scad")
`

### SuporteCamera

Suporte para camera Raspberry Pi.

`python
from src.pecas import SuporteCamera

suporte = SuporteCamera(largura=40, altura=30)
suporte.salvar_scad("suporte_camera.scad")
`

### CarcacaRobo

Carcaca principal do robo.

`python
from src.pecas import CarcacaRobo

carcaca = CarcacaRobo(comprimento=200, largura=150, altura=50)
carcaca.salvar_scad("carcaca.scad")
`

### Roda

Roda para robo com pneu.

`python
from src.pecas import Roda

roda = Roda(diametro=65, largura=26, dentes=20)
roda.salvar_scad("roda.scad")
`

---

## Calculos

### Volume e Peso

`python
peca = Roda(diametro=65)
print(f"Volume: {peca.calcular_volume():.2f} cm3")
print(f"Peso: {peca.calcular_peso():.2f}g")
`

### Materiais Suportados

| Material | Densidade (g/cm3) |
|---|---|
| PLA | 1.24 |
| ABS | 1.04 |
| PETG | 1.27 |
| TPU | 1.21 |
| Nylon | 1.14 |

---

## Workflow

1. **Criar peca** com parametros desejados
2. **Gerar arquivo .scad** com salvar_scad()
3. **Abrir no OpenSCAD** e ajustar se necessario
4. **Exportar STL** para impressora
5. **Imprimir 3D**

---

## Dicas de Design

### Espessura Minima

- Pecas estruturais: 2-3mm
- Pecas flexiveis: 1-1.5mm
- Pecas decorativas: 0.8-1mm

### Angulos

- Angulo maximo sem suporte: 45 graus
- Raio minimo de curva: 1mm

### Tolerancias

- Furos para parafusos: +0.2mm
- Encaixes: +0.1mm
- Pecas moveis: +0.3mm

---

## Equipe

**RAIDENS - SESI Aluminio 192**

Desenvolvido para uso interno da equipe. Licenciado sob MIT.