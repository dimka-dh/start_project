import time
import hashlib


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return f"User(nickname={self.nickname}, age={self.age})"

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname
        return False


class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})"

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title
        return False

    def __contains__(self, keyword: str):
        return keyword.lower() in self.title.lower()


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if user.nickname == nickname and user.password == user.hash_password(password):
                self.current_user = user
                return
        print("Неверный логин или пароль")

    def register(self, nickname: str, password: str, age: int):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
            return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos: Video):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, keyword: str):
        return [video.title for video in self.videos if keyword.lower() in video.title.lower()]

    def watch_video(self, title: str):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                print(f"Смотрим: {video.title}")
                for second in range(1, video.duration + 1):
                    time.sleep(1)
                    print(second, end=' ', flush=True)
                print("\nКонец видео")
                return

        print("Видео не найдено")

    def __str__(self):
        return f"UrTube(users={len(self.users)}, videos={len(self.videos)}, current_user={self.current_user})"

    def __repr__(self):
        return f"UrTube(users={self.users}, videos={self.videos}, current_user={self.current_user})"


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')
