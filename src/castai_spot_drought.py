import os
import requests

castai_api_key: str = os.getenv("CASTAI_API_KEY")

organization_id: str = "CASTAI_ORGANIZATION_ID"

cluster_id: str = "CASTAI_CLUSTER_ID"

aks_instance_families: list = [
    "standard_DADSv5",
    "standard_DASv4",
    "standard_DASv5",
    "standard_DAv4",
    "standard_DCADSv5_CC",
    "standard_DCASv5_CC",
    "standard_DCDSv3",
    "standard_DCS",
    "standard_DCSv2",
    "standard_DCSv3",
    "standard_DCv2",
    "standard_DDSv4",
    "standard_DDSv5",
    "standard_DDv4",
    "standard_DDv5",
    "standard_DLDSv5",
    "standard_EBSv5",
    "standard_ECADSv5_CC",
    "standard_ECASv5_CC",
    "standard_EDSv4",
    "standard_EDSv5",
    "standard_EDv4",
    "standard_EDv5",
    "standard_EIADSv5",
    "standard_EIASv5",
    "standard_EIBDSv5",
    "standard_EIBSv5",
    "standard_EIDSv4",
    "standard_EIDSv5",
    "standard_EIDv5",
    "standard_EISv3",
    "standard_EISv4",
    "standard_EISv5",
    "standard_EIv5",
    "standard_ESv3",
    "standard_ESv4",
    "standard_ESv5",
    "standard_Ev4",
    "standard_Ev5",
    "standard_FS",
    "standard_FSv2",
    "standard_FXDS",
    "standard_HBRS",
    "standard_HBRSv2",
    "standard_HBRSv3",
    "standard_HBRSv4",
    "standard_HCRS",
    "standard_HXRS",
    "standard_LASv3",
    "standard_LSv2",
    "standard_LSv3",
    "standard_M",
    "standard_MDMSv2",
    "standard_MDSv2",
    "standard_MIDMSv2",
    "standard_MIDSv2",
    "standard_MISv2",
    "standard_MLS",
    "standard_MS",
    "standard_MSv2",
    "standard_MSv2_8",
    "standard_MTS",
    "standard_NCADSv4_A100",
    "standard_NCASv3_T4",
    "standard_NCRSv2",
    "standard_NCRSv3",
    "standard_NCSv2",
    "standard_NCSv3",
    "standard_NDAMSRv4_A100",
    "standard_NDASRv4",
    "standard_NDRS",
    "standard_NDRSv2",
    "standard_NDS",
    "standard_NPS",
    "standard_NVADMSv5_A10",
    "standard_NVADSv5_A10",
    "standard_NVASv4",
    "standard_NVSv3",
    "standard_PBS",
]

eks_instance_families: list = [
    "c5",
    "c5a",
    "c5ad",
    "c5d",
    "c5n",
    "c6a",
    "c6g",
    "c6gd",
    "c6gn",
    "c6i",
    "c6id",
    "c6in",
    "c7a",
    "c7g",
    "c7gd",
    "c7gn",
    "c7i",
    "d2",
    "d3",
    "d3en",
    "dl1",
    "f1",
    "g3",
    "g3s",
    "g4ad",
    "g4dn",
    "g5",
    "g5g",
    "h1",
    "i3",
    "i3en",
    "i4g",
    "i4i",
    "im4gn",
    "inf1",
    "inf2",
    "is4gen",
    "m5",
    "m5a",
    "m5ad",
    "m5d",
    "m5dn",
    "m5n",
    "m5zn",
    "m6a",
    "m6g",
    "m6ad",
    "m6gd",
    "m6i",
    "m6id",
    "m6idn",
    "m6in",
    "m7a",
    "m7g",
    "m7gd",
    "m7i",
    "m7i-flex",
    "p2",
    "p3",
    "p4d",
    "p5",
    "r5",
    "r5a",
    "r5ad",
    "r5b",
    "r5b",
    "r5d",
    "r5dn",
    "r5n",
    "r6a",
    "r6g",
    "r6gd",
    "r6i",
    "r6id",
    "r6idn",
    "r7a",
    "r7g",
    "r7gd",
    "r7i",
    "r7iz",
    "trn1",
    "u-12tb1",
    "u-18tb1",
    "u-3tb1",
    "u-6tb1",
    "u-9tb1",
    "vt1",
    "x1",
    "x1e",
    "x2gd",
    "x2idn",
    "x2iedn",
    "x2izn",
    "z1d",
]

gke_instance_families: list = [
    "a2",
    "c2",
    "c2d",
    "c3",
    "e2",
    "g2",
    "m1",
    "n1",
    "n2",
    "n2d",
    "t2a",
    "t2d",
]

blacklist_headers: dict = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-API-Key": f"{castai_api_key}",
}


def add_to_blacklist(instance_families: list) -> list:
    add_blacklist_url = "https://api.cast.ai/v1/inventory/blacklist/add"
    responses = []
    for family in instance_families:
        payload = {
            "lifecycle": "spot",
            "organizationId": f"{organization_id}",
            "clusterId": f"{cluster_id}",
            "instanceFamily": f"{family}",
        }
        responses.append(
            requests.post(add_blacklist_url, json=payload, headers=blacklist_headers)
        )
    return responses


def get_blacklist() -> str:
    get_blacklist_url: str = "https://api.cast.ai/v1/inventory/blacklist"
    headers: dict = {"accept": "application/json", "X-API-Key": f"{castai_api_key}"}
    response: requests.Response = requests.get(get_blacklist_url, headers=headers)
    return response.text


def remove_from_blacklist(instance_families: list) -> list:
    remove_blacklist_url: str = "https://api.cast.ai/v1/inventory/blacklist/remove"
    responses: list = []
    for family in instance_families:
        payload: dict = {
            "lifecycle": "spot",
            "organizationId": f"{organization_id}",
            "clusterId": f"{cluster_id}",
            "instanceFamily": f"{family}",
        }
        responses.append(
            requests.post(remove_blacklist_url, json=payload, headers=blacklist_headers)
        )
    return responses


def interactive_mode():
    while True:
        print("Choose an option:")
        print("1: Add to blacklist")
        print("2: Get blacklist")
        print("3: Remove from blacklist")
        print("4: Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice in ["1", "3"]:
            print("Select instance family list:")
            print("a: AKS")
            print("b: EKS")
            print("c: GKE")
            family_choice = input("Enter your choice (a/b/c): ")

            if family_choice == "a":
                families = aks_instance_families
            elif family_choice == "b":
                families = eks_instance_families
            elif family_choice == "c":
                families = gke_instance_families
            else:
                print("Invalid choice for instance family. Try again.")
                continue

            if choice == "1":
                add_responses = add_to_blacklist(families)
                print(add_responses)
            elif choice == "3":
                remove_responses = remove_from_blacklist(families)
                print(remove_responses)
        elif choice == "2":
            blacklist = get_blacklist()
            print(blacklist)
        elif choice == "4":
            break
        else:
            print("Invalid main menu choice. Try again.")


if __name__ == "__main__":
    interactive_mode()
