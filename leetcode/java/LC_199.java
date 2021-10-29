class Solution_199 {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> out= new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        
        queue.add(root);
 
        while(!queue.isEmpty()){
            int size= queue.size();//큐의길이=한 레벨에 존재하는 노드개수
            
            for(int i = 0; i < size; i++){
                TreeNode cur = queue.poll();
                if(cur == null) break;
                
                if(i == size - 1) out.add(cur.val); //제일 오른쪽 노드
                //다음 레벨 노드를 큐로 넣음
                if(cur.left != null) queue.add(cur.left);
                if(cur.right != null) queue.add(cur.right);
            }
        }
        
        return out;
    }
}