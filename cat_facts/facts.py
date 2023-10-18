import requests

__all__ = ["Facts"]

class Facts:
    """A class to demonstrate how to use Poetry to create a custom library

    Attributes
    ----------
        None.

    Methods
    -------
        get_fact()
            Gets a random fact about cats. 
    """

    def __init__(
        self,
        api_url: str
    ):
        """
        Sets base class attributes.

        Parameters
        ----------
            api_url: str
                Gives the option to override the default API
        """
        if api_url is None:
            self.__api_url = "https://catfact.ninja/fact"
        else:
            self.__api_url = api_url

    def get_fact(self) -> str:
        """
        Gets a random fact about cats.

        Parameters
        ----------
            url : str
                URL of API to query

        Returns
        -------
            job_id : str
                The Job ID number. Kept as a string to aid later usage.
        """

        response_obj = requests.get(url=self.__api_url, timeout=60)

        if response_obj.status_code != 200:
            raise ValueError(
                f"Error! Response {response_obj.status_code} received - status 200 expected."
            )

        output = f"Random cat fact! {response_obj.json()['fact']}"
        return output
