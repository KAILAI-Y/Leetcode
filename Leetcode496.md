#### Leetcode 496 [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/description/) 
```java
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int n1 = nums1.length;
        int n2 = nums2.length;
        int[] result = new int[n1];

        for(int i = 0; i < n1;i++){
           for(int j = 0; j < n2; j++){
                //find nums1[i] in nums2
               if(nums2[j] == nums1[i]){
                   for(int k = j; k < n2; k++){
                    //find the next greater num in nums2
                       if(nums2[k] > nums2[j]){
                           result[i] = nums2[k];
                           break;
                        }else{
                            result[i] = -1;
                        }
                   }
                }
           }
        }
        return result;     
    }
}
```
单调栈 + 哈希表
O(m+n) runtime O(n) space
```java
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        //initialize stack, result, hashmap
        Stack<Integer> stack = new Stack<>();
        int[] res = new int[nums1.length]; // [0, 0, 0]
        HashMap<Integer, Integer> map = new HashMap<>(); //nums: next greater

        //nums1 = [4,1,2], nums2 = [1,3,4,2]
        for(int i = nums2.length - 1; i >= 0; --i){
            int num = nums2[i]; //i:4->2 i:3->4 i:2->3 i:1->1
            while(!stack.empty() && num >= stack.peek()){ // i:3-> 4>2
                stack.pop(); //i:3 ->[]
            }
            map.put(num, stack.isEmpty() ? -1 : stack.peek()); //{2:-1, 4:-1, 3:4, 1:3}
            stack.push(num); //i:4 ->[2] i:3->[4] i:2->[4, 3] i:1->[4, 3, 1]
        }

        for(int i = 0; i < res.length; i++){
            res[i] = map.get(nums1[i]); //[-1, 0, 0] [-1, 3, 0] [-1, 3, -1]
        }
        return res;      
    }
}
```
###### Java hashmap的基本操作
```java
//key:value
HashMap<Integer, Integer> map = new HashMap<>();

map.put(key, value);

map.get(key);
```

###### 单调递增
```java
public int[] monotoneIncreasingStack(int[] nums){
    Stack<Integer> stack = new Stack<>();
    for(int i = 0; i < nums.length; i++){
        int num = nums[i];
        while(!stack.empty && num >= stack.peek()){
            stack.pop();
        }
        stack.push(num);
    }
}
```

###### 单调递减
```java
public int[] monotoneIncreasingStack(int[] nums){
    Stack<Integer> stack = new Stack<>();
    for(int i = 0; i < nums.length; i++){
        int num = nums[i];
        while(!stack.empty && num <= stack.peek()){
            stack.pop();
        }
        stack.push(num);
    }
}

