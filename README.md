# Analysing-Density-of-Primes-along-Polynomials
A Python tool that quantifies the density of prime numbers in quadratic sequences (an^2 + bn + c) and compares them against the theoretical baseline derived from the Prime Number Theorem.

##  Key Features

* **Polynomial Streaming:** Uses Python generators to stream values efficiently ($O(1)$ space complexity), allowing for deep searches without memory overhead.
* **6k ± 1 Optimization:** Implements a deterministic primality test that skips multiples of 2 and 3, reducing the search space by ~66% compared to naive trial division.
* **Statistical Comparison:** Automatically benchmarks the "richness" of the polynomial against the asymptotic average density of primes (1/ln(x)).
* **Performance Metrics:** Tracks execution time and total items processed to measure algorithmic efficiency.

##  Requirements

* NumPy
* SciPy
