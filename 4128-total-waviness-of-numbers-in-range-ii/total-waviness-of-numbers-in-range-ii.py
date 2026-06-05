from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def get_total_waviness(limit: int) -> int:
            if limit < 100:
                return 0
            
            s = str(limit)
            n = len(s)
            
            @lru_cache(None)
            def dp(idx, tight, is_started, last, sec_last):
                # Base case: completed building the number
                if idx == n:
                    return 1, 0  # (valid numbers formed, accumulated waviness)
                
                max_digit = int(s[idx]) if tight else 9
                res_count = 0
                res_wave = 0
                
                for d in range(max_digit + 1):
                    next_tight = tight and (d == max_digit)
                    
                    if not is_started:
                        if d == 0:
                            # Still processing leading zeros
                            cnt, wave = dp(idx + 1, next_tight, False, -1, -1)
                            res_count += cnt
                            res_wave += wave
                        else:
                            # Placing the first valid non-zero digit
                            cnt, wave = dp(idx + 1, next_tight, True, d, -1)
                            res_count += cnt
                            res_wave += wave
                    else:
                        # We have a valid preceding context
                        is_wave = 0
                        if sec_last != -1:
                            # Check if 'last' is a peak or valley relative to 'sec_last' and 'd'
                            if (sec_last < last > d) or (sec_last > last < d):
                                is_wave = 1
                        
                        cnt, wave = dp(idx + 1, next_tight, True, d, last)
                        res_count += cnt
                        # Total waviness contributed by branches below + current wave point * valid combinations
                        res_wave += wave + is_wave * cnt
                        
                return res_count, res_wave
            
            return dp(0, True, False, -1, -1)[1]
            
        return get_total_waviness(num2) - get_total_waviness(num1 - 1)