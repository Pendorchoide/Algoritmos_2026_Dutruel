from typing import Any

class Heap():
    def __init__(self):
        self.elements = []

    def add_element(self, value: Any) -> None:
        self.elements.append(value)
        self.float_element(self.size()-1)


    def delete_top_element(self) -> None:
        self.elements[0], self.elements[-1] = self.elements[-1], self.elements[0]
        value = self.elements.pop()
        self.sink_element(0)

    def size(self) -> int:
        return len(self.elements)

    def float_element(self, index) -> None:
        while index > 0 and (self.elements[index] > self.elements[(index - 1) // 2]):
            father = ((index - 1) // 2)
            self.elements[index], self.elements[father] = self.elements[father], self.elements[index]
            index = father

    def sink_element(self, index) -> None:
        left_child = (index * 2) + 1
        control = True
        while(control and left_child < self.size()):
            right_child = left_child + 1
            aux = left_child
            if (right_child < self.size()):
                if self.elements[right_child] > self.elements[left_child]:
                    aux = right_child

            if self.elements[index] < self.elements[aux]:
                self.elements[index], self.elements[aux] = self.elements[aux], self.elements[index] 
                index = aux
                left_child = (index * 2) + 1
            else:
                control = False

    def convert_to_heap(self)->None:
        for i in range(len(self.elements)):
            self.float_element(i)

    def heap_sort(self)->None:
        result = []
        while self.size() > 0:
            value = self.delete_top_element
            result.append(value)
        return result

    #Cola de Prioridad

    def arrive(self, )

    

monticulo = Heap()

monticulo.add_element(15)
print(monticulo.elements)

monticulo.add_element(5)
print(monticulo.elements)

monticulo.add_element(52)
print(monticulo.elements)

monticulo.add_element(26)
print(monticulo.elements)

monticulo.add_element(26)
print(monticulo.elements)

monticulo.add_element(99)
print(monticulo.elements)

monticulo.add_element(38)
print(monticulo.elements)

monticulo.add_element(9)
print(monticulo.elements)

monticulo.add_element(87)
print(monticulo.elements)



print(monticulo.elements)


monticulo.delete_top_element()
print("===========")
print(monticulo.elements)
