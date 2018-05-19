with gzip.GzipFile(filename, 'rb') as f:
                    wellData = pickle.load(f)

