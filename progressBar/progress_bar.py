"""Module describing the classes associated with the progress bar"""


class ProgressBar:
    """Simple iterator of progress status bar."""

    def __init__(self, total: int) -> None:
        """Initialization of ProgressBar object"""
        self.__value = 0
        self.__total = total

    @property
    def value(self) -> int:
        """Returns the property __value

        Returns:
            int: property of the value
        """
        return self.__value

    @value.setter
    def value(self, value: int):
        """Setter for __value property

        Args:
            value (int): value to be set

        Raises:
            ValueError: If value is smaller of 0 or greater of __total property
        """
        if value <= self.total:
            self.__value = value
        else:
            raise ValueError(f'Value must be between 0 and {self.total}')

    @property
    def total(self):
        """Value of property __total"""
        return self.__total

    def __iter__(self):
        """ Initialization of iterator"""
        self.__value = 0
        return self

    def __next__(self) -> int:
        """ Method next"""
        if self.__value <= self.__total:
            value = self.__value
            self.__value += 1
            return value

        raise StopIteration


class ProgressBarCLI(ProgressBar):
    """It's progress bar with print_bar method
    """

    def __init__(self, total: int, prefix: str, suffix: str, length: int) -> None:
        super().__init__(total)
        self.prefix = prefix
        self.suffix = suffix
        self.length = length

    def print_bar(self, end: str = '\r') -> str:
        """Print progress bar method in command line

        Args:
            end (str): end of line. Defaults to '\r'.

        Returns:
            str: progress bar
        """
        fill_char = '█'
        empty_char = '-'
        percent_value = self.value / self.total * 100
        filled_length = self.length * self.value // self.total
        print( f'\r{self.prefix}'\
            f'|'\
            f'{fill_char * filled_length}{empty_char * (self.length - filled_length)}'\
            f'| {percent_value:.2f}% {self.suffix}', end=end)
