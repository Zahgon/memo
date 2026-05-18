from typing import Callable, Dict, Iterable, Optional
from types import GeneratorType
from joblib import Parallel, delayed, parallel_backend
import joblib.parallel
from rich.progress import Progress
import time
import warnings


class Runner:
    """
    Run functions in parallel with joblib.

    Arguments:
        backend: choice of parallism backend, can be "loky", "multiprocessing" or "threading"
        n_jobs: degree of parallism, set to -1 to use all available cores

    All keyword arguments during instantiaition will pass through to `parallel_backend`.
    More information on joblib can be found [here](https://joblib.readthedocs.io/en/latest/parallel.html).
    Joblib can also attach to third party backends such as Ray or Apache spark,
    however that functionality has not yet been tested.

    Usage:

    ```python
    from memo import Runner

    runner = Runner(backend='threading', n_jobs=2)
    ```
    """

    def __init__(
        self,
        *args,
        backend: Optional[str] = "loky",
        n_jobs: Optional[int] = None,
        **kwargs,
    ):
        self.args = args
        self.kwargs = kwargs
        self.backend = backend
        self.n_jobs = n_jobs

    def _run(self, func: Callable, settings: Iterable[Dict]) -> None:
        """run the parallel backend
        Private. All arguments passed through run method
        """
        pass

    def run(
        self, func: Callable, settings: Iterable[Dict], progbar: bool = True
    ) -> None:
        """Run function with joblibs parallel backend

        Args:
            func (Callable): The function to be run in parallel.
            settings (Iterable): An Iterable of Key-value pairs.
            progbar (bool, optional): Show progress bar. Defaults to True.

        Raises:
            TypeError: When **kwargs doesn't match signature of `parallel_backend`

        Usage:

        ```python
        from memo import Runner
        import numpy as np

        from memo import memlist, grid, time_taken

        data = []


        @memlist(data=data)
        @time_taken()
        def birthday_experiment(class_size, n_sim):
            sims = np.random.randint(1, 365 + 1, (n_sim, class_size))
            sort_sims = np.sort(sims, axis=1)
            n_uniq = (sort_sims[:, 1:] != sort_sims[:, :-1]).sum(axis=1) + 1
            proba = np.mean(n_uniq != class_size)
            return {"est_proba": proba}

        settings = grid(class_size=range(20, 30), n_sim=[100, 10_000], progbar=False)

        # To Run in parallel
        runner = Runner(backend="threading", n_jobs=-1)
        runner.run(func=birthday_experiment, settings=settings)
        ```
        """
        pass
