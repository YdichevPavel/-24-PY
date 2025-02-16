class Person:
    """Класс описывает человека."""

    def __init__(self, name: str, age: int, growth: float) -> None:
        """Инициализация объекта Person.
        
        Args:
            name (str): Имя человека.
            age (int): Возраст человека.
            growth (float): Рост человека.
        """
        if not isinstance(name, str):
            raise TypeError("name должно быть строкой")
        if not isinstance(age, int):
            raise TypeError("age должно быть целочисленным")
        if age > 120 or age < 0:
            raise ValueError("Введите реальный возраст")
        if not isinstance(growth, (int, float)):
            raise TypeError("growth должно быть целочисленным числом или с плавающей запятой")
        
        self.name = name
        self.age = age
        self.growth = growth

    def get_name(self) -> str:
        """Возвращает имя человека."""
        return self.name
    
    def get_age(self) -> int:
        """Возвращает возраст человека."""
        return self.age
    
    def get_growth(self) -> float:
        """Возвращает рост человека."""
        return self.growth
    
    def set_growth(self, new_growth: float) -> None:
        """Устанавливает новый рост"""
        if not isinstance(new_growth, (int, float)) or new_growth <= 0:
            raise ValueError("Рост должен быть положительным числом")
        self.growth = new_growth
    
    def change_name(self, new_name: str) -> None:
        """Меняет имя человека."""
        if not isinstance(new_name, str):
            raise TypeError("Имя должно быть строкой")
        self.name = new_name
    
    def __repr__(self) -> str:
        """Возвращает строковое представление объекта для отладки."""
        return f"Person(name={self.name!r}, age={self.age}, growth={self.growth})"

    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        return f"Гражданин {self.name}, {self.age} лет, рост {self.growth}"
    

class Child(Person):
    """Класс описывает ребенка, у которого должен быть опекун."""

    def __init__(self, name: str, age: int, growth: float, guardian: Person) -> None:
        """Инициализация объекта Child.
        
        Args:
            name (str): Имя ребенка.
            age (int): Возраст ребенка.
            growth (float): Рост ребенка.
            guardian (Person): Опекун ребенка.
        """
        super().__init__(name, age, growth)
        if not isinstance(guardian, Person):
            raise TypeError("guardian должен быть экземпляром класса Person")
        if not isinstance(age, int):
            raise TypeError("age должен быть int")
        if age > 18:
            raise ValueError("Гражданин совершенолетний, воспользуйтесь клссом Person")
        
        self.age = age
        self.guardian = guardian

    def get_guardian(self) -> Person:
        """Возвращает опекуна ребенка."""
        return self.guardian
    
    def get_name(self) -> str:
        """Возвращает имя ребенка с указанием опекуна.

        Метод переопределён, чтобы дополнительно указывать опекуна ребенка.
        Это позволяет различать объекты `Child`, а также учитывать особенности детей, 
        находящихся под опекой.
        """        
        
        return f"{self.name} подопечный {self.guardian.name}"
    
    def set_guardian(self, new_guardian: Person) -> None:
        """Устанавливает нового опекуна.
        
        Args:
            new_guardian (Person): Новый опекун.
        """
        if not isinstance(new_guardian, Person):
            raise TypeError("new_guardian должен быть экземпляром класса Person")
        self.guardian = new_guardian

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта для отладки."""
        return f"Child(name={self.name!r}, age={self.age}, growth={self.growth}, guardian={self.guardian!r})"

    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        return f"Ребенок {self.name}, {self.age} лет, рост {self.growth}, опекун: {self.guardian.name}"


if __name__ == "__main__":
    adult = Person(name="Иван", age=35, growth=180.5)
    print(adult)
    
    print(f"Имя: {adult.get_name()}")
    print(f"Возраст: {adult.get_age()}")
    print(f"Рост: {adult.get_growth()}")
    
    adult.change_name("Алексей")
    adult.set_growth(182.0)
    print(adult)
    
    child = Child(name="Маша", age=10, growth=140.3, guardian=adult)
    print(child)
    
    print(f"Имя ребенка: {child.get_name()}")
    print(f"Опекун: {child.get_guardian().get_name()}")
    
    new_guardian = Person(name="Ольга", age=40, growth=165.2)
    child.set_guardian(new_guardian)
    print(child)