<div align="center">

<img src="https://sesiraidens.github.io/portifolio/assets/logo_color-aNRVU26Y.png" alt="Logo RAIDENS" width="140">

# raidens-3d

**Peças 3D paramétricas para robôs, geradas em Python e exportadas para OpenSCAD**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![OpenSCAD](https://img.shields.io/badge/OpenSCAD-.scad-F9D72C?style=flat-square&logo=openscad&logoColor=black)
![Licença MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-D9333B?style=flat-square)

[Sobre](#sobre) · [Instalação](#instalação) · [Peças](#peças-disponíveis) · [Fluxo](#do-código-à-impressora) · [Boas práticas](#boas-práticas-de-design)

</div>

---

## Sobre

O **raidens-3d** transforma as medidas do robô em peças prontas para imprimir. Em vez de redesenhar um suporte toda vez que o sensor muda de lugar, você ajusta os parâmetros em Python e gera um novo arquivo `.scad`.

Cada peça também estima volume e peso conforme o material, o que ajuda a manter o robô dentro do limite de massa da competição.

## Instalação

```bash
git clone https://github.com/sesiraidens/raidens-3d.git
cd raidens-3d
```

Requer Python 3.8 ou superior e o [OpenSCAD](https://openscad.org/) para visualizar e exportar as peças.

## Peças disponíveis

| Classe | Peça | Parâmetros (mm) |
|---|---|---|
| `SuporteSensor` | Suporte para ultrassônico HC-SR04 | `largura`, `altura`, `profundidade` |
| `SuporteCamera` | Suporte para câmera Raspberry Pi | `largura`, `altura`, `profundidade` |
| `CarcacaRobo` | Carcaça principal | `comprimento`, `largura`, `altura` |
| `Roda` | Roda com pneu | `diametro`, `largura`, `dentes` |

```python
from src.pecas import SuporteSensor, Roda

SuporteSensor(largura=60, altura=30).salvar_scad("suporte_sensor.scad")

roda = Roda(diametro=65, largura=26, dentes=20)
roda.salvar_scad("roda.scad")
print(f"{roda.calcular_volume():.2f} cm³ · {roda.calcular_peso():.2f} g")
```

### Materiais

| Material | Densidade (g/cm³) |
|---|---|
| PLA | 1,24 |
| ABS | 1,04 |
| PETG | 1,27 |
| TPU | 1,21 |
| Nylon | 1,14 |

## Do código à impressora

1. Crie a peça com as medidas do seu robô.
2. Gere o `.scad` com `salvar_scad()`.
3. Abra no OpenSCAD e confira a pré-visualização.
4. Exporte para STL.
5. Fatie e imprima.

## Boas práticas de design

| Aspecto | Recomendação |
|---|---|
| Espessura de peças estruturais | 2 a 3 mm |
| Espessura de peças flexíveis | 1 a 1,5 mm |
| Espessura de peças decorativas | 0,8 a 1 mm |
| Ângulo máximo sem suporte | 45° |
| Raio mínimo de curva | 1 mm |
| Folga em furos para parafuso | +0,2 mm |
| Folga em encaixes | +0,1 mm |
| Folga em peças móveis | +0,3 mm |

## Estrutura

```text
raidens-3d/
└── src/
    └── pecas.py   # Peca3D base e as peças paramétricas
```

## Ecossistema RAIDENS

Este repositório faz parte de um conjunto de bibliotecas da equipe. Elas usam os mesmos nomes de classes e convenções, então o que você aprende em uma serve nas outras.

| Repositório | Para quê |
|---|---|
| [`raidens-python`](https://github.com/sesiraidens/raidens-python) | Biblioteca principal em Python: sensores, motores e robôs prontos (seguidor, parede, resgate) |
| [`raidens-arduino`](https://github.com/sesiraidens/raidens-arduino) | As mesmas abstrações em C++ para rodar direto no Arduino |
| [`raidens-sensores`](https://github.com/sesiraidens/raidens-sensores) | Catálogo completo de sensores com calibração e filtragem |
| [`raidens-motores`](https://github.com/sesiraidens/raidens-motores) | Motores DC, servo, passo, driver L298N e rodas mecanum |
| [`raidens-pid`](https://github.com/sesiraidens/raidens-pid) | Controladores PID, PID avançado, cascata e sintonia Ziegler-Nichols |
| [`raidens-opencv`](https://github.com/sesiraidens/raidens-opencv) | Visão computacional: cores, linhas e navegação por câmera |
| [`raidens-lab`](https://github.com/sesiraidens/raidens-lab) | Calibração interativa de cores em HSV e LAB |
| [`raidens-obr`](https://github.com/sesiraidens/raidens-obr) | Robô completo para a OBR, integrando sensores, motores e missões |
| [`raidens-electronics`](https://github.com/sesiraidens/raidens-electronics) | Cálculos e modelos de componentes eletrônicos |
| [`raidens-ros`](https://github.com/sesiraidens/raidens-ros) | Estrutura de nodes e tópicos ROS 2 |
| [`raidens-snippets`](https://github.com/sesiraidens/raidens-snippets) | Trechos de código prontos para copiar e colar |

---

<div align="center">

<img src="https://sesiraidens.github.io/portifolio/assets/logo_color-aNRVU26Y.png" alt="Logo RAIDENS" width="56">

**Equipe RAIDENS** · SESI 192 Alumínio/SP

[![Email](https://img.shields.io/badge/Email-sesiraidens%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:sesiraidens@gmail.com)
[![Linktree](https://img.shields.io/badge/Linktree-sesiraidens-39E06B?style=flat-square&logo=linktree&logoColor=white)](https://linktr.ee/sesiraidens)
[![GitHub](https://img.shields.io/badge/GitHub-sesiraidens-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sesiraidens)

<sub>Desenvolvido pela equipe RAIDENS para fins educacionais. Licenciado sob MIT.</sub>

</div>
