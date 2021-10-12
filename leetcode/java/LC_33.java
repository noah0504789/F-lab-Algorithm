 public int search(int[] nums, int target) {
        int result=0;
        int l = 0;
        int r = nums.length - 1;

        //피봇찾기
        while (l < r) {
            int p = (int) Math.floor(((double)l+ r) / 2);
            if (nums[p] > nums[r]) {
                l = p + 1;
            } else {
                r = p;
            }
        }


        int pivot=l;
        l=0;
        r=nums.length-1;


        if(l==pivot){
           l=0;
        }
        else if(target<nums[l]){
            l=pivot;
        }
        else if (target>nums[l]){
            r=pivot-1;
        }

        if(target==nums[l]){
            return l;
        }

        while (true){
            int t=(int) Math.floor(((double)l + r) / 2);
            if(l>r){
                result=-1;
                break;
            }
            else if (target==nums[t]){
                result= t;
                break;
            }
            else if((r==l)&&nums[r]!=target){
                result=-1;
                break;
            }
            else if (target<nums[t]) {
                r = t;
            } else if(target>nums[t]) {
                l = t+1;
            }

        }
       return result;
    }