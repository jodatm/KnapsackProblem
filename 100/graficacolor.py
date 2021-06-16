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
z = np.array([8911.484764521,8775.513431707,8681.520712393,8563.648407768,8435.052979518,8363.544536275,8289.990035873,8210.111338934,8105.746049133,8043.867714732,7979.228800085,7933.628737955,7849.70195459,7772.676145024,7724.75848878,7703.081154159,7650.756537074,7576.748540633,7535.270260865,7496.583183246,7448.243491093,7395.06683274,7341.450980023,7316.702997475,7281.275197725,7246.462063932,7185.43093595,7149.410639772,7102.498377049,7079.480263972])

#Tiempo
y = np.array([0.248452218,0.4716893,0.686718313,0.897217822,1.105355,1.312520337,1.516336393,1.718773135,1.91948092,2.118610915,2.316887212,2.51321675,2.710002828,2.903754322,3.095811129,3.286377215,3.476419862,3.667125416,3.858092086,4.04673388,4.232594903,4.415935691,4.599215802,4.781310773,4.96271174,5.144249908,5.322151796,5.498279691,5.673645496,5.848653817])
x, y = np.meshgrid(x, y)

fig = plt.figure()

ax = fig.add_subplot(2, 2, 1, projection='3d')


surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True, label="SWHD")
                       
#fig.colorbar(surf, shrink=0.5, aspect=5)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.set_title(u'Estrategias swbest', fontsize=8)
plt.xlabel(u"Iteración", fontsize=7)
plt.ylabel(u"Tiempo", fontsize=7)
#Caso 

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])


z = np.array([9314.400993301,9236.964115984,9178.28402694,9080.208247945,8959.511938781,8893.549836874,8820.350110748,8772.348360099,8732.092232721,8671.099037512,8612.115131368,8571.018584029,8545.209654184,8479.727145314,8401.88553599,8366.653297037,8332.188303146,8285.219742805,8263.551544555,8213.900674604,8155.156158423,8126.480389744,8100.35042824,8074.461744265,8023.770297938,8005.645200599,7962.355320031,7932.627739514,7901.119425538,7864.848924436])

y = np.array([0.14399995,0.263428386,0.37555426,0.485670288,0.595202708,0.702169323,0.808831978,0.91495525,1.02053264,1.124762781,1.229593809,1.334215522,1.438860536,1.54320511,1.646859225,1.751225877,1.85388279,1.955095522,2.056510981,2.157442999,2.25749836,2.356669513,2.455610418,2.554100545,2.652788115,2.751015091,2.849271592,2.947832068,3.045962429,3.143980678])

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
ax.set_title(u'Estrategia swhd', fontsize=8)

# Add a color bar which maps values to colors.
#fig.colorbar(surf2, shrink=0.5, aspect=5)


#otra swnormal

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])

y = np.array([0.138932761,0.256983892,0.368029118,0.474846204,0.581335211,1,0.793398245,0.896587118,1.000524672,1.104261486,1.207543604,1.310498134,1.412244399,1.513323434,1.615240113,1.716838813,1.816616559,1.916261665,2.015146534,2.11413854,2.213583597,2.3121545,2.410859712,2.509173965,2.606267834,2.703442375,2.799987022,2.897634459,2.994348772,3.090436069])

z = np.array([8989.42836738,8904.692001051,8853.759444934,8747.048899314,8645.716434624,8577.262606745,8519.203945489,8451.142380541,8392.477185129,8311.015963732,8235.445403691,8206.164022921,8170.41465385,8105.89470386,8052.235937963,8034.172673314,8007.952261613,7947.061303626,7910.310307207,7872.250578762,7827.729956938,7793.542768468,7753.552263334,7734.712857055,7716.680326719,7679.045753751,7639.246924786,7620.185694623,7576.286629071,7576.70513572])

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
ax.set_title(u'Estrategia sw normal', fontsize=8)


# Add a color bar which maps values to colors.
#fig.colorbar(surf2, shrink=0.5, aspect=5)

#otra evolutivo

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])

y = np.array([0.262891531,0.448068706,0.632804759,0.817409039,1.001602594,1,1,1.556995614,1.741418616,1.926625713,2.112937586,2.297848026,2.481059345,2.666455038,2.851912562,3.039510107,3.225686733,3.410396194,3.5966151,3.780901066,3.967866103,4.152364127,4.338212689,4.52443378,4.709081682,4.893538117,5.077975853,5.263253355,5.447639441,5.634706227])

z = np.array([8864.325099682,8737.820188322,8557.705513147,8446.207466346,8295.330779957,8240,8176,8140.987999861,8047.323849833,7957.777045909,7892.463791073,7833.661250127,7760.115452048,7710.413877113,7693.211082795,7651.78344398,7606.334524703,7545.222271326,7541.37663259,7503.679695597,7455.57658294,7425.36842422,7387.38945929,7316.008273579,7313.043116688,7301.939836409,7287.26295295,7246.127774384,7248.683048764,7206.095276853
])

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
ax.set_title(u'Estrategia evolutiva', fontsize=8)

# Add a color bar which maps values to colors.
#fig.colorbar(surf2, shrink=0.5, aspect=5)

plt.savefig("color.png")
