#### Leetcode 1047 [Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/)
```java
class Solution {
    public String removeDuplicates(String s) {
        String result = new String("");
        Stack<Character> stack = new Stack<Character>();
        for(int i = 0; i < s.length(); i++){
            if(stack.empty() || s.charAt(i) !=  stack.peek()){ // empty or not equal -> push
                stack.push(s.charAt(i)); 
            }else if(!stack.empty() && s.charAt(i) ==  stack.peek()){   //if the new one = last one -> pop          
                stack.pop(); 
            }
        }

        int size = stack.size(); // store size
        if(size == 0){ // all removed -> return result = "" directly
            return result;
        }else{
            for(int i = 0; i < size; i++){
            result = stack.pop() + result;
            }
        }

        return result;
    }
}
```

