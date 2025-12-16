import numpy as np
import time
import math
from scipy import stats


def is_prime_optimized(n):
    """
    Determines if n is prime using the 6k +/- 1 optimization.
    All primes are of the from 6k +/- 1 so can utlise this to speed up checking of primes
    """
    # 1. Handle small edge cases efficiently
    if n <= 1: return False
    if n <= 3: return True
    
    # 2. Fast elimination of multiples of 2 and 3
    # This prevents entering the loop for 66% of integers.
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # 3. Trial Division with 6k steps
    # We only check factors of form 6k-1 and 6k+1.
    # We stop when i^2 > n because if n has a factor larger than sqrt(n),
    # it must also have a factor smaller than sqrt(n).
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True

def polynomial_stream(a, b, c, limit):
    """
    Generator that yields values of the quadratic polynomial P(n) = an^2 + bn + c.
    """
    for n in range(limit):
        # Calculate the value on the diagonal
        val = a * (n**2) + b * n + c
        
        # Ensure we are checking positive integers
        if val > 0:
            yield val


def find_density(a, b, c, search_limit):
    """
    Calculates the prime density of a quadratic path and compares it to 
    the asymptotic average 1/ln(x).
    """
    prime_count = 0
    total_count = 0
    
    # Benchmarking start
    t0 = time.time()
    
    # Stream the data (O(1) Space)
    stream = polynomial_stream(a, b, c, search_limit)
    
    for val in stream:
        total_count += 1
        
        # Use our optimized primality test
        if is_prime_optimized(val):
            prime_count += 1
            
    t1 = time.time()
    
    # --- Statistical Analysis ---
    
    # 1. Actual Density in this specific polynomial path
    actual_density = prime_count / total_count if total_count > 0 else 0
    
    # 2. Theoretical Average Density (Prime Number Theorem)
    # The average density of primes around x is 1/ln(x).
    # We take the average magnitude of numbers in our path to estimate this.
    avg_magnitude = a * (search_limit/2)**2  # Rough approximation of avg size
    theoretical_density = 1 / math.log(avg_magnitude) if avg_magnitude > 1 else 0
    
    ratio = actual_density / theoretical_density
    
    print(f"\n--- Results for P(n) = {a}n^2 + {b}n + {c} ---")
    print(f"Items Processed: {total_count:,}")
    print(f"Primes Found:    {prime_count:,}")
    print(f"Execution Time:  {t1 - t0:.4f} seconds")
    print(f"Actual Density:  {actual_density:.4f}")
    print(f"Market Avg (est):{theoretical_density:.4f}")
    print(f"Performance:     {ratio:.2f}x higher than average")
    
    return actual_density, ratio