
Pseudocode
Backward Dynamic Programming Algorithm
INPUT:
    C  ← total capacity
    T  ← number of time periods
    J  ← number of fare classes
    f[j]  ← fare of class j
    p[j]  ← arrival probability of class j
    (with sum of p[j] ≤ 1)

INITIALIZATION:
    Create value function array V[t][x] for t = 0..T and x = 0..C
    Set V[0][x] = 0 for all x   (no time remaining → no future revenue)

BACKWARD RECURSION:
    For t = 1 to T:
        For x = 0 to C:

            If x = 0:
                V[t][0] = 0
                Continue to next capacity

            Compute expected value:

                expected_value = 0

                For each fare class j = 1..J:

                    Accept_Value  = f[j] + V[t-1][x-1]
                    Reject_Value  = V[t-1][x]

                    Best_Action_Value = max(Accept_Value, Reject_Value)

                    expected_value += p[j] * Best_Action_Value

                No_Arrival_Prob = 1 - sum_j p[j]
                expected_value += No_Arrival_Prob * V[t-1][x]

            Set V[t][x] = expected_value

OUTPUT:
    Value function table V[t][x]
Bid Price Computation
For each time t = 0..T:
    For each capacity x = 1..C:

        Bid_Price[t][x] = V[t][x] - V[t][x-1]

This represents the marginal value of one unit of capacity.

Booking Decision Rule
When a request of class j arrives at state (t, x):

    If f[j] ≥ Bid_Price[t][x]:
        Accept request
        Capacity reduces to x-1
    Else:
        Reject request
Forward Simulation Validation
Repeat N simulation runs:

    Set seats = C
    revenue = 0

    For t = T down to 1:

        Randomly generate arrival based on probabilities p[j]

        If a request of class j arrives AND seats > 0:

            If f[j] ≥ Bid_Price[t][seats]:
                Accept
                seats -= 1
                revenue += f[j]
            Else:
                Reject

    Record revenue

Compute average simulated revenue

Compare average revenue to V[T][C]

-------------------------------------------------------------------------------------------------------------------------------------------

Revenue Management Dynamic Programming Tool

Single-Leg Airline Revenue Management Model

Overview

This project implements a discrete-time, single-leg revenue management model using backward dynamic programming.

The tool computes:

The value function V(t, x)
Bid prices (marginal seat values)
Optimal accept/reject decisions
Visualizations of pricing dynamics
Forward Monte Carlo simulation validation

The objective is to determine the optimal booking control policy under stochastic demand and limited capacity.

Model Description
State Variables
x — remaining capacity (seats)
t — remaining time periods until departure
Decision Rule

When a booking request arrives:

Accept the request if:

fare ≥ bid price

Reject otherwise.

Bellman Recursion

The value function satisfies:

V(t, x) = E[ max{ f_j + V(t-1, x-1), V(t-1, x) } ]

where the expectation is taken over arrival probabilities.

Bid Price Definition

The bid price (marginal seat value) is defined as:

Bid(t, x) = V(t, x) − V(t, x-1)

This represents the opportunity cost of consuming one unit of capacity.

Inputs

The program prompts the user to enter:

Total capacity
Number of time periods
Number of fare classes
Fare for each class
Arrival probability for each class

Constraint:

The sum of arrival probabilities must be ≤ 1.

Outputs

The tool generates:

Value Function Table
Bid Price Table
Bid Price Heatmap
Bid Price Over Time (selected capacity)
Capacity Comparison Plot
Forward Monte Carlo Simulation Validation

The simulation verifies that average realized revenue converges to the DP expected value.

How to Run
Step 1: Navigate to the project folder
cd RM_DP_SingleLeg_Project
Step 2: Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

On Windows:

venv\Scripts\activate
Step 3: Install required packages
pip install -r requirements.txt
Step 4: Run the program
python rm_dp_tool.py

If python does not work, use:

python3 rm_dp_tool.py
Economic Interpretation
Lower remaining capacity leads to higher bid prices
Bid prices generally decline as departure approaches
Accept only when fare exceeds opportunity cost
Simulated revenue closely matches DP expected revenue

This aligns with classical airline revenue management theory.

Code Structure
single_leg_dp() — backward dynamic programming solver
simulate_policy() — forward simulation validation
run_model() — user interface and visualization
main() — menu system
Dependencies
numpy
pandas
matplotlib
Author

Lakshanyaa Rajkumar Sudhakar
CMOR 465 / INDE 565
Rice University
