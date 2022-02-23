    public static int lengthOfLongestSubstring(String s) {
    	int start = 0, end = 0, max = 0;
    	HashSet<Character> hashSet = new HashSet<>();
    	
    	while(end < s.length()) {
    		if(hashSet.contains(s.charAt(end))) {
    			hashSet.remove(s.charAt(start));
    			start++;
    		}else {
    			hashSet.add(s.charAt(end));
    			end++;
    			max = Math.max(hashSet.size(), max);
    		}
    	}
    	return max;
    }
