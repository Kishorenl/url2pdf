def read_file_in_batches(file_path, batch_size):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        for i in range(0, len(lines), batch_size):
            batch = lines[i:i + batch_size]
            return batch
