import argparse
from util.parser import *

def main():
    parser = argparse.ArgumentParser(description='A tool to parse results from FASTQC. Returns a csv (";") tabular data for each option.')

    parser.add_argument("-f", "--file", dest="file", default=None, required=True, action="store", help="The 'fastqc_data.txt' file from fastqc command")
    parser.add_argument("-s", "--summary", dest="sum", default=None, required=True, action="store",
    help=
    """One of the following options: 
    basic_statistics, per_base_quality, per_sequence_quality_scores, 
    per_base_sequence_content, per_sequence_gc_content, per_base_n_content, 
    sequence_length_distribution, sequence_duplication_levels, 
    overrepresented_sequences, adapter_content
    """)

    args = parser.parse_args()

    if args.file and args.sum:
        df = get_table_summaries(args.sum, args.file)
        print(df)

if __name__ == '__main__':
    main()
