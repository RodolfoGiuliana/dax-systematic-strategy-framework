# DAX Monte Carlo Simulation Results

This repository showcases the outcomes of Monte Carlo simulations applied to the DAX index. Only the final results are shared as images (PNG), without exposing the underlying data or scripts.

## Methodology

- Monte Carlo simulations were run to model potential DAX index paths.
- Random sampling techniques were used to simulate multiple trajectories.
- The results are visualized as charts showing projected index behavior and volatility.

## Images

All the simulation charts are stored in the `images/` folder.

-  Example of a single simulation path.
-  Distribution of multiple simulation outcomes.
-  Additional charts demonstrating variations.

## Notes

- Data used for these simulations is confidential and not included.
- This repository is for visualization and demonstration purposes only.

- #Data

Index(['<DATE>', '<BALANCE>', '<EQUITY>', '<DEPOSIT LOAD>'], dtype='object')
             <DATE>  <BALANCE>  <EQUITY>  <DEPOSIT LOAD>
0  2024.12.14 00:00   50000.00  50000.00          0.0000
1  2024.12.17 11:21   48938.75  50047.50         25.6702
2  2024.12.17 13:06   48938.75  48860.00          0.0000
3  2024.12.17 14:45   48938.75  48938.75          0.0000
4  2024.12.18 08:00   49176.65  48911.91          0.0000


Number of observations: 1043
Mean return: 0.000747
Std return: 0.013104


Monte Carlo Final Equity Statistics:
5th percentile:  51757.43
Median:         98054.47
95th percentile:197122.70
Probability of Ruin (-30%): 4.70%
Monte Carlo Drawdown Statistics:
5th percentile:  -40012.40
Median:         -21182.25
95th percentile:-13460.38

               <DATE>  <EQUITY>   returns
0 2024-12-17 11:21:00  50047.50  0.000950
1 2024-12-17 13:06:00  48860.00 -0.023727
2 2024-12-17 14:45:00  48938.75  0.001612
3 2024-12-18 08:00:00  48911.91 -0.000548
4 2024-12-18 08:04:00  49387.71  0.009728
1038   -0.001063
1039   -0.001310
1040   -0.001365
1041   -0.000883
1042   -0.000883
Name: returns, dtype: float64



