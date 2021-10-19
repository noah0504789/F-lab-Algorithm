class Solution {
    public int numTrees(int n) {
        int []dp=new int[20];
        
        dp[0]=1;
        dp[1]=1;
        for (int nodes = 2; nodes <n+1 ; nodes++) {
            int total=0;
            for (int root = 1; root <nodes+1 ; root++) {
                int left=root-1;
                int right=nodes-root;
                total+=dp[left]*dp[right];
            }
            dp[nodes]=total;
        }
        return dp[n];
    }
}