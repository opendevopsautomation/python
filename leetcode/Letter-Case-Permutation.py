class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def dfs(S,ans,i):
            if i==len(S):
                ans.append(S)
            elif S[i].isdigit():
                dfs(S,ans,i+1)
            else:
                S=S[:i]+S[i].lower()+S[i+1:]
                dfs(S,ans,i+1)
                S=S[:i]+S[i].upper()+S[i+1:]
                dfs(S,ans,i+1)
            return ans
        ans=[]
        if S.isnumeric() or len(S)==0:
            ans.append(S)
            return ans
        else:
            return dfs(S,ans,0)