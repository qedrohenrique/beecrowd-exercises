public boolean isPalindrome(int x) {
    	char[] arr = String.valueOf(x).toCharArray();
    	int half = arr.length / 2;
    	for(int i = 0; i < half; i++) {
    		if(arr[i] != arr[arr.length - i - 1]) return false;
    	}
        return true;
}

//

public boolean isPalindrome(int x) {
    	if (x == 0) return true;
      if ( x < 0 || x % 10 == 0) return false;
      
      int reversed = 0;
      while(x > reversed){
        int pop = x % 10;
        x /= 10;
        reversed = (reversed * 10) + pop;
      }
      
      if(x == reversed || x == reversed / 10) return true;
      else return false;
}
