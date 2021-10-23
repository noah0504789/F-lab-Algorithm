//출처 : https://www.youtube.com/watch?v=SPKJz8oPJo4&list=PL2mzT_U4XxDl8PP-jMk4rt6BPzBtS__pQ&index=33
public class Solution_142 {
    public ListNode detectCycle(ListNode head) {
        ListNode walker=head;
        ListNode runner=head;
        while (runner!=null){ //루프가 없을경우 탈출
            runner = runner.next;
            if(runner!=null){
                runner=runner.next; //러너는 달리는 사람이라 두번 움직임
                walker=walker.next;
                if(walker==runner){
                    break;
                }
            }
            else { //runner가 null일경우 루프가 없으므로 탈출
                break;
            }
        }

        if(runner==null) // 루프가 없는경우 최종 null 반환
            return null;

        ListNode check = head;
        while (check!=walker){
            check=check.next;
            walker=walker.next;
        }
        return check;
    }
}