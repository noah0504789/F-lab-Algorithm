class Solution_78 {
    public List<List<Integer>> subsets(int[] nums) {

        List<List<Integer>> output=new ArrayList<>();
        output.add(new ArrayList<>());
        List<Integer> numsList=new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            numsList.add(nums[i]);
        }
        recursion(output,new ArrayList<>(),numsList);
        return output;

    }
    void recursion (List<List<Integer>> output,List<Integer> powerSet, List<Integer>nums){
        for (int i = 0; i < nums.size(); i++) {
            List<Integer> powerSetCopy=new ArrayList<>(powerSet);
            powerSetCopy.add(nums.get(i));
            Collections.sort(powerSetCopy);
            if(!output.contains(powerSetCopy)){ //이미 저장된것과 중복된 값이 있으면 재귀하지 않음
                output.add(powerSetCopy);
                List<Integer> numsCopy=new ArrayList<>(nums);
                numsCopy.remove(i);
                recursion(output,powerSetCopy,numsCopy);
            }
        }
    }
}