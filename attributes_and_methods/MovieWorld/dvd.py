class DVD:
    def __init__(self, name, id, creation_year, creation_month: str, age_restriction: int):
        self.creation_year = creation_year
        self.name = name
        self.id = id
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def rented_status(self):
        if self.is_rented:
            return f'rented'
        return f'not rented'

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {self.rented_status()}"

    @classmethod
    def from_date(cls, id: int, name: str, date, age_restriction):
        day, month, year = date.split(".")
        ##TODO month to STRING
        months = {
            '01': 'Janauary',
            '02': 'February',
            '03': 'March',
            '04': 'April',
            '05': 'May',
            '06': 'June',
            '07': 'July',
            '08': 'August',
            '09': 'September',
            '10': 'October',
            '11': 'November',
            '12': 'December'
        }

        return cls(name, id, int(year), months[month], age_restriction)


