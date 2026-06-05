class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # All possible prime numbers of set bits for numbers up to 10^6 (max 20 bits)
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        prime_bit_count = 0
        
        # Iterate through the inclusive range
        for num in range(left, right + 1):
            # num.bit_count() returns the number of 1 bits in the binary representation
            if num.bit_count() in primes:
                prime_bit_count += 1
                
        return prime_bit_count