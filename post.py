##############################
### OBSERVAR Class & Objects##
##############################
# OBSERVAR main2.py #
#####################


class Post:
    def __int__(self, message, author):
        self.message =  message
        self.author = author

    def get_post_info(self):
        print(f"Post: {self.message} written by {self.author}")