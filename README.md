# Description

FASTQC results are stored on the `fastqc_data.txt`. This file has multiple fields, which are represented on the HTML output. This simple tool extracts each field and returns it as a csv file. 

# Requirements 

- Python 3
- pandas

## Usage 

Clone this repo:

```
git clone git@github.com:iaradsouza1/fastqc-parser.git
```

To get help:
```
python fastqc-parser.py --help
```

The options available are: `basic_staistics`, `per_base_quality`, `per_sequence_quality_scores`, `per_base_sequence_content`, `per_sequence_gc_content`, `per_base_n_content`, `sequence_length_distribution`, `sequence_duplication_levels`, `overrepresented_sequences`, `adapter_content`.

Run the `fastqc-parser.py`:

```
python fastqc-parser.py -f fastqc_data.txt -s per_base_quality
```

