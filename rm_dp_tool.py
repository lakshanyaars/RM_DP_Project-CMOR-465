import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.ion()


def single_leg_dp(capacity, T, fares, arrival_probs):

    num_classes = len(fares)

    V = np.zeros((T + 1, capacity + 1))
    policy = np.empty((T + 1, capacity + 1), dtype=object)

    for t in range(1, T + 1):
        for x in range(capacity + 1):

            expected_value = 0

            for j in range(num_classes):
                p = arrival_probs[j]
                f = fares[j]

                if x == 0:
                    accept_value = 0
                    reject_value = V[t - 1][x]
                else:
                    accept_value = f + V[t - 1][x - 1]
                    reject_value = V[t - 1][x]

                best_value = max(accept_value, reject_value)
                expected_value += p * best_value

            p_no_arrival = 1 - sum(arrival_probs)
            expected_value += p_no_arrival * V[t - 1][x]

            V[t][x] = expected_value

    bid_prices = np.zeros((T + 1, capacity + 1))

    for t in range(1, T + 1):
        for x in range(1, capacity + 1):
            bid_prices[t][x] = V[t - 1][x] - V[t - 1][x - 1]

    return V, bid_prices

import random

def simulate_policy(capacity, T, fares, arrival_probs, bid_prices, runs=1000):

    total_revenue = 0

    for _ in range(runs):

        seats = capacity
        revenue = 0

        for t in reversed(range(1, T + 1)):

            if seats == 0:
                break

            rand = random.random()

            cumulative_prob = 0
            arrival_class = None

            for j in range(len(fares)):
                cumulative_prob += arrival_probs[j]
                if rand <= cumulative_prob:
                    arrival_class = j
                    break

            if arrival_class is None:
                continue  # no arrival

            fare = fares[arrival_class]
            bid = bid_prices[t][seats]

            if fare >= bid:
                revenue += fare
                seats -= 1

        total_revenue += revenue

    return total_revenue / runs

def run_model():

    print("\n--- Single-Leg Revenue Management DP Tool ---\n")

    capacity = int(input("Enter total capacity (number of seats): "))
    T = int(input("Enter number of time periods: "))
    num_classes = int(input("Enter number of fare classes: "))

    fares = []
    arrival_probs = []

    for i in range(num_classes):
        f = float(input(f"Enter fare for class {i+1}: "))
        p = float(input(f"Enter arrival probability for class {i+1}: "))
        fares.append(f)
        arrival_probs.append(p)

    if sum(arrival_probs) > 1:
        print("\nError: Arrival probabilities cannot exceed 1.")
        return

    V, bid_prices = single_leg_dp(capacity, T, fares, arrival_probs)

    print("\n--- RESULTS ---\n")

    V_df = pd.DataFrame(V)
    bid_df = pd.DataFrame(bid_prices)

    print("Value Function V(t,x):")
    print(V_df.round(2))
    print("\nBid Prices (Marginal Seat Values):")
    print(bid_df.round(2))
    
    plt.figure(1)
    plt.imshow(bid_prices, cmap="Blues", aspect="auto")
    plt.colorbar(label="Bid Price")
    plt.title("Bid Price Heatmap")
    plt.xlabel("Capacity")
    plt.ylabel("Time")
    plt.show()

    avg_simulated_revenue = simulate_policy(
    capacity, T, fares, arrival_probs, bid_prices
)

    print("\n--- FORWARD SIMULATION ---")
    print("Average simulated revenue over 1000 runs:",
    round(avg_simulated_revenue, 2))

    # ---- Bid Price Over Time Plot ----

    plt.figure(2)

# Choose capacity level to visualize (e.g., full capacity)
    cap_to_plot = capacity

    time_axis = list(range(len(bid_prices)))[::-1]
    plt.plot(time_axis, bid_prices[:, cap_to_plot][::-1], marker='o')

    plt.title(f"Bid Price Over Time (Capacity = {cap_to_plot})")
    plt.xlabel("Time")
    plt.ylabel("Bid Price")
    plt.grid(True)

    plt.show()

    # ---- Capacity Comparison Plot ----

    plt.figure(3)

    for x in range(1, capacity + 1):
        plt.plot(range(len(bid_prices)), bid_prices[:, x], label=f"Capacity {x}")

    plt.title("Bid Price Over Time (All Capacity Levels)")
    plt.xlabel("Time")
    plt.ylabel("Bid Price")
    plt.legend()
    plt.grid(True)

    plt.show()

    print("\n--- INTERPRETATION ---")
    print("• Accept a request if fare ≥ bid price.")
    print("• Higher bid prices indicate greater scarcity of capacity.")
    print("• As time decreases, bid prices typically decline.")
    print("• As capacity decreases, bid prices typically increase.")
    print("\nMaximum expected revenue starting from full capacity:",
          round(V[T][capacity], 2))


def main():

    while True:
        print("\n==============================")
        print("Revenue Management DP Tool")
        print("==============================")
        print("1. Run new experiment")
        print("2. Exit")
        print("==============================")

        choice = input("Select option: ")

        if choice == "1":
            run_model()
        elif choice == "2":
            print("\nExiting tool. Goodbye.")
            break
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()