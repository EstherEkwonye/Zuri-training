class Student:

    def __init__(self, name: str, age: int, tracks: list, score: float):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def __str__(self):
        return f"{self.name} is {self.age} years old and has {self.score} points. He enrolled for {self.tracks[0]} in the I4G course."

    def change_name(self, name: str):
        self.name = name
        return self.name

    def change_age(self, age: int):
        self.age = age
        return self.age

    def add_track(self, track: str):
        self.tracks.append(track)
        return self.tracks

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("Product Designer")
Bob.get_score()

print(Bob)

