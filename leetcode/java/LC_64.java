class Solution_64 {
    public int minPathSum(int[][] grid) {
        int[][] mem= new int[grid.length][grid[0].length];

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j <grid[0].length ; j++) {
                if(i==0&&j==0)
                    mem[i][j]=grid[i][j];
                else if(i>0 && j>0)
                    mem[i][j]=Math.min(mem[i][j-1],mem[i-1][j])+grid[i][j];
                else if(i==0)
                    mem[i][j]=mem[i][j-1]+grid[i][j];
                else
                    mem[i][j]=mem[i-1][j]+grid[i][j];
            }

        }
        return mem[grid.length-1][grid[0].length-1];
    }
}