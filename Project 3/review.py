from user_generated_content import UserGeneratedContent

class Review(UserGeneratedContent):

    def __init__(self, title, author, game, text, rating, recommend):

        super().__init__(title, author, game)

        # Type checking for all new parameters
        if not isinstance(text, str):
            raise TypeError("Text parameter must be a string.")
        if not isinstance(rating, int) or isinstance(rating, bool):
            raise TypeError("Rating parameter must be an integer out of 10")
        if not isinstance(recommend, bool):
            raise TypeError("Recommend parameter must be a Boolean value (True or False).")

        # Checks that rating is within the allowed bounds of 1-10 inclusive
        if rating < 1 or rating > 10:
            raise ValueError("Rating must be between 1-10 inclusive.")

        self.__text = text
        self.__rating = rating
        self.__recommend = recommend

    def get_text(self):
        return self.__text

    def get_rating(self):
        return self.__rating

    def get_recommend(self):
        return self.__recommend

    text = property(get_text)
    rating = property(get_rating)
    recommend = property(get_recommend)

    def __str__(self):
        recommend_str = "Recommended" if self.recommend else "Not Recommended"
        return (f"A Review titled \"{self.title}\" with ID {self.id} for the game \"{self.game.title}\". "
                f"Written by {self.author.username} with a rating of {self.rating}/10 ({recommend_str}).")

    def get_details(self) -> str:
        recommend_str = "Yes" if self.recommend else "No"
        return_string = (f"\"{self.title}\""
                         f"\nContent type: Review"
                         f"\nGame: \"{self.game.title}\""
                         f"\nAuthor: {self.author.username}"
                         f"\nRating: {self.rating}/10"
                         f"\nRecommended: {recommend_str}"
                         f"\nReview Text: \"{self.text}\"")

        return return_string