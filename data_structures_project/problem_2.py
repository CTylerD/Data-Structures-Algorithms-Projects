import os


def find_files(suffix, path):
    files_list = []
    find_files_solver(suffix, path, files_list)
    return files_list


def find_files_solver(suffix, path, files_list):
    pathway = os.listdir(path)
    for content in pathway:
        file_path = os.path.join(path, content)
        if os.path.isdir(file_path):
            find_files_solver(suffix, file_path, files_list)
        elif os.path.isfile(file_path):
            if suffix and file_path.endswith(suffix):
                files_list.append(file_path)
    return files_list


# test case 1 - multiple files/dirs
test_case_1 = (find_files('.c', './testdir'),
               ['./testdir/subdir3/subsubdir1/b.c',
                './testdir/t1.c',
                './testdir/subdir5/a.c',
                './testdir/subdir1/a.c'])

if test_case_1[0] == test_case_1[1]:
    print("Test 1: Pass!")
else:
    print("Test 1: FAIL.")

# test case 2 - single file/dir
test_case_2 = (find_files('.h', './testdir/subdir3'),
               ['./testdir/subdir3/subsubdir1/b.h'])

if test_case_2[0] == test_case_2[1]:
    print("Test 2: Pass!")
else:
    print("Test 2: FAIL.")

# test case 3 - file doesn't exist
test_case_3 = (find_files('.c', './testdir//subdir2'), [])

if test_case_3[0] == test_case_3[1]:
    print("Test 3: Pass!")
else:
    print("Test 3: FAIL.")

# test case 4 - empty file extension
test_case_4 = (find_files('', './testdir'), [])

if test_case_4[0] == test_case_4[1]:
    print("Test 4: Pass!")
else:
    print("Test 4: FAIL.")
