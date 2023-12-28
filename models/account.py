"""
Account Class

An Account represents a user on connectify.
"""

from __future__ import annotations
from models.post import Post

class Account:
    """
    A user account.

    >>> #TODO: example usage
    """
    # === Attr types ===
    # account info
    username: str
    email: str
    __password: str

    # followers
    followers: set[Account]
    num_followers: int
    following: set[Account]
    num_following: int

    # media
    posts: list[Post]  # end of list is newest posts
    __liked_posts: set[Post]

    def __init__(
            self,
            username: str,
            password: str,
            email: str
            ) -> None:
        """
        Account Constructor.
        """
        # account info
        self.username = username
        self.__password = password
        self.email = email

        # followers
        self.followers = set()
        self.following = set()
        self.num_followers = 0
        self.num_following = 0

        # media
        self.posts = []
        self.__liked_posts = set()
    
    def passwordIsCorrect(self, attempt: str) -> bool:
        """
        Return True if and only if attempt matches password.
        """
        return attempt == self.__password

    def like(self, post: Post) -> None:
        """
        Like a post.

        If post is already liked, do nothing.
        """
        if post not in self.__liked_posts:
            post.like(self)
            self.__liked_posts.add(post)
        # do nothing if this account already liked the post
    
    def remove_like(self, post: Post) -> None:
        """
        Unlike a post.

        If post is already unliked, do nothing.
        """
        if post in self.__liked_posts:
            post.remove_like(self)
            self.__liked_posts.remove(post)
        # do nothing if the account already unliked the post.

    def upload(self, post: Post) -> None:
        """
        Share a post.
        """
        self.posts.append(post)

    def delete(self, post: Post) -> None:
        """
        Delete the specified post.
        
        Precondition: post is from this user.
        """
        if post in self.posts:
            self.posts.remove(post)  # remove from posts
            del post  # remove from memory
        else:
            raise LookupError("post cannot be deleted as it does not belong to this account.")

    def follow(self, account: Account) -> None:
        """
        Follow another account.

        Do nothing if this account already follows them.
        """
        if account not in self.following:
            self.following.add(account)
            self.num_following += 1
    
    def unfollow(self, account: Account) -> None:
        """
        Unfollow another account.

        Do nothing if this account does not follow them.
        """
        if account in self.following:
            self.following.remove(account)
            self.num_following -= 1
        
    def change_username(self, new_username: str) -> None:
        """
        Change this account's username to the specified one.

        Precondition: new_username is not taken by another account.
        """
        self.username = new_username

    def change_password(self, new_password: str) -> None:
        """
        Change this account's password to the specified one.

        Precondition: password meets format requirements.
        """
        self.__password = new_password