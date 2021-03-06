class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        s=''
        words.sort(key=len,reverse=True)
        for i in range(len(words)):
            if words[i]+'#' in s:
                continue
            else:
                s=s+words[i]+'#'
        return len(s)  