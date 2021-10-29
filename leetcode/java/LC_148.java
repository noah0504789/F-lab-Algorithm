class Solution_148 {
    public ListNode sortList(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }

        List<Integer> list = new ArrayList<>();
        while(head != null){
            list.add(head.val);
            head = head.next;
        }

        Collections.sort(list, Collections.reverseOrder());

        ListNode out = new ListNode(list.get(0));
        for(int i=1; i< list.size(); i++){
            out = new ListNode(list.get(i), out);
        }

        return out;
    }
}