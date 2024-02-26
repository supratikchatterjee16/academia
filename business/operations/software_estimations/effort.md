# Effort Estimation

## Types

1. Parametric Technique(Mathematical parameters based techniques)
    - Productivity based : effort estimation through pre-base-lined productivity or project delivery rate derived on past data
    - COCOMO : Effort estimation through Constructive Cost Model regression equation derived on past data
2. Heuristic(Experience and Discussion based technique)
    - Work Breakdown Structure(Bottom Up) : Effort estimation through requirements decomposition into granular work packages and summing up the effort
    - Expert Judgement : Effort estimation based on expert experience and agreement
    - Monte Carlo Simulation : Effort estimation through statistical model requiring considerable amount of data
    - Estimation by Analogy : Effort estimation by experienced professionals based on similar projects executed in the past

### Example formula to calculate effort using COCOMO and PERT

For development/testing projects COCOMO uses :

Total Schedule(in months) = $ y * \sqrt{PY}$

PY is number of Person Years  
Value of Y is :
    - 2.5 - 3 for <= 180 person months
    - 2 - 2.5 for > 180 person months

PERT Schedule Estimation formula is :

Schedule = $(O + 4M + P) / 6$

where,
O = Optimistic Schedule  
M = Most Likely Schedule
P = Pessimistic Schedule

