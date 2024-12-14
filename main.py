class Disk:
    def __init__(self, name: str, type: str, size: float, free_space: float):
        """
        Инициализация объекта Disk.

        :param name: Название диска
        :param type: Тип диска (например, HDD или SSD)
        :param size: Общий размер диска (в ГБ)
        :param free_space: Свободное пространство на диске (в ГБ)

        :raises TypeError: Если атрибуты имеют неправильный тип.
        :raises ValueError: Если size меньше или равно 0, free_space меньше 0 или больше чем size.
        """
        if not isinstance(name, str):
            raise TypeError("Атрибут name должен быть строкой")
        
        if not isinstance(type, str):
            raise TypeError("Атрибут type должен быть строкой")
        
        if not isinstance(size, (int, float)):
            raise TypeError("Атрибут size должен быть float или int)")
        if size <= 0:
            raise ValueError("Атрибут size должен быть больше 0")
        
        if not isinstance(free_space, (int, float)):
            raise TypeError("Атрибут free_space должен быть float или int)")
        if free_space < 0:
            raise ValueError("Атрибут free_space не может быть отрицательным")
        if free_space > size:
            raise ValueError("Свободное пространство не может быть больше общего размера диска")

        self.name = name
        self.type = type
        self.size = size
        self.free_space = free_space
        self.employed_space = size - free_space

    def take_the_disk_space(self, space_will_be_busy: float) -> None:
        """
        Занимает пространство на диске.

        :param space_will_be_busy: Количество занимаемого пространства (в ГБ)
        :raises ValueError: Если space_will_be_busy больше свободного пространства на диске.
        
        >>> disk = Disk('D', 'HDD', 1000, 1000)
        >>> disk.take_the_disk_space(50)
        >>> disk.free_space
        950
        >>> disk.employed_space
        50
        """
        if space_will_be_busy > self.free_space:
            raise ValueError("Мало пространства на диске")
        
        self.free_space -= space_will_be_busy
        self.employed_space += space_will_be_busy

    def free_the_disk_space(self, space_will_be_released: float) -> None:
        """
        Освобождает пространство на диске.

        :param space_will_be_released: Количество освобождаемого пространства
        
        >>> disk = Disk('D', 'HDD', 1000, 950)
        >>> disk.free_the_disk_space(50)
        >>> disk.free_space
        1000
        >>> disk.employed_space
        0
        """
        ...

    def format_the_disk(self) -> None:
        """
        Форматирует диск, освобождая всё пространство.

        >>> disk = Disk('D', 'HDD', 1000, 500)
        >>> disk.format_the_disk()
        >>> disk.free_space
        1000
        >>> disk.employed_space
        0
        """
        self.free_space = self.size
        self.employed_space = 0


class Directory:
    def __init__(self, name: str, path: str, size: float):
        """
        Инициализация объекта Directory.

        :param name: Название директории
        :param path: Путь к директории
        :param size: Размер директории (в ГБ)
        """
        if not isinstance(name, str):
            raise TypeError("Атрибут name должен быть строкой")
        if not isinstance(path, str):
            raise TypeError("Атрибут path должен быть строкой")
        if not isinstance(size, (int, float)):
            raise TypeError("Атрибут size должен быть float или int")

        self.name = name
        self.path = path
        self.size = size

    def rename_directory(self, new_name: str) -> None:
        """
        Переименовывает директорию.

        :param new_name: Новое имя директории
        """
        self.name = new_name
    
    def information_about_directorr(self) -> None:
        """
        Выводит информацию о директории.
        """
        print(self.__dict__)

    def show_path_directory(self) -> None:
        """
        Выводит полный путь к директории.
        """
         
        print(self.path + self.name)


class File:
    def __init__(self, name: str, size: float, directory: Directory):
        """
        Инициализация объекта File.

        :param name: Название файла
        :param size: Размер файла (в ГБ)
        :param directory: Директория, в которой находится файл
        """
        if not isinstance(name, str):
            raise TypeError("Атрибут name должен быть строкой")
        if not isinstance(size, (int, float)):
            raise TypeError("Атрибут size должен быть числом (float или int)")
        if size <= 0:
            raise ValueError("Размер файла должен быть больше 0")
        
        self.name = name
        self.size = size
        self.directory = directory

    def move_file(self, new_directory: Directory) -> None:
        """
        Перемещает файл в новую директорию.

        :param new_directory: Новая директория для файла
        """
        ...

    def information_file(self) -> None:
        """
        Выводит информацию о файле.
        """
        print(self.__dict__)


if __name__ == "__main__":
    D_disk = Disk('D', 'HDD', 1000, 1000)
    D_disk.take_the_disk_space(50)
    print(D_disk.__dict__)

    first_my_directory = Directory('first', '~/home/', 50)
    first_my_directory.information_about_directorr()
    first_my_directory.show_path_directory()

    file_1 = File('file_1', 20, first_my_directory)
    file_1.information_file()