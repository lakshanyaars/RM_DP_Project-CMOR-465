Single-Leg Revenue Management Dynamic Programming Tool
-------------------------------------------------------

Author: Lakshanyaa Rajkumar Sudhakar
Course: Revenue Management
Instructor: Dr. Darius

Project Description
-------------------
This tool implements a single-leg (single-resource) revenue management 
model using dynamic programming. The program computes the optimal value 
function and bid prices for capacity control decisions under stochastic 
demand.

The model follows the Bellman recursion framework discussed in lecture 
(slides on single-resource dynamic programming and bid prices).

Inputs
------
• Total capacity (number of seats)
• Time horizon (number of periods)
• Number of fare classes
• Fare values
• Arrival probabilities

Output
------
• Value function table V(t,x)
• Bid price table (marginal seat values)
• Maximum expected revenue
• Interpretation guidelines

How to Run
----------
1. Open terminal in this folder.
2. Run:

   python rm_dp_tool.py

3. Follow the prompts to enter parameters.

Interpretation
--------------
Accept a request if fare ≥ bid price.
Bid prices represent the marginal value of capacity.