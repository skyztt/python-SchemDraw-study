# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import SchemDraw as schem
import SchemDraw.elements as e


def addArduino(draw):
    left = {'cnt': 10,
            'labels': ['RESET', 'RESET2', 'AREF', 'N/C', 'A0', 'A1', 'A2', 'A3', 'A4/SDA', 'A5/SCL'],
            'plabels': ['2', '6', '7'],
            'lblsize': 12,
            }
    right = {'cnt': 17,
             'labels': ['TX/D0', 'RX/D1', 'D2', 'PWM D3', 'D4', 'PWM D5', 'PWM D6', 'D7', 'D8', 'PWM D9', 'SS/PWM D10',
                        'MOSI/PWM D11', 'MISO/D12', 'SCK/D13', 'ICSP2 MISO', 'ICSP2 SCK', 'ICSP MISO'],
             'plabels': ['5', '3'],
             'lblsize': 12,
             }
    top = {'cnt': 3,
           'labels': ['3v3', '5v', 'VIN'],
           'plabels': ['4', '8'],
           'lblsize': 12,
           }
    bot = {'cnt': 1,
           'labels': ['GND'],
           'lblsize': 12,
           }
    return e.blackbox(draw.unit * 2.5, draw.unit * 4.5,
                      linputs=left, rinputs=right, tinputs=top, binputs=bot,
                      leadlen=1, mainlabel='Arduino\nUno\n(Rev3)')


d = schem.Drawing()
ICArduino = addArduino(d)

T = d.add(ICArduino)
d.add(e.LINE, d='down', xy = T.GND, l=d.unit * 0.5)
BOT = d.add(e.GND)  # Note: Anchors named same as pin labels
d.add(e.DOT)

d.add(e.LINE, d='up', xy=getattr(T, '5v'), l=d.unit * 0.3)
d.add(e.LINE, d='left', l=d.unit * 2.5)
pot = d.add(e.POT, d='down', label='Rb', toy=BOT.start)
d.add(e.LINE, d='right', tox=BOT.start)
d.add(e.LINE, d='right', xy=pot.tap, l=d.unit * 0.5)
d.add(e.LINE, d='down', toy = T.A0)
d.add(e.LINE, d='right', to = T.A0)

d.add(e.RES, d='right', xy = T.TXD0)
d.add(e.LED, d='down', toy = BOT.start)
d.add(e.LINE, d='left', to = BOT.start)

lenBeAdded = 1

ledPortArray = ['RXD1', 'D2', 'PWMD3', 'D4', 'PWMD5', 'PWMD6', 'D7', 'D8'];
               
for portName in ledPortArray:
    lenBeAdded += 0.5
    d.add(e.RES, d='right', xy = getattr(T, portName), l=d.unit * lenBeAdded)
    d.add(e.LED, d='down', toy = BOT.start)
    d.add(e.LINE, d='left', to = BOT.start)


d.draw()