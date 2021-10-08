//11. Container With Most Water

public static int maxArea(int[] height) {
    int result=0,left=0,right=height.length-1;
    while (right-left>0){
        result =Math.max(result,(right-left)*Math.min(height[right],height[left]));

        if(height[right]<=height[left])
            right--;
        else
            left++;
    }
    return result;
}