import pandas as pd
import requests
import sys
from chembl_webresource_client.new_client import new_client

# REMINDER: activity endpoint links compounds to targets

if __name__ == '__main__':
    drugs = new_client.drug.filter(first_approval__isnull=False, first_approval__gte=2012.0).order_by('first_approval')
    drdf = pd.DataFrame(drugs)

    activities = new_client.activity.filter(molecule_chembl_id__in=list(drdf.molecule_chembl_id)).only(['target_chembl_id'])
    targets_id = [a['target_chembl_id'] for a in activities]
    targets_id_unique = list(set(targets_id))

    targets = new_client.targets.filter(targets_chembl_id__in=targets_id_unique)
    tgdf = pd.DataFrame(targets)

    accessions = []

    requestURLs = ["https://www.ebi.ac.uk/proteins/api/proteins/{}".format(a) for a in accessions]

    keywords = []

    for url in requestURLs:
        r = requests.get(url, headers={"Accept": "application/xml"})
        if not r.ok:
            r.raise_for_status()
            sys.exit()
        responseBody = r.text
        keywords.append(responseBody)
