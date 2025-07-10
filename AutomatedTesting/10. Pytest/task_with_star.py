# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)  # через реквест?
def test(request):
    # Здесь пишем код
    id = request.keywords.node.own_markers[0].args  # Нашёл через дебаг маркер и вытащил путь до args
    print(*id)
    pass
