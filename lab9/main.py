"""
main.py

Программа реализует следующий алгоритм:
1) Сгенировать и записать последовательность нужной длины в файл (далее - исходный файл).
2) Создать необходимое количество пустых файлов.
3) Прочитать максимально возможное количество элементов из исходного файла.
4) Отсортировать полученную последовательность внутренней сортировкой.
   (Отсортированную последовательность будем называть отрезком).
5) Повторять шаги 3-4, распределяя отрезки во все файлы, кроме исходного и последнего,
   до тех пор, пока исходный файл не будет прочтён полностью.
6) Очистить исходный файл.
7) Если в непустых файлах хранится не более одного отрезка, то
   слить их в один файл (результирующий) и перйти к шагу 11.
8) Слить все отрезки в два пустых файла и очистить файлы, с которых читались данные.
9) Распределить отрезки на все пустые фалы и очистить файлы,
   с которых читались данные и перейти к шагу 7.
11) Удалить все файлы, кроме результируещего и закончить выполнение.

***
    По произвоительности программа получилось крайне не эфективная. Я хотел достичь хоть какой-нибудь гибкости,
чтобы можно было задавать произвольное количество файлов и максимальных элементов, если это не противоречит
алгоритму выше, из-за чего пострадала производительность. Но главная причина тормознутости - простое неумение
писать эффективные программы.
    Для экономии памяти, я также решил использовать генераторы, что перетекло в постоянную головную боль с отлавливанием
StopIteration ошибок.
    Тем не менее программа неплохо справляется с сортировкой больших последовательностей, но при условии, что количество
файлов, которое можно задействовать для сортировки, также задано большое.
    Из всех лабораторных работ, эта была самая интересная :D.
***
(c) Хасанов Ислам, КЭ-101
GitHub: https://github.com/Khasanov41/Laboratory-works.git
"""
import tape as tp
import sorts as sr
from math import ceil


def update_chunks(ch_list, gen_list):
    """
    Fills empty chunks with the following.
    If this is not possible, then removes the chunk from the list.

    Warning: All actions modify the original chunks list!

    :param ch_list: List with tapes keys.
    :param gen_list: List with chunks generators.
    :return: True, if at least one of the chunks has been updated, otherwise it is False.
    """
    update_flag = False
    for i in range(len(ch_list)):
        if not ch_list[i]:
            update_flag = True
            try:
                ch_list[i] = next(gen_list[i])
            except StopIteration:
                ch_list[i] = [None]
    return update_flag


def merge_files(source, result, limit, ch_size):
    """
    Merge files with chunks.

    :param set | list source: Keys map of source tapes with chunks to merge.
    :param set | list result: Keys map of files for writing merged chunks.
    :param int limit: Max elements in RAM.
    :param int ch_size: Max number of elements in one chunk.
    """
    buff_ch = limit // (len(source) + 1)  # Number of elements in one segment.
    assert buff_ch != 0, "Buffer error!"
    buff_size = limit - buff_ch * len(source)
    assert buff_size != 0, "Buffer error!(2)"
    chunk_gens = [tp.split_tape(k, buff_ch, ch_size) for k in source]
    chunks_ = [next(chunk_gens[i]) for i in range(len(source))]
    buffer = []                     # List of elements to write to file.
    merge = sr.minimal(chunks_)     # First charging merge sort.
    index = 0                       # Index of output file in result list.

    while chunks_.count([None]) != len(chunks_):  # != []
        buffer.append(next(merge))
        if len(buffer) == buff_size:
            tp.write_seg(result[index % len(result)], buffer, True)
        if update_chunks(chunks_, chunk_gens):
            if chunks_ == [[None]]:
                break
            elif chunks_.count([None]) == len(chunks_):  # All chunks = [None].
                if len(buffer) != 0:
                    tp.write_seg(result[index % len(result)], buffer, True)
                for i in range(len(chunks_)):
                    try:
                        chunks_[i] = next(chunk_gens[i])
                    except StopIteration:
                        continue
                index += 1
            merge = sr.minimal([i for i in chunks_ if i != [None]])  # Recharging merge sort.


if __name__ == "__main__":
    length = 60000  # Size of original sequence.
    files = 6       # The number of files needed for sorting.
    items = 50      # The maximum number of items that can be stored in RAM.
    assert items > files - 2, "Input parameters error!"
    ch_count = ceil(length / items)     # Number of chunks.
    ch_length = items                   # Number of items in one chunk.
    print("Please wait...")
    with tp.tapes(files, length) as res:
        chunks, key = tp.split_tape(0, items), 0
        # Distribute segments to all files except the original and the last one.
        for _ in range(ch_count):
            key = key + 2 if key % (files - 1) == files - 2 else key + 1
            tp.write_seg(key % (files - 1), sr.insert_sort(next(chunks)))

        # Uncomment to display the original sequence.
        # print("Original sequence:")
        # tp.print_tape(0)

        del _, chunks
        tp.clear_tape(0)
        nonempty = [i for i in range(1, files) if tp.chek_tape(i)]
        empty = [i for i in range(files) if i not in nonempty]

        # Uncomment to display distributed sequences.
        # print("\nDistributed sequences:")
        # for i in nonempty:
        #    tp.print_tape(i)

        while ch_count > len(nonempty):
            merge_files(nonempty, empty, items, ch_length)

            # Uncomment to output each sorting step.
            # print("\nStage sequence:")
            # for i in empty:
            #    tp.print_tape(i)

            ch_count = ceil(ch_count / len(nonempty))
            ch_length = ch_length * len(nonempty)

            for i in nonempty:  # Clear all read tapes.
                tp.clear_tape(i)
            nonempty = [i for i in range(files) if tp.chek_tape(i)]
            empty = [i for i in range(files) if i not in nonempty]
        else:
            merge_files(nonempty, res, items, ch_length)

            # Uncomment to display the sorted sequence.
            # print("\nResult sequence:")
            # tp.print_tape(res[0])

            print("Done! The result is located in the ./tapes/ directory.")
