# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 18:24:55 2019

@author: Roy
"""

## 4 friends are ordering pizza.  The pizza shop sells pizzas of 6 slices and they will all eat four slices
## What is the minimum number of pizzas they need to order? Work this problem using floor division

Number_of_friends = 4
slices_each = 4
slices_needed = Number_of_friends * slices_each
slices_per_pizza = 6
# minimum_required = slices_needed//slices_per_pizza
minimum_required = (slices_needed + 5) // 6
slices_over = minimum_required * 6 - slices_needed
print('The minimum number of pizzas to order is ', minimum_required, ' and there will be ', slices_over, ' slices left')
# slices needed plus 5 as floor division always rounds down
print(f'If four friends each want 4 slices of pizza and the pizzas all have {slices_per_pizza} slices\nthen the minimum number of pizzas needed is {minimum_required}')
print(f'There will be {slices_over} slices left')
