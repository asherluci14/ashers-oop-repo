from abc import ABC, abstractmethod


class StudyMaterial(ABC):
    def __init__(self, title, length):
        self.__title = title
        self.__length = length

    def get_title(self):
        return self.__title

    def get_length(self):
        return self.__length

    title = property(get_title)
    length = property(get_length)

    @abstractmethod
    def calculate_study_time(self, study_rate):
        pass


class Media(StudyMaterial):

    def calculate_study_time(self, playback_speed):
        return self.length / playback_speed


class Reading(StudyMaterial):
    # Represents a reading-based learning resource
    def __init__(self, title, author, pages):
        super().__init__(title, pages)
        self.__author = author

    # Calculates study time based on pages and reading speed
    # Includes 1 minute per page extra time for note-taking
    def calculate_study_time(self, reading_speed):
        return self.length * reading_speed + self.length * 1

    def __str__(self):
        return (
            f"Reading: ***{self.title}***\n"
            f" -Length: {self.length} pages\n"
            f" -Author: {self.__author}\n"
        )


class VideoLecture(Media):
    def __init__(self, title, length, resolution):
        super().__init__(title, length)  # Duration in minutes
        self.__resolution = resolution

    def __str__(self):
        return (
            f"Video: ***{self.title}***\n"
            f" -Length: {self.length} minutes\n"
            f" -Resolution: {self.__resolution}\n"
        )


class AudioLecture(Media):
    def __init__(self, title, length, bitrate):
        super().__init__(title, length)  # Duration in minutes
        self.__bitrate = bitrate

    def __str__(self):
        return (
            f"Audio: ***{self.title}***\n"
            f" -Length: {self.length} minutes\n"
            f" -Bitrate: {self.__bitrate}kbps\n"
        )


class Course:
    # Represents a full course made up of multiple modules
    def __init__(self, name):
        self.__name = name
        self.__modules = []

    def get_name(self):
        return self.__name

    name = property(get_name)

    def create_module(self, title):

        if not isinstance(title, str):
            return None
        else:
            module = Module(title)
            self.__modules.append(module)
            return module

    # Calculates total study time across all modules
    def calculate_study_time(self, playback_speed, reading_speed):
        total_time = 0
        for module in self.__modules:
            total_time += module.calculate_study_time(playback_speed, reading_speed)
        return total_time

    def __str__(self):
        output = f"Course: {self.__name}\n"
        output += f"Modules: {len(self.__modules)}\n\n"

        for module in self.__modules:
            output += str(module) + "\n"

        # Calculate total study time in hours.
        # use default
        # playback speed (1x playback speed)
        # reading speed (2 minutes per page)
        study_time = (self.calculate_study_time(1.0, 2.0)) / 60
        output += (
            "Course Total Length for an average student "
            "(playback at normal speed (1.0) reading rate 2 minutes per page): "
            f"{round(study_time, 2)} hours\n"
        )

        return output


class Module:
    # Represents a single teaching module within a course
    # A module has a title and contains different types of learning materials
    def __init__(self, title):
        self.__title = title
        self.__materials = []

    def get_title(self):
        return self.__title

    title = property(get_title)

    # Calculates the total study time for this module in minutes
    # Media items depend on playback speed
    # Readings depend on reading speed
    def calculate_study_time(self, playback_speed, reading_speed):
        total_time = 0

        for material in self.__materials:
            if isinstance(material, Reading):
                total_time += material.calculate_study_time(reading_speed)
            elif isinstance(material, Media):
                total_time += material.calculate_study_time(playback_speed)

        return total_time

    def __str__(self):
        output = f"Module: {self.__title}\n"

        # Total number of materials in the module
        output += f"Materials: {len(self.__materials)}\n"

        for material in self.__materials:
            output += str(material) + "\n"

        # Calculate total study time using default
        # playback speed (1x playback speed)
        # reading speed (2 minutes per page)
        output += (
            f"Total Module Length: "
            f"{round(self.calculate_study_time(1.0, 2.0), 2)} minutes\n"
        )
        return output

    def create_video_lecture(self, title, minutes, resolution):

        if not isinstance(title, str):
            return None
        else:
            lecture = VideoLecture(title, minutes, resolution)
            self.__materials.append(lecture)
            return lecture

    def create_audio_lecture(self, title, minutes, bitrate):

        if not isinstance(title, str):
            return None
        else:
            lecture = AudioLecture(title, minutes, bitrate)
            self.__materials.append(lecture)
            return lecture

    def create_reading(self, title, author, pages):

        if not isinstance(title, str):
            return None
        else:
            reading = Reading(title, author, pages)
            self.__materials.append(reading)
            return reading


course = Course('Software Design Basics')
module_1 = course.create_module("Foundations")
module_2 = course.create_module("Applications")
video_1 = module_1.create_video_lecture("Inheritance in Action", 6.1, "1920x1080")
reading_1 = module_1.create_reading("Reference Manual", "G. Van Rossum", 54)
audio_1 = module_2.create_audio_lecture("Office Hours Q&A", 7.9, "192")