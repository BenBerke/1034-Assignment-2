class Job:

    """
    A single job with attributes:
    name, category, rate, date, hours
    Ensures valid input types and
    0 < hour <= 6, 0 < rate
    """

    def __init__(self, name, category, rate, date, hours):
        if not isinstance(name, str):
            raise TypeError('name must be a string')
        if not isinstance(category, str):
            raise TypeError('category must be a string')
        if not isinstance(rate, float):
            raise TypeError('rate must be a float')
        if not isinstance(date, str):
            raise TypeError('date must be a string')
        if not isinstance(hours, int):
            raise TypeError('hours must be a int')

        if hours > 6:
            raise ValueError('Hours can not be greater than 6')
        if hours <= 0:
            raise ValueError('Hours must be positive')
        if rate <= 0:
            raise ValueError('Rate must be positive')

        self._name = name
        self._category = category
        self._rate = rate
        self._date = date
        self._hours = hours

    def get_name(self):
        return self._name

    def get_category(self):
        return self._category

    def get_rate(self):
        return self._rate

    def get_date(self):
        return self._date

    def get_hours(self):
        return self._hours

    def __eq__(self, other):
        if not isinstance(other, Job):
            return False
        return self._name == other._name and self._category == other._category and self._rate == other._rate and self._date == other._date and self._hours == other._hours

    def __hash__(self):
        return hash((self._name, self._category, self._rate, self._date, self._hours))

    def __str__(self):
        return f"Job({self._name} {self._category} {self._rate} {self._date} {self._hours})"

    def __repr__(self):
        return self.__str__()
