// O(n^2)

    public static int[] twoSum(int[] nums, int target) {
        for(int i = 0; i < nums.length; i++) {
        	for(int j = i; j < nums.length; j++) {
        		if(nums[i] + nums[j] == target) return new int[] {i,j};
        	}
        }
        throw new IllegalArgumentException("No solution");
    }

// O(nlogn)

    public static int[] twoSum(int[] nums, int target) {
        Arrays.sort(nums);
        for (int i = 0, l = nums.length; i < l; i++) {
            int j = Arrays.binarySearch(nums, i + 1, l, target-nums[i]);
            if (j > i) return new int[]{i, j};
        }
        return null;
    }

// O(n)

    public static int[] twoSum(int[] nums, int target) {
        HashMap hashmap = new HashMap();
        for(int i = 0; i < nums.length; i ++){
            int complement = target - nums[i];
            if(hashmap.containsKey(complement)) {
            	return new int[] {(int) hashmap.get(complement), i};
            }
            hashmap.put(nums[i], i);
        }
        throw new IllegalArgumentException("No solution");
    }
