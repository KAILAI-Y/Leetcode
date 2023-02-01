#### Leetcode 739 [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/description/)
O(n) runtime O(n) space 
```java
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        //initialize stack, res
        Stack<Integer> stack = new Stack<>();
        int[] res = new int[temperatures.length];


        for(int i = 0; i <temperatures.length; i++){
            int curTemp = temperatures[i];
            while(!stack.empty() && temperatures[stack.peek()] < curTemp){
                int prevIndex = stack.pop();
                res[prevIndex] = i-prevIndex;
            }
            //store index
            stack.push(i); 
        }
        return res;        
    }
}
```

