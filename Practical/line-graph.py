import matplotlib.pyplot as plt


def plot_dynamic_graph():
    # write your code here...
    n = input("Enter the number of data points (N): ")
    x = list(map(int, input(f"Enter {n} space-separated values for Study Hours (X-axis): ").split()))
    y = list(map(int, input(f"Enter {n} space-separated values for Marks Obtained (Y-axis): ").split()))

    print("Data Points:", n)
    print("X-Data (Hours Studied):", x)
    print("Y-Data (Marks Obtained):", y)
    print("Plotting 'Student Performance Analysis'...")

    plt.plot(x, y, color="blue", linestyle="-", marker="s", label="Performance Data")
    plt.title("Student Performance Analysis")
    plt.xlabel("Hours Studied")
    plt.ylabel("Marks (0-100)")
    print("Plot generation complete")

    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    plot_dynamic_graph()