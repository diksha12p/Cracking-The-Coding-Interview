class Animal(object):
    def __init__(self, name=None, type=None):
        self.name = name
        self.type = type
        self.timestamp = 0
        self.next = None


class AnimalShelter(object):
    def __init__(self):
        self.cat_head = None
        self.cat_tail = None
        self.dog_head = None
        self.dog_tail = None
        self.order = 0

    def enqueue(self, animal_name, animal_type):
        self.order += 1
        new_animal = Animal(animal_name, animal_type)
        new_animal.timestamp = self.order

        if new_animal.type == 'cat':
            if not self.cat_head:
                self.cat_head = new_animal
            if self.cat_tail:
                self.cat_tail.next = new_animal
            self.cat_tail = new_animal

        if new_animal.type == 'dog':
            if not self.dog_head:
                self.dog_head = new_animal
            if self.dog_tail:
                self.dog_tail.next = new_animal
            self.dog_tail = new_animal

    def deque_cat(self):
        if self.cat_head:
            new_animal = self.cat_head
            self.cat_head = new_animal.next
            return str(new_animal.name)
        else:
            raise Exception('No cat left!')

    def deque_dog(self):
        if self.dog_head:
            new_animal = self.dog_head
            self.dog_head = new_animal.next
            return str(new_animal.name)
        else:
            raise Exception('No dog left!')

    def deque_any(self):
        if self.cat_head and not self.dog_head:
            return self.deque_cat()
        elif self.dog_head and not self.cat_head:
            return self.deque_dog()
        elif self.cat_head:
            if self.cat_head.timestamp < self.dog_head.timestamp:
                return self.deque_cat()
            else:
                return self.deque_dog()
        else:
            raise Exception('No animal left!')


if __name__ == "__main__":
    AS = AnimalShelter()
    AS.enqueue('mia', 'cat')
    AS.enqueue('tommy', 'dog')
    AS.enqueue('lisa', 'cat')
    AS.enqueue('bruno', 'dog')
    AS.enqueue('brando', 'dog')
    AS.enqueue('molly', 'cat')

    print("\nSelect a cat")
    print(AS.deque_cat())
    print("\nSelect a dog")
    print(AS.deque_dog())
    print("\nSelect any animal")
    print(AS.deque_any())


