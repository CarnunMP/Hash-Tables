# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    # TODO: STRETCH
    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # if there's nothing at the index
        i = self._hash_mod(key)
        if self.storage[i] == None:
            # insert a new LinkedPair pointing to NULL
            self.storage[i] = LinkedPair(key, value)
        # else,
        else:
            # insert a new LinkedPair at the end of the linked list present
            last_in_list = self.storage[i]
            while last_in_list.next != None:
                last_in_list = last_in_list.next

            last_in_list.next = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # get the list associated with the hashed key
        i = self._hash_mod(key)
        linked_list = self.storage[i]

        # search the list for the key
        list_element = linked_list
        prev_element = None
        while list_element != None:
            # if it's found, delete it (remove pointer to it)
            if list_element.key == key:
                # If it's the 1st in the list, make the 2nd the new first
                if prev_element == None:
                    self.storage[i] = list_element.next
                # else point the previous to its .next
                else:
                    prev_element.next = list_element.next

                return

            prev_element = list_element
            list_element = list_element.next
    
        # if not, print warning
        print("Invalid key.")



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # get the list associated with the key
        i = self._hash_mod(key)
        linked_list = self.storage[i]

        # search the list for the key
        while linked_list != None:
            # if it's found, return its value
            if linked_list.key == key:
                return linked_list.value

            linked_list = linked_list.next
        
        # else, return None
        return


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
