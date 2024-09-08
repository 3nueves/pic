""" Module to manager git repos """

from git import Repo

class Git():
    """ class Manage Git """

    def __init__(self) -> None:
        self.git = Repo()
    
    def clone_repo(self, repo_url: str, local_dir: str) -> None:
        """ func to clone repo """
        _ = self.git.clone_from(repo_url, local_dir)