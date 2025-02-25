from .linked_list_nodes import Node

class TwoPointerTechniques:
    def detect_cycle(self, head: Node):
        """
        Floyd's Cycle Detection Algorithm
        Returns True if cycle exists, False otherwise
        Args:
            head (_type_): _description_
       
        Pattern: Fast/Slow Pointers
        - slow moves 1 step at a time
        - fast moves 2 steps at a time
        - if they meet, cycle exists
        """

        if not head or not head.next:
            return False

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow==fast:
                return True

        return False

    def find_cyle_start(self, head:Node):
        """
        Finds and returns the node where cycle begins
        Returns None if no cycle exists
        
        Pattern: Combined Fast/Slow and Same-Speed Pointers
        Phase 1: Fast/Slow to find intersection
        Phase 2: Same-speed pointers to find cycle start
        """

        if not head or not head.next:
            return None

        # Phase 1: Fast/Slow pattern to find intersection
        slow = fast = head
        has_cycle = False

        while fast and fast.next:
            slow =slow.next
            fast = fast.next.next

            if slow == fast:
                has_cycle = True
                break

        if not has_cycle:
            return None

        # Phase 2: Same-speed pattern
        slow = head

        while slow !=fast:
            slow = slow.next
            fast = fast.next

        return slow

    def find_middle_node(self, head:Node):
        """
        Returns the middle node of the linked list
        For even length, returns the second middle node
        
        Pattern: Fast/Slow Pointers
        - When fast reaches end, slow is at middle
        - Fast moves twice as fast, so slow ends up in middle
        """

        if not head or not head.next:
            return head

        # Fast/Slow pointer initialization
        slow = fast = head

        while fast and fast.next:
            slow = slow.next        # 1 step
            fast = fast.next.next   # 2 steps 

        return slow


    def find_kth_from_end(self, head:Node, k):
        """
        Returns the kth node from the end
        
        Pattern: Leader/Follower
        - Leader starts k nodes ahead
        - Both move at same speed
        - When leader hits end, follower is at kth from end
        """
        if not head or k<= 0:
            return None

        # Leader/Follower pattern initialization
        leader = follower = head

        # Create k-node gap between pointers
        for _ in range(k):
            if not leader:
                return None

            leader = leader.next

        # Move both at same speed
        while leader:
            leader = leader.next
            follower = follower.next

        return follower

    def is_palindrome(self,head:Node):
        """
        Checks if linked list is palindrome
        
        Pattern: Combined Fast/Slow and Left/Right
        Phase 1: Fast/Slow to find middle while reversing first half
        Phase 2: Left/Right comparison of reversed first half with second half
        """
        if not head or not head.next:
            return True

        # Phase 1: Fast/Slow pattern to find middle
        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            # Reverse first half while finding middle
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Handle odd length - skip middle node
        if fast:
            slow = slow.next

        # Phase 2: Left/Right pattern for comparison
        left = prev         # First half (reversed)
        right = slow        # Second half

        while left and right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True


    def reorder_list(self, head:Node):
        """
        Reorders list to L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
        
        Pattern: Multiple Two-Pointer Patterns
        Phase 1: Fast/Slow to find middle
        Phase 2: Reverse second half
        Phase 3: Left/Right merge of two halves
        """
        if not head or not head.next:
            return

        # Phase 1: Fast/Slow pattern to find middle
        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # Split into two lists
        prev.next = None

        # Phase 2: Reverse second half using iteration
        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Phase 3: Left/Right pattern to merge lists
        left = head
        right = prev

        while right:
            next1 = left.next
            next2 = right.next
            left.next = right
            right.next = next1
            left = next1
            right = next2

    def reverse_between(self, head:Node, m, n):
        """
        Reverses linked list nodes between positions m and n
        
        Pattern: Left/Right with Fixed Window
        - Left pointer at position m
        - Right pointer moves through positions m to n
        - Reversal happens within this window
        """
        if not head or m==n:
            return head


        dummy = Node(0)
        dummy.next = head
        prev = dummy

        # Move to position m
        for _ in range(m-1):
            prev = prev.next

        # Reverse within window from m to n
        current = prev.next
        next_node = None

        for _ in range(n-m+1):
            temp = current.next
            current.next = next_node
            next_node = current
            current = temp

        # Connect reversed portion with rest of list
        prev.next.next = current
        prev.next = next_node

        return dummy.next