class Solution {
    List<List<Integer>> output;
    
        {
            output=new ArrayList<>();
        }
        public List<List<Integer>> permute(int[] nums) {
    
            if(nums.length==1){
                List<Integer> new_list=new ArrayList<>();
                new_list.add(nums[0]);
                output.add(new_list);
                return output;
            }
    
    
            List<Integer> numList=new ArrayList<>();
            for (int num : nums) {
                numList.add(num);
            }
            recursion(new ArrayList<Integer>(),numList);
            return output;
        }
        
        void recursion(List<Integer> list,List<Integer> numList){
            if(numList.size()==1){
                list.add(numList.get(0));
                output.add(list);
                return;
            }
    
            for (int i = 0; i < numList.size(); i++) {
                List<Integer> new_numList=new ArrayList<>(numList);
                new_numList.remove(i);
                List<Integer> new_list=new ArrayList<>(list);
                new_list.add(numList.get(i));
                recursion(new_list,new_numList);
            }
        }
    }