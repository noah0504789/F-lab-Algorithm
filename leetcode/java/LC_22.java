class Solution {
    public static int n;
    public static List<String> result;
    
    {
        result=new ArrayList();
    }
    
    public List<String> generateParenthesis(int n) {
        this.n=n;
        make(1,0,"(");
        return result;
    }
    public void make(int f_basket, int b_basket,String s){
        if(f_basket<b_basket)
            return;
        else if(f_basket>n||b_basket>n)
            return;
        else if(f_basket==b_basket&&f_basket==n){
            result.add(s);
            return;
            }
        else
        {
            make(f_basket+1,b_basket,s+"(");
            make(f_basket,b_basket+1,s+")");
        }
                   
    }
}