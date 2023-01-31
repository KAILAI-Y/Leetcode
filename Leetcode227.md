#### Leetcode 227 [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) 
O(n) runtime O(n) space
```java
class Solution {
    public int calculate(String str) {
        String s = str.replaceAll("\\s", "");
        int n = s.length();

        Stack<Integer> stack = new Stack<>();
        char op = '+';
        int top = 0;
        int result = 0;

        // test case: 3+2*2
        int i = 0;
        while (i < n){
            if(Character.isDigit(s.charAt(i))){
                int num = Character.getNumericValue(s.charAt(i)); //3
                while(i< n-1 && Character.isDigit(s.charAt(i+1))){ //test case: 42
                    i++;
                    num = 10 * num + Character.getNumericValue(s.charAt(i));
                }
                if(op == '+'){
                    stack.push(num); //[3] [3, 2]
                }else if(op == '-'){
                    stack.push(-num);
                }else if(op == '*'){ 
                    top = stack.pop();
                    stack.push(top*num); //[4]
                }else if(op == '/'){
                    top = stack.pop();
                    stack.push(top/num);
                }
            }else if(s.charAt(i) == '+' || s.charAt(i) == '-' || s.charAt(i) == '*'|| s.charAt(i) == '/'){
                op = s.charAt(i); //+ ,*
            }
            i++;
        }

        while(!stack.empty()){ // [3,4]
            result += stack.pop();
        }

        return result;
        
    }
}
```
