#
from constants import Constants


#
def get_file_name(file_dir, model, cpt, block, i):
    """
    get prediction file name

    :params file_dir - directory where all prediction files are
    :params model - model name
    :params cpt - chapter number
    :params block - block number
    :params i - iteration number

    :returns: file path
    """
    frmt = "{}/predictions_{}_{}_{}_{}.npy"
    file_path = frmt.format(
                        file_dir,
                        model,
                        f'{cpt:03d}',
                        f'{block:03d}',
                        f'{i:02d}'
                    )
    return file_path


#
def is_vowel(letter):
    """
    check if letter is vowel

    :params letter - letter which should be checked

    :returns: True or False
    """
    return letter in Constants.vowels
