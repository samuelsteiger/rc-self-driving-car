import plotille

plt = plotille.Canvas(width=20, 
                      height=20,
                       xmin=-10,
                        ymin=-10,
                         xmax=10,
                          ymax=10 )

plt.point(0,0, marker='@')
plt.point(5.5,5.5, marker='#')
plt.point(5,5, marker='@')

plt.point(-5,-5, marker='@')

print(plt.plot())

