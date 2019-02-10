import regression_tree
import sys
import csv


def main(col_names=None):
    # parse command-line arguments to read the name of the input csv file
    # and optional 'draw tree' parameter
    if len(sys.argv) < 2:  # input file name should be specified
        print ("Please specify input csv file name")
        return

    csv_file_name = sys.argv[1]

    data = []
    with open(csv_file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            data.append(list(row))

    print("Total number of records = ",len(data))
    tree = regression_tree.buildtree(data[1:], min_gain =0.004, min_samples = 5)

    regression_tree.printtree(tree, '', col_names)

    max_tree_depth = regression_tree.max_depth(tree)
    print("max number of questions=" + str(max_tree_depth))

    if len(sys.argv) > 2: # draw option specified
        import dtree_draw_regression
        dtree_draw_regression.drawtree(tree, jpeg=csv_file_name+'.jpg')

    if len(sys.argv) > 3:  # create json file for d3.js visualization
        import json
        import regression_to_json
        json_tree = regression_to_json.dtree_to_jsontree(tree, col_names)

        # create json data for d3.js interactive visualization
        with open(csv_file_name + ".json", "w") as write_file:
            json.dump(json_tree, write_file)

    #4.5, 4.469
    print("course evaluation score ['tenured', 'not minority', 'male', 'english', 50, 30, 'lower', 5, 4] is: ", regression_tree.classify(['tenured', 'not minority', 'male', 'english', 50, 30, 'lower', 5, 4], tree))
    #4.0, 4.248
    print("course evaluation score ['tenure track', 'not minority', 'female', 'english', 30, 30, 'upper', 6, 4] is: ", regression_tree.classify(['tenure track', 'not minority', 'female', 'english', 30, 30, 'upper', 6, 4], tree))
    #3.5, 3.446
    print("course evaluation score ['teaching', 'not minority', 'female', 'english', 40, 30, 'lower', 5, 3] is: ", regression_tree.classify(['teaching', 'not minority', 'female', 'english', 40, 30, 'lower', 5, 3], tree))



if __name__ == "__main__":
    col_names = ['rank',
                 'ethnicity',
                 'gender',
                 'language',
                 'age',
                 'class_size',
                 'cls_level',
                 'bty_avg',
                 'prof_eval']
    main(col_names)
