class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
         Map<String,List<String>> map=new HashMap<>();
        for (String str : strs) {
            char[] charArray=str.toCharArray();
            Arrays.sort(charArray);
            String sortedString=new String(charArray);
            if(map.containsKey(sortedString)){
                List<String> stringList=map.get(sortedString);
                stringList.add(str);
                map.replace(sortedString,stringList);
            }
            else{
                List<String> stringList=new ArrayList<>();
                stringList.add(str);
                map.put(sortedString,stringList);
            }

        }
        
        return new ArrayList<>(map.values());
    }
}