import matplotlib.pyplot as plt

cpus = [1,2,4,8]
reduce_time = [2.1141469478607178, 1.2097463607788086, 0.9153831005096436, 0.9085781574249268]
total_time = [6.131474018096924, 3.2272188663482666, 1.930466651916504, 1.9209980964660645]

# plt.plot(cpus, reduce_time, label = 'reduce time')
plt.plot(cpus, total_time, label = 'total time')
plt.legend()
plt.xlabel('Number of CPUs')
plt.ylabel('Time (s)')
plt.title('Total running time on different numbers of CPUs')
plt.show()