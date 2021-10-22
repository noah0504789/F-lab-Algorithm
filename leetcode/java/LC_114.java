//출처 : https://velog.io/@youn_22/leetcode-114.-Flatten-Binary-Tree-to-Linked-List
class Solution_114 {

    public void flatten(TreeNode root) {
        TreeNode head=root;
        TreeNode prev;
        while (head!=null){
            if(head.left!=null){
                prev=head.left;
                while (prev.right!=null){
                    prev=prev.right;
                }
                prev.right=head.right;
                head.right=head.left;
                head.left=null;

            }
            head=head.right;
        }
    }



}