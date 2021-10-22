//출처 https://velog.io/@ujone/Leetcode-138.-Copy-List-with-Random-Pointer-JAVA
class Solution_138 {
    public Node copyRandomList(Node head) {

        Map< Node,Node> map=new HashMap<>(); //<원래 노드, 카피한 노드> 맵핑용 해시맵 인스턴스

        Node ret=new Node(-1);
        Node copy_node=ret;
        Node node=head;

        while (node!=null){
            if(!map.containsKey(node)) //현재 노드가 맵에 없을경우 맵에 저장,카피노드 생성
                map.put(node,new Node(node.val));

            copy_node.next=map.get(node);
            copy_node=copy_node.next;

            if(node.random!=null){ //현재 노드의 랜덤포인트가 있을경우
                if(!map.containsKey(node.random)) map.put(node.random,new Node(node.random.val)); //랜덤이 가리키는 노드가 맵에 없으면 맵에 저장 ,카피노드 생성

                copy_node.random=map.get(node.random); //카피노드에도 랜덤포인터 저장.
            }
            node=node.next;
        }
        return ret.next;
    }
}
