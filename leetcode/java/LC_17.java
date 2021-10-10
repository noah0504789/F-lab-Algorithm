class Solution {
    String digits;
    List<String> result=new ArrayList<>();

    String[] letters=new String[10];
    public  List<String> letterCombinations(String digits) {
        char start='a';
        this.digits=digits;

        //키패드 문자 저장
        for (int i = 2; i <=9; i++) {
            for (int j = 0; j < 4; j++) {
                if(i!=7&&i!=9&&j==3)
                    continue;
                if(letters[i]==null){
                    letters[i]=String.valueOf(start);}
                else
                    letters[i] = letters[i] + start;
                start++;
            }
        }
         if(!digits.equals(""))
            recursion("",0);
        return result;
    }

    public void recursion(String s,int ind){
        if(digits.length()==ind){
            result.add(s);
        }
        else {
            int digit=digits.charAt(ind)-'0';
            for (int i = 0; i < letters[digit].length(); i++) {
                recursion(s + letters[digit].charAt(i), ind + 1);
            }
        }

    }
}