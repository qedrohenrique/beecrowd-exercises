class MedianOfTwoSortedArrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    	
    	if(nums1.length == 0) {
    		if(nums2.length % 2 == 0) {
    			return (nums2[nums2.length/2-1] + nums2[nums2.length/2])/2.0;
    		}else {
    			return nums2[nums2.length/2];
    		}
    	}
    	
    	if(nums2.length == 0) {
    		if(nums1.length % 2 == 0) {
    			return (nums1[nums1.length/2-1] + nums1[nums1.length/2])/2.0;
    		}else {
    			return nums1[nums1.length/2];
    		}
    	}
        
    	if(nums1.length > nums2.length) {
    		int[] temp = nums1;
    		nums1 = nums2;
    		nums2 = temp;
    	}
    	
    	int low = 0;
    	int high = nums1.length;
    	
    	while (low <= high) {
    		int partitionA = (low + high) / 2;
    		int partitionB = ((nums1.length + nums2.length + 1) / 2) - partitionA;
    		
    		int leftA, rightA, leftB, rightB;
    		leftA = immediatelyToLeft(nums1, partitionA);
    		rightA = immediatelyToRight(nums1, partitionA);
    		leftB = immediatelyToLeft(nums2, partitionB);
    		rightB = immediatelyToRight(nums2, partitionB);
    				
    		if(leftA <= rightB && leftB <= rightA) {
    			if((nums1.length + nums2.length) % 2 == 0) 
    				return (Math.max(leftA, leftB) + Math.min(rightA, rightB)) / 2.0;
    			else
    				return Math.max(leftA, leftB);
    		}
    		
    		if(leftA > rightB) {
    			high = partitionA - 1;
    		}else {
    			low = partitionA + 1;
    		}
    	}
    	
    	return -1;
    }
    
    private int immediatelyToLeft(int[] nums, int partition) {
    	if(partition == 0) {
    		return Integer.MIN_VALUE;
    	}else {
    		return nums[partition - 1];
    	}
    }
    
    private int immediatelyToRight(int[] nums, int partition) {
    	if(partition == nums.length) {
    		return Integer.MAX_VALUE;
    	}else {
    		return nums[partition];
    	}
    }
}
