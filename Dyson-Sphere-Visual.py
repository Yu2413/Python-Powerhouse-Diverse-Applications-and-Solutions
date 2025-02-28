import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def create_dyson_sphere(num_panels=100, resolution=50):
    # Create sphere surface (representing the Dyson sphere)
    phi = np.linspace(0, np.pi, resolution)
    theta = np.linspace(0, 2 * np.pi, resolution)
    phi, theta = np.meshgrid(phi, theta)
    r = 1  # Radius of the sphere

    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the sphere surface with a semi-transparent color
    ax.plot_surface(x, y, z, color='orange', alpha=0.3, edgecolor='none')

    # Create random panels on the sphere surface
    # Generate random angles to simulate the placement of panels
    panel_phi = np.random.uniform(0, np.pi, num_panels)
    panel_theta = np.random.uniform(0, 2 * np.pi, num_panels)
    panel_x = r * np.sin(panel_phi) * np.cos(panel_theta)
    panel_y = r * np.sin(panel_phi) * np.sin(panel_theta)
    panel_z = r * np.cos(panel_phi)

    # Plot the panels as blue dots
    ax.scatter(panel_x, panel_y, panel_z, color='blue', s=50)

    # Set equal aspect ratio for all axes
    ax.set_box_aspect([1, 1, 1])
    ax.set_title("Dyson Sphere Visualization")
    plt.show()

if __name__ == "__main__":
    create_dyson_sphere()
