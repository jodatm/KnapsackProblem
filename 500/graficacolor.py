#!/usr/bin/python
# -*- coding: utf-8 -*- 
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
plt.rc('xtick',labelsize=6)
plt.rc('ytick',labelsize=6)


#Caso SWHD
#Iteracion
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])

#Fitness
z = np.array([49269.216383489,48955.641494145,48584.713284348,48239.224137661,47962.519240851,47682.633502728,47423.372989596,47265.554940776,47100.635814537,46958.02274112,46774.519163444,46596.608851917,46480.643072577,46307.767442017,46195.323392808,46101.187675228,45985.968958682,45899.401573248,45729.228765768,45621.219020203,45468.786805476,45429.816831412,45334.329393363,45254.31459634,45158.634283774,45127.836048937,44937.271355838,44831.194942907,44795.391765983,
44708.240554602])

#Tiempo
y = np.array([1.496502535,2.849651035,4.153906409,5.438761036,6.715015944,7.976759362,9.227024659,10.465325038,11.700418504,12.920732045,14.133202251,15.325245762,16.51141386,17.684297085,18.847839268,20.004858772,21.168912117,22.305352926,23.430900534,24.556511792,25.66868128,26.780513604,27.889538447,29.004400428,30.108533422,31.199087874,32.282227524,33.375245372,34.463376093,35.543065572])
x, y = np.meshgrid(x, y)

fig = plt.figure()

ax = fig.add_subplot(2, 2, 1, projection='3d')


surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True, label="SWHD")

plt.xlabel(u"Iteración", fontsize=7)
plt.ylabel(u"Tiempo", fontsize=7)                       
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.set_title(u'Estrategias swbest', fontsize=10)

#Caso 

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])


z = np.array([50193.007099494,50013.666239283,49884.356325123,49680.034624784,49406.91821557,49257.95096525,48963.904247035,48795.544974084,48553.556519398,48423.970166926,48314.028902155,48148.000885604,48040.160288522,47834.982223924,47777.727023903,47764.762102474,47635.731913466,47625.728833337,47493.809088939,47470.555338338,47309.81896141,47199.838618191,47127.230349002,47040.675671553,46966.084194998,46861.272325405,46820.115356752,46745.202391862,46667.7812279,46650.20484772])

y = np.array([0.875474604,1.604929225,2.310366964,2.994241675,3.67143449,4.347777247,5.025130463,5.700624776,6.368964934,7.03499101,7.691415675,8.355130585,9.009934553,9.665336132,10.318718378,10.971264537,11.626437553,12.280633839,12.928241547,13.577265716,14.219534508,14.857967989,15.495924457,16.133685486,16.770187871,17.409440859,18.035947617,18.660278138,19.28315076,19.900208298])

x, y = np.meshgrid(x, y)

ax = fig.add_subplot(2, 2, 2, projection='3d')

surf2= ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True, label="Normal")


# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

plt.xlabel(u"Iteración", fontsize=7)
plt.ylabel(u"Tiempo", fontsize=7)
#plt.zlabel(u"Fitness")
ax.set_title(u'Estrategia swhd', fontsize=10)

# Add a color bar which maps values to colors.
#fig.colorbar(surf2, shrink=0.5, aspect=5)


#otra swnormal

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])

z= np.array([49954.833381454,49751.937994207,49478.659134516,49221.064357717,49104.512202248,48899.41575679,48767.488683454,48521.713653449,48373.953544404,48299.096838085,48101.843332291,47995.854177614,47890.254586108,47814.901202769,47634.349486571,47526.03116858,47458.749879155,47359.09968123,47219.147402328,47163.495361342,47092.57636698,47062.278662843,46999.221055629,46875.097358961,46806.870571059,46749.844272171,46641.632024921,46568.06633635,46537.031699148,46562.632996106])

y = np.array([0.867280269,1.594461155,2.293405135,2.978545094,3.655440927,4.326392229,4.987880262,5.661634421,6.327508752,6.981545472,7.638641238,8.292847188,8.942204054,9.593217214,10.236341755,10.87607309,11.513718303,12.148191833,12.788613701,13.424940077,14.055662839,14.684391936,15.321881485,15.954342635,16.585939153,17.213361883,17.831052876,18.456987524,19.084166741,19.702422651
])

x, y = np.meshgrid(x, y)

ax = fig.add_subplot(2, 2, 3, projection='3d')

surf2= ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True, label="Normal")


# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

plt.xlabel(u"Iteración", fontsize=7)
plt.ylabel(u"Tiempo", fontsize=7)
#plt.zlabel(u"Fitness")
ax.set_title(u'Estrategia sw normal', fontsize=10)


# Add a color bar which maps values to colors.
#fig.colorbar(surf2, shrink=0.5, aspect=5)

#otra evolutivo

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])

z = np.array([50763.829811134,50543.079813158,50221.702522952,49875.950629256,49616.772060834,49330.385828649,49039.810746947,48876.405688387,48717.148795322,48575.486012891,48382.834057344,48260.393122566,48081.349115012,48041.873852556,47922.134701925,47776.415063718,47742.455228134,47688.076845059,47632.829460754,47553.95268767,47520.742080411,47376.363180209,47219.356896368,47130.616259164,47103.110801522,47051.939059827,47018.889138189,46973.968261149,46989.762232209,46907.619144352])

y = np.array([1.333340963,2.262228131,3.173418061,4.067361474,4.954650911,5.858661135,6.738193528,7.595133567,8.451873231,9.323827942,10.233239063,11.151278885,12.049511925,12.942774073,13.833431403,14.720268051,15.583170199,16.451081522,17.361472607,18.272282084,19.201979574,20.150329932,21.045348255,21.943119097,22.837072984,23.728200285,24.652571909,25.571162264,26.470484972,27.389137824])

x, y = np.meshgrid(x, y)

ax = fig.add_subplot(2, 2, 4, projection='3d')

surf2= ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True, label="Normal")


# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

plt.xlabel(u"Iteración", fontsize=7)
plt.ylabel(u"Tiempo", fontsize=7)
#plt.zlabel(u"Fitness")
ax.set_title(u'Estrategia evolutiva', fontsize=10)

# Add a color bar which maps values to colors.
#fig.colorbar(surf2, shrink=0.5, aspect=5)

plt.savefig("color.png")