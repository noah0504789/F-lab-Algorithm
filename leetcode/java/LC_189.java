//출처:https://withhamit.tistory.com/452
public class Solution_189 {
    public void rotate(int[] nums, int start, int end) {
        int tmp;

        while (start < end) {
            tmp = nums[start];
            nums[start++] = nums[end];
            nums[end--] = tmp;
        }
    }

    public void rotate(int[] nums, int k) {
        int size = nums.length;
        
        if (size == 0) return;
        k %= size;

        rotate(nums, 0, size - 1);
        rotate(nums, 0, k - 1);
        rotate(nums, k, size - 1);
    }
}