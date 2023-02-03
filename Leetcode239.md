#### Leetcode 239 [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) 
O(n) runtime O(n) space
```java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        PriorityQueue<Integer> p =new PriorityQueue<>(Collections.reverseOrder());
        int[] ans = new int[n-k+1];

        int ans_i=0;
        for(int i = 0 ; i < n; i++){
            p.add(nums[i]);
            if(p.size() == k){
                ans[ans_i] = Math.max(Integer.MIN_VALUE, p.peek());
                p.remove(nums[ans_i++]);
            }
        }

        return ans;
        
    }
}
```
###### Java Queue的基本操作
```java
//initialization of PriorityQueue
PriorityQueue<Integer> p =new PriorityQueue<>();
PriorityQueue<Integer> p =new PriorityQueue<>(Collections.reverseOrder()); //from min to max

// add
p.add()

//remove
p.remove()

//fetch the top
p.peek()

//size
p.size()

//check if empty
p.empty()

//add remove element
//offer poll peek
```
