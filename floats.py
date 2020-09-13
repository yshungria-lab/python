x = 0.0
for i in range(10):
    x += 0.1

if x == 1.0:
    print(f'x = {x}')
else:
    print(f'x != {x}')
    
# Es probable que te hayas sorprendido con el resultado. 
#La mayoría de nosotros esperaríamos que imprimiera 1.0 en vez de 0.999999999999. 
#¿Qué es lo que pasó?.
