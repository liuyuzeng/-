from DBDynamics import Ant
import time

# 电机最大值
i = 9
cont = 3
max1 = 50000 * 14
m = Ant('com3')  # or COM2 COM3
# for i in range(1, cont):
m.setPowerOn(i)
m.setPowerOn(i) 

# Start Homing


# for i in range(1, cont):
m.setHomingLevel(i, 1)
m.setHomingLevel(i, 1)
m.setHomingDirection(i, -1)
m.setHomingDirection(i, -1)
m.waitTargetPositionReached(i)
m.waitTargetPositionReached(i)
m.setHomingMode(i)
m.setHomingMode(i)
time.sleep(15)
m.setTargetPosition(i, max1)
# print("home done!")
# while True:
#     for i in range(1, 4):
#         for n in range(1, cont):
#             m.setTargetVelocity(n, 100)
#             m.setAccTime(n, 500)
#             m.setTargetPosition(n, max1)
#             m.setTargetPosition(n, max1)
#             m.setTargetPosition(n, max1)
#         time.sleep(7)
#         print("Point A Reached!")
#         # Move to Point B
#         for n in range(1, cont):
#             m.setTargetVelocity(n, 100)
#             m.setAccTime(n, 500)
#             m.setTargetPosition(n, 50000*4)
#             m.setTargetPosition(n, 50000*4)
#             m.setTargetPosition(n, 50000*4)
#         time.sleep(7)
#         print("Point B Reached!")
#     for i in range(1, 2):
#         for n in range(1, cont):
#             m.setTargetVelocity(n, 150)
#             m.setAccTime(n, 1000)
#             m.setTargetPosition(n, 50000 * 14)
#             m.setTargetPosition(n, 50000 * 14)
#             m.setTargetPosition(n - 4, 0)
#             m.setTargetPosition(n - 4, 0)
#             m.setTargetPosition(n - 8, 50000 * 14)
#             m.setTargetPosition(n - 8, 50000 * 14)
#             m.setTargetPosition(n - 12, 0)
#             m.setTargetPosition(n - 12, 0)
#             m.setTargetPosition(n - 16, 50000 * 14)
#             m.setTargetPosition(n - 16, 50000 * 14)
#             m.setTargetPosition(n - 20, 0)
#             m.setTargetPosition(n - 20, 0)
#             m.setTargetPosition(n - 24, 50000 * 14)
#             m.setTargetPosition(n - 24, 50000 * 14)
#             m.setTargetPosition(n - 28, 0)
#             m.setTargetPosition(n - 28, 0)
#             m.setTargetPosition(n - 32, 50000 * 14)
#             m.setTargetPosition(n - 32, 50000 * 14)
#             m.setTargetPosition(n - 36, 0)
#             m.setTargetPosition(n - 36, 0)
#             m.setTargetPosition(n - 40, 50000 * 14)
#             m.setTargetPosition(n - 40, 50000 * 14)
#             m.setTargetPosition(n - 44, 0)
#             m.setTargetPosition(n - 44, 0)
#             m.setTargetPosition(n - 48, 50000 * 14)
#             m.setTargetPosition(n - 48, 50000 * 14)
#             m.setTargetPosition(n - 52, 0)
#             m.setTargetPosition(n - 52, 0)
#             m.setTargetPosition(n - 56, 50000 * 14)
#             m.setTargetPosition(n - 56, 50000 * 14)
#             time.sleep(1.2)
#     time.sleep(10)
#     for i in range(1, 4):
#         for n in range(1, cont):
#             m.setTargetVelocity(n, 100)
#             m.setAccTime(n, 500)
#             if n % 2 == 0:
#                 m.setTargetPosition(n, max1)
#                 m.setTargetPosition(n, max1)
#                 m.setTargetPosition(n, max1)
#                 m.setTargetPosition(n, max1)
#             else:
#                 m.setTargetPosition(n, 50000*4)
#                 m.setTargetPosition(n, 50000*4)
#                 m.setTargetPosition(n, 50000 * 4)
#                 m.setTargetPosition(n, 50000 * 4 )

#         time.sleep(7)
#         for n in range(1, cont):
#             m.setTargetVelocity(n, 100)
#             m.setAccTime(n, 500)
#             if n % 2 == 0:
#                 m.setTargetPosition(n, 50000*4)
#                 m.setTargetPosition(n, 50000*4)
#                 m.setTargetPosition(n, 50000 * 4)
#                 m.setTargetPosition(n, 50000 * 4)
#             else:
#                 m.setTargetPosition(n, max1)
#                 m.setTargetPosition(n, max1)
#                 m.setTargetPosition(n, max1)
#                 m.setTargetPosition(n, max1)
#         time.sleep(7)
#     for n in range(1, cont):
#         m.setTargetVelocity(n, 100)
#         m.setAccTime(n, 500)
#         m.setTargetPosition(n, 50000 * 9)
#         m.setTargetPosition(n, 50000 * 9)
#         m.setTargetPosition(n, 50000 * 9)
#     time.sleep(7)
#     for n in range(1, cont):
#         m.setTargetVelocity(n, 100)
#         m.setAccTime(n, 500)
#         m.setTargetPosition(12, 50000 * 14)
#         m.setTargetPosition(1, 0)
#         m.setTargetPosition(2, 50000 * 1.4)
#         m.setTargetPosition(3, 50000 * 2.8)
#         m.setTargetPosition(4, 50000 * 4.2)
#         m.setTargetPosition(5, 50000 * 5.6)
#         m.setTargetPosition(6, 50000 * 7)
#         m.setTargetPosition(7, 50000 * 8.4)
#         m.setTargetPosition(8, 50000 * 9.8)
#         m.setTargetPosition(9, 50000 * 11)
#         m.setTargetPosition(10, 50000 * 12.4)
#         m.setTargetPosition(11, 50000 * 13.8)
#     time.sleep(7)
#     for n in range(1, cont):
#         m.setTargetVelocity(n, 100)
#         m.setAccTime(n, 500)
#         m.setTargetPosition(12, 0)
#         m.setTargetPosition(1, 14)
#         m.setTargetPosition(2, 50000 * 13.8)
#         m.setTargetPosition(3, 50000 * 12.4)
#         m.setTargetPosition(4, 50000 * 11)
#         m.setTargetPosition(5, 50000 * 9.8)
#         m.setTargetPosition(6, 50000 * 8.4)
#         m.setTargetPosition(7, 50000 * 7)
#         m.setTargetPosition(8, 50000 * 5.6)
#         m.setTargetPosition(9, 50000 * 4.2)
#         m.setTargetPosition(10, 50000 * 2.8)
#         m.setTargetPosition(11, 50000 * 1.4)
#     time.sleep(7)