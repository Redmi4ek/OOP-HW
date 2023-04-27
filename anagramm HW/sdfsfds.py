class Solvik:
    def anagrama(self, strs: list(str)) -> list(list(str)):
        anag = {}

        for word in strs:
            sorted_w = ''.join(sorted(word))
            if sorted_w in anag:
                anag[sorted_w].append(word)
            else:
                anag[sorted_w] = word

        return list(anag.values())
    
Solvik('rat', 'car')