#### Leetcode 347 [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
O(Nlogk) runtime O(n+k) space 
```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) { //[4,1,-1,2,-1,2,3]
        //initialize hashmap key:value -> num: frequency
        Map<Integer, Integer> count = new HashMap();
        for(int n: nums){
            count.put(n, count.getOrDefault(n, 0)+1); 
        } //{-1:2,1:1,2:2,3:1,4:1}

        //initialize priorityqueue 如果它的“计数”值较小，那么它应该在队列中较早出现（优先级较高）。
        //count.get(n1) - count.get(n2) < 0 -> n1, n2; >0 -> n2, n1
        Queue<Integer> heap = new PriorityQueue<>((n1, n2) -> count.get(n1) - count.get(n2));
        for(int n: count.keySet()){
            heap.add(n);
            if(heap.size() > k) heap.poll();
        }
        //[2, -1]

        int[] res = new int[k];
        for(int i = 0; i < k; i++){
            res[i] = heap.poll();
        }
        return res; //[2, -1]
        
    }
}
```

```java
// {-1:2,1:1,2:2,3:1,4:1}
map.getOrDefault(n, 0); //如果map中存在n，则返回对应value，否则返回0
map.getOrDefault(3, 0); //1
map.getOrDefault(5, 0); //0
map.keySet(); //[-1, 1, 2, 3, 4]

// 如果它的“计数”值较小，那么它应该在队列中较早出现（优先级较高）。
//count.get(n1) - count.get(n2) < 0 -> n1, n2; >0 -> n2, n1
Queue<Integer> heap = new PriorityQueue<>((n1, n2) -> count.get(n1) - count.get(n2));
```
