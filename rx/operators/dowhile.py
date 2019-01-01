from typing import Callable, Any
from rx.core import Observable, StaticObservable


def do_while(condition: Callable[[Any], bool]) -> Callable[[Observable], Observable]:
    """Repeats source as long as condition holds emulating a do while loop.

    Keyword arguments:
    condition -- The condition which determines if the source
        will be repeated.

    Returns an observable {Observable} sequence which is repeated as long
    as the condition holds.
    """

    def partial(source: Observable) -> Observable:
        return source.concat(StaticObservable.while_do(condition, source))
    return partial
