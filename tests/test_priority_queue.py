import pytest
import occasionally


def insert_new_top(q, val):
    # type: (occasionally.priority_queue.PriorityQueue, any) -> None
    q.enqueue(val)
    assert q._queue[0] == val


def test_priority_min_queue(priority_min_queue):
    insert_new_top(priority_min_queue, 5)  # insert a 5 -- only element so at the top
    insert_new_top(priority_min_queue, 1)  # insert a 1 -- new top, so deque should be [1, 5]
    assert priority_min_queue._queue[1] == 5
    insert_new_top(priority_min_queue, -500)  # insert -500 -- new top again
    priority_min_queue.enqueue(-200)  # insert -200 -- -500 should still be tpo
    assert priority_min_queue._queue[0] == -500
    assert priority_min_queue.peek() == -500
    sort_results = priority_min_queue.queue_sort()
    assert sort_results == [-500, -200, 1, 5]


def test_priority_max_queue(priority_max_queue):
    insert_new_top(priority_max_queue, 10)
    insert_new_top(priority_max_queue, 20)
    insert_new_top(priority_max_queue, 30)
    assert priority_max_queue.peek() == 30
    sort_results = priority_max_queue.queue_sort()
    assert sort_results == [30, 20, 10]


def test_dequeue_empty_error_raises(priority_max_queue):
    with pytest.raises(occasionally.priority_queue.QueueEmptyException):
        priority_max_queue.dequeue()
    with pytest.raises(occasionally.priority_queue.QueueEmptyException):
        priority_max_queue.peek()


def test_queue_full_insert_error_raises(small_max_queue):
    small_max_queue.enqueue(1)
    small_max_queue.enqueue(1)
    with pytest.raises(occasionally.priority_queue.QueueFullException):
        small_max_queue.enqueue(1)
    # sort empties the queue
    sort_results = small_max_queue.queue_sort()
    assert sort_results == [1, 1]
