"""
Программа реализует следующий алгоритм:
1) Сгенировать и записать последовательность нужной длины в файл (далее - исходный файл).
2) Создать необходимое количество пустых файлов.
3) Прочитать максимально возможное количество элементов из исходного файла.
4) Отсортировать полученную последовательность внутренней сортировкой.
   (Отсортированную последовательность будем называть отрезком).
5) Повторять шаги 3-4, распределяя отрезки во все файлы, кроме исходного и последнего,
   до тех пор, пока исходный файл не будет прочтён полностью.
6) Очистить исходный файл.
7) Если в непустых файлах хранится по одному отрезку, то
   слить их в один файл (результирующий) и перйти к шагу 13.
8) Слить все отрезки в два пустых файла и очистить файлы, с которых читались данные.
9) Распределить отрезки на все пустые фалы и очистить файлы,
   с которых читались данные и перейти к шагу 7.
11) Удалить все файлы, кроме результируещего и закончить выполнение.
"""
import tape as tp
import sorts as sr
from math import ceil


def update_chunks(ch_list, gen_list):
    """
    Fills empty chunks with the following.
    If this is not possible, then removes the chunk from the list.
    Warning: All actions modify the original chunks list!

    :param ch_list: List with tape keys.
    :param gen_list: List with chunks generators.
    :return:
    """
    updated = False
    for i in range(len(ch_list)):
        if not ch_list[i]:
            updated = True
            try:
                ch_list[i] = next(gen_list[i])
            except StopIteration:
                del ch_list[i]
    return updated


def test_update_chunks():
    with tp.tapes(3, 20):
        chunks_ = tp.split_tape(0, 10)
        for i in (1, 2):
            tp.write_seg(i, next(chunks_))
        chunk_gens = [tp.split_tape(i, 2) for i in (1, 2)]
        chunks_ = [next(chunk_gens[i]) for i in (0, 1)]
        for i in range(5):
            print(chunks_[0], chunks_[1])
            chunks_[1] = []
            update_chunks(chunks_, chunk_gens)


def merge_files(source, result, limit, ch_size):
    """
    Merge files with chunks.

    :param set | list source: Keys map of source tapes with chunks to merge.
    :param set | list result: Keys map of files for writing merged chunks.
    :param int limit: Max elements in RAM.
    :param int ch_size: Max number of elements in one chunk.
    """
    buff_ch = limit // (len(source) + 1)  # Number of elements in one segment.
    buff_size = limit - buff_ch * len(source)
    chunk_gens = [tp.split_tape(k, buff_ch, ch_size) for k in source]
    chunks_ = [next(chunk_gens[i]) for i in range(len(source))]
    buffer = []   # List of elements to write to file.
    merge = sr.minimal(chunks_)  # First charging merge sort.
    index = 0   # Index of output file in result list.

    while chunks_:  # != []
        # BUG IN MERGE SORT!
        buffer.append(next(merge))
        if len(buffer) == buff_size:
            tp.write_seg(result[index % len(result)], buffer)
            buffer.clear()
        if update_chunks(chunks_, chunk_gens):
            # chunks_.count([None]) == len(source):
            if not [0 for i in chunks_ if i != [None]]:  # All elements in chunks = [None].
                if len(buffer) != 0:
                    tp.write_seg(index % (len(result) + 1), buffer)
                try:
                    chunks_ = [next(chunk_gens[i]) for i in range(len(source))]
                except StopIteration:
                    break
                index += 1
            # Recharge merge sort.
            merge = sr.minimal([i for i in chunks_ if i != [None]])  # BUG! Merge sort will not delete element.
            # Merge sort is not ready to sort None objects!


if __name__ == "__main__":
    length = 11  # 60000  # Size of original sequence.
    files = 6  # 6       # Number of files.
    max_e = 3  # 50      # Max number of elements in RAM.
    ch_count = ceil(length / max_e)     # Number of chunks.
    ch_length = max_e      # Number of elements in one chunk.
    with tp.tapes(files, length) as res:
        chunks, key = tp.split_tape(0, max_e), 0
        # Distribute segments to all files except the original and the last one.
        for _ in range(ch_count):
            key = key + 2 if key % (files - 1) == files - 2 else key + 1
            tp.write_seg(key % (files - 1), sr.insert_sort(next(chunks)))

        tp.read_tape(0)  # Debug!
        tp.clear_tape(0)
        nonempty = [i for i in range(1, files) if tp.chek_tape(i)]
        empty = [i for i in range(files) if i not in nonempty]

        while ch_count > len(nonempty):
            merge_files(nonempty, empty, max_e, ch_length)
            for i in empty:
                tp.read_tape(i)
            ch_count = ceil(ch_count / len(nonempty))
            for i in nonempty:  # Clear all read tapes.
                tp.clear_tape(i)
            nonempty = [i for i in range(files) if tp.chek_tape(i)]
            empty = [i for i in range(files) if i not in nonempty]
        else:
            ch_length = ceil(length / ch_count)
            merge_files(nonempty, res, max_e, ch_length)
            tp.read_tape(res[0])
