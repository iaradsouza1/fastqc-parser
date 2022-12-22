import pandas as pd

opt_dict = {
    "basic_statistics":             ">>Basic Statistics",
    "per_base_quality":             ">>Per base sequence quality",
    "per_sequence_quality_scores":  ">>Per sequence quality scores",
    "per_base_sequence_content":    ">>Per base sequence content",
    "per_sequence_gc_content":      ">>Per base sequence content",
    "per_base_n_content":           ">>Per base N content",
    "sequence_length_distribution": ">>Sequence Length Distribution",
    "sequence_duplication_levels":  ">>Sequence Duplication Levels",
    "overrepresented_sequences":    ">>Overrepresented sequences",
    "adapter_content":              ">>Adapter Content"
}

def get_table_summaries(opt, file):

    count_line = [0, 0]
    inside = False
    res_list = []

    with open(file, "r") as fn:
        for i, line in enumerate(fn):
            if line.startswith(opt_dict[opt]):
                count_line[0] = i+1
                inside = True
            elif line.startswith(">>END_MODULE") and inside:
                count_line[1] = i-1
                break

    with open(file, "r") as fn:
        for i, line in enumerate(fn):
            if i >= count_line[0] and i <= count_line[1]:
                if line.startswith("#"):
                    colnames = line.strip("#").strip().split("\t")
                else:
                    res_list.append(line.strip().split("\t"))

    df = pd.DataFrame(res_list)
    df.columns = colnames
    return df.to_csv(path_or_buf=None,index=False, header=True, sep=";")
