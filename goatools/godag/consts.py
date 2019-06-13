"""GO-DAG constants."""

__copyright__ = "Copyright (C) 2010-2019, DV Klopfenstein, H Tang, All rights reserved."
__author__ = "DV Klopfenstein"


NAMESPACE2NS = {
    'biological_process' : 'BP',
    'molecular_function' : 'MF',
    'cellular_component' : 'CC'}

# https://owlcollab.github.io/oboformat/doc/GO.format.obo-1_4.html
RELATIONSHIP_LIST = ['part_of', 'regulates', 'negatively_regulates', 'positively_regulates']
RELATIONSHIP_SET = set(RELATIONSHIP_LIST)

top_terms = set(['GO:0008150', 'GO:0003674', 'GO:0005575']) # BP, MF, CC
NS2GO = {'BP':'GO:0008150', 'MF':'GO:0003674', 'CC':'GO:0005575'}
NAMESPACE2GO = {'biological_process':'GO:0008150',
                'molecular_function':'GO:0003674',
                'cellular_component':'GO:0005575'}


# Copyright (C) 2010-2019, DV Klopfenstein, H Tang, All rights reserved.
