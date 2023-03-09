import pytest
from ting_file_management.priority_queue import PriorityQueue


@pytest.mark.xfail
def test_basic_priority_queueing():
    # Test enqueueing items with priority and without priority
    q = PriorityQueue()
    q.enqueue({"nome_arquivo": "file1.txt", "qtd_linhas": 10})
    q.enqueue({"nome_arquivo": "file2.txt", "qtd_linhas": 2})
    q.enqueue({"nome_arquivo": "file3.txt", "qtd_linhas": 6})
    q.enqueue({"nome_arquivo": "file4.txt", "qtd_linhas": 4})
    assert len(q) == 4

    # Test dequeueing an item with high priority
    item = q.dequeue()
    assert item == {"nome_arquivo": "file2.txt", "qtd_linhas": 2}
    assert len(q) == 3

    # Test dequeueing an item without priority
    item = q.dequeue()
    assert item == {"nome_arquivo": "file4.txt", "qtd_linhas": 4}
    assert len(q) == 2

    # Test search an item with a valid index
    item = q.search(0)
    assert item == {"nome_arquivo": "file1.txt", "qtd_linhas": 10}

    # Test search an item with an invalid index
    with pytest.raises(IndexError):
        q.search(2)

    # Test inverted search an item with a valid index
    item = q.search(-1)
    assert item == {"nome_arquivo": "file3.txt", "qtd_linhas": 6}
