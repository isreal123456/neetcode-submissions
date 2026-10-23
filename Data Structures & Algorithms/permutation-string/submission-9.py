class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen_hit = {}
        second_str = {}
        for ch in s1 :
            if ch in seen_hit:
                seen_hit[ch] += 1
            else :
                seen_hit[ch] = 1
        
        # i take each length of str1 possibliites into str2 right?
        first_pointer = 0
        second_pointer = len(s1) - 1
        real_boolean_value = False
        checker = {}
        lengthy = len(s2) - 1
        current_substring = s2[first_pointer:second_pointer + 1]
        for ch in current_substring :
            if ch in checker :
                checker[ch] += 1
            else :
                checker[ch] = 1

        #sliding window logic
        while second_pointer <= lengthy:
            # we have the two lists
            boolean_value = True
            for key in checker.keys() :
                if not key in seen_hit :
                    boolean_value = False
                    break
                if checker[key] != seen_hit[key] :
                    boolean_value = False
            if boolean_value :
                return True
            #update checker list
            # remove my first_pointer_value, which is
            checker[s2[first_pointer]] -= 1
            if checker[s2[first_pointer]] == 0:
                del checker[s2[first_pointer]]
                
            # iterate throguh my pointer stuff
            first_pointer += 1
            second_pointer += 1

            if second_pointer <= lengthy :
                if s2[second_pointer] in checker :
                    checker[s2[second_pointer]] += 1
                else :
                    checker[s2[second_pointer]] = 1
        return False