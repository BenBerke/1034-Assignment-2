class Job:

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

        self.name = name
        self.category = category
        self.rate = rate
        self.date = date
        self.hours = hours

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

    def get_rate(self):
        return self.rate

    def get_date(self):
        return self.date

    def get_hours(self):
        return self.hours

    def __eq__(self, other):
        if not isinstance(other, Job):
            return False
        return self.name == other.name and self.category == other.category and self.rate == other.rate and self.date == other.date and self.hours == other.hours

    def __hash__(self):
        return hash((self.name, self.category, self.rate, self.date, self.hours))

    def __str__(self):
        return f"Job({self.name} {self.category} {self.rate} {self.date} {self.hours})"

    def __repr__(self):
        return self.__str__()
