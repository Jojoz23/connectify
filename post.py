"""
Post Class (Abstract)

A Post is a form of media that an Account can share on connectify.
"""

# image processing libraries
import numpy as np
import cv2

class Post:
    """
    Media posted by an Account.

    >>> #TODO: example usage
    """
    # Attr types
    author: str
    content: np.ndarray
    num_likes: int
    liked_by: set  # (of accounts) can't import due to circular import error

    def __init__(
            self,
            author: str,
            content: np.ndarray,
            ) -> None:
        """
        Construct a Post.
        """
        self.author = author  # username of account that posted it
        self.content = content
        self.num_likes = 0
        self.liked_by = set()

    def like(self, account) -> None:
        """
        Process a like on this post from account.

        Precondition: the account did not already like the post.
        """
        self.num_likes += 1
        self.liked_by.add(account)
    
    def remove_like(self, account) -> None:
        """
        Remove the like on this post from account.

        Precondtion: the account already liked the post.
        """
        self.num_likes -= 1
        self.liked_by.remove(account)

