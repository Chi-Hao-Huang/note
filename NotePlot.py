# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 21:26:54 2023

@author: gerar
"""

import matplotlib.pyplot as plt



plt.scatter([1, 2, 3, 4], [10, 4, 16, 12])
plt.scatter([3], [10])

plt.plot([1, 3],[10, 10], 'k--')


plt.axis([0, 6, 0, 20])
plt.text(1, 1, '123\n456' )
plt.grid(True)
plt.show()

