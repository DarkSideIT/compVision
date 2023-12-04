import cv2
import matplotlib.pyplot as plt
import numpy as np


class Circle:
    def __init__(self, x, y):
        self.cords = [(x, y)]

    def is_connected(self, new_cords, threshold=10):
        last_x, last_y = self.cords[-1]
        distance = ((new_cords[0] - last_x) ** 2 + (new_cords[1] - last_y) ** 2) ** 0.5
        return distance <= threshold

    def append(self, cords):
        self.cords.append(cords)

    def cords_trace(self):
        return list(zip(*self.cords))


def find_circle(file_path):
    img = np.load(file_path)
    circles, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return [(int(cv2.moments(circle)["m10"] / cv2.moments(circle)["m00"]),
             int(cv2.moments(circle)["m01"] / cv2.moments(circle)["m00"])) for circle in circles]


def process_circle(cords, circle):
    circle.append(cords)


files = [f'out/h_{i}.npy' for i in range(100)]
circle_list = [Circle(*cords) for cords in find_circle(files.pop(0))]

for file_path in files:
    current_circles = find_circle(file_path)

    for circle in circle_list:
        idx = 0
        threshold = 5

        while current_circles:
            idx = (idx + 1) % len(current_circles)
            threshold += 5

            if circle.is_connected(current_circles[idx], threshold):
                process_circle(current_circles.pop(idx), circle)

# Plotting
for circle in circle_list:
    x, y = circle.cords_trace()
    plt.plot(x, y)

plt.show()
