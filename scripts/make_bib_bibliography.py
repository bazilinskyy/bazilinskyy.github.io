# by Pavlo Bazilinskyy <pavlo.bazilinskyy@gmail.com>
import os


def concat_bib(dir_in, dir_out, file_out):
    """Concatenate bib files into one large file.

    Args:
        dir_in (string): Directory with bib files stored as .txt plain text
                         files.
        dir_out (string): Directory for output
        file_out (string): File for concatenated output.
    """
    files = os.listdir(dir_in)
    with open(os.path.join(dir_in, file_out), 'w') as fo:
        for f in sorted(files):
            # check if we have a txt file
            if f.endswith('txt'):
                print('Appending bib info from file %s.' % f)
                try:
                    with open(os.path.join(dir_in, f)) as fi:
                        fo.write(fi.read())
                        fo.write('\n')
                # ignore subdirectories
                except IsADirectoryError:
                    print('Detected subdirectory: %s.' % f)


if __name__ == '__main__':
    # concatenate bib files
    # directory with bib files
    dir_in = os.path.join(os.path.abspath(os.path.join(__file__, '../..')),
                          '_publications')
    # output directory for the concatenated file
    dir_out = os.path.join(os.path.abspath(os.path.join(__file__, '../..')),
                           '_publications')
    # concatenated file
    file_out = 'bazilinskyy.bib'
    concat_bib(dir_in, dir_out, file_out)
