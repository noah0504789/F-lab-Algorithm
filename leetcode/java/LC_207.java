//출처:https://daehopark.tistory.com/entry/Leetcode-207-Course-Schedule
class Solution_207 {

    public boolean canFinish(int numCourses, int[][] prerequisites) {
				
        int[] topology = new int[numCourses];  //위상 저장 배열
        List<List<Integer>> graph = new ArrayList<>();
        for (int i=0; i<numCourses; i++) { //prerequisites 정렬용 List 생성
            graph.add(new ArrayList<>());
        }

        for (int[] prerequisite : prerequisites) { //선수강이 필요한 과목이 있으면 위상 증가
            int x = prerequisite[0];
            int y = prerequisite[1];
            topology[x]++;
            graph.get(y).add(x); //list 에 prerequisites 값 넣음 (인덱스가 과목, 해당 인덱스의 리스트가 선수강과목)
        }

        int count = 0;
        while (count < numCourses) { //과목 수만큼 반복
            boolean courseTaken = false;
            for (int i = 0; i < numCourses; i++) { //topology 배열을 돌면서
                if (topology[i] == 0) { //위상이 0인 과목 수강 (선수강강의가 없는과목)
                    List<Integer> list = graph.get(i); //해당과목의 선수강이 필요한 과목을 찾아 
                    for (Integer x : list) {
                        topology[x]--; //위상을 1씩 감소
                    }

                    topology[i]--; //-1로 만들어 중복 탐색 제거
                    courseTaken = true;
                    count++; //과목 수만큼 반복
                }
            }
            if (!courseTaken) break; //더이상 들을 수 있는 선수강과목이 없는 과목이 없으면 탈출
        }

        return count == numCourses;
    }
}