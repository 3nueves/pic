""" Module to manager git repos """

from git import Repo

class Git():
    """ class Manage Git """

    def __init__(self, local_dir=None) -> None:
        self.repo = Repo(local_dir)

    def clone_repo(self, repo_url: str, local_dir: str) -> None:
        """ func to clone repo """
        _ = self.repo.clone_from(repo_url, local_dir)

    def pull_repo(self):
        """ func to pull repo """
        origin = self.repo.remotes.origin
        origin.pull()
