class Solution_39 {
    int[] candidates;
    List<List<Integer>> result;
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        this.candidates=candidates;
        result=new ArrayList<>();
        recursion(new ArrayList<>(),target,0);
        return result;
    }

    void recursion(List<Integer> list, int num,int candi_ind){

        for (int i =candi_ind ; i <candidates.length ; i++) {
            //List<Integer> new_list=list;
            List<Integer> new_list=new ArrayList<>(list);
            if(num-candidates[i]==0){
                new_list.add(candidates[i]);
                result.add(new_list);
                return;
            }
            else if(num-candidates[i]>0){
                new_list.add(candidates[i]);
                recursion(new_list,num-candidates[i],i);
            }

        }
    }
}
