class Solution_56 {
    public int[][] merge(int[][] intervals) {
        int[][] output =new int[intervals.length][2];
        int outputLength=0;

        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return Integer.compare(o1[0], o2[0]);
            }
        });
        output[0][0]=intervals[0][0];
        output[0][1]=intervals[0][1];
        outputLength++;

        for (int i = 1; i < intervals.length; i++) {
            boolean overlapFlag=false;
            for (int j = 0; j < outputLength; j++) {

                if((output[j][0]<=intervals[i][0] && output[j][1]>=intervals[i][0]) && output[j][1]<intervals[i][1] ){ //앞글자가 속하고 뒷글자가 범뮈확장
                    output[j][1]=intervals[i][1];
                    overlapFlag=true;
                    break;
                } else if (output[j][0]>intervals[i][0] && (output[j][1]>=intervals[i][1] && output[j][0]<=intervals[i][1])){ // 뒷글자가 속하고 앞글자가 범위확장
                    output[j][0]=intervals[i][0];
                    overlapFlag=true;
                    break;
                } else if( output[j][0]>=intervals[i][0] && output[j][1]<=intervals[i][1]){ //모든게 intervals 가 더 클경우
                    output[j][1]=intervals[i][1];
                    output[j][0]=intervals[i][0];
                    overlapFlag=true;
                    break;
                }
                else if(output[j][0]<=intervals[i][0] && output[j][1]>=intervals[i][1]) { //모든게 output 보다 작을경우
                    overlapFlag=true;
                    break;
                }
            }
            if(!overlapFlag){
                output[outputLength][0]=intervals[i][0];
                output[outputLength][1]=intervals[i][1];
                outputLength++;
            }
        }

        return Arrays.copyOf(output,outputLength);
    }
}
