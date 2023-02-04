###### Java stack的基本操作
```java
//initialization of Stack
Stack<Character> stack = new Stack<Character>();

// add
stack.push()

//remove the last
stack.pop()

//fetch the top
stack.peek()
//stack.lastElement()

//size
stack.size()

//check if empty
stack.empty()
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
```

###### Java Queue的基本操作
```java
//initialization of PriorityQueue
PriorityQueue<Integer> p =new PriorityQueue<>();
PriorityQueue<Integer> p =new PriorityQueue<>(Collections.reverseOrder()); //from min to max
// 如果它的“计数”值较小，那么它应该在队列中较早出现（优先级较高）。
//count.get(n1) - count.get(n2) < 0 -> n1, n2; >0 -> n2, n1
Queue<Integer> heap = new PriorityQueue<>((n1, n2) -> count.get(n1) - count.get(n2));

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


###### Java hashmap的基本操作
```java
//key:value
HashMap<Integer, Integer> map = new HashMap<>();

map.put(key, value);

map.get(key);

// {-1:2,1:1,2:2,3:1,4:1}
map.getOrDefault(n, 0); //如果map中存在n，则返回对应value，否则返回0
map.getOrDefault(3, 0); //1
map.getOrDefault(5, 0); //0

map.keySet(); //[-1, 1, 2, 3, 4]
```
