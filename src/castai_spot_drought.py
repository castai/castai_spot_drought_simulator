import os
import requests

castai_api_key: str = os.getenv("CASTAI_API_KEY")
organization_id: str = "CASTAI_ORGANIZATION_ID"
cluster_id: str = "CASTAI_CLUSTER_ID"
blacklist_headers: dict = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-API-Key": f"{castai_api_key}",
}


def extract_instance_families() -> list:
    filter_instance_types_url: str = f"https://api.cast.ai/v1/kubernetes/clusters/{cluster_id}/filter-instance-types"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-Key": f"{castai_api_key}"
    }
    response = requests.post(filter_instance_types_url, headers=headers)
    available_instance_types = response.json()
    return list(set([instance["family"] for instance in available_instance_types["availableInstanceTypes"]]))


def add_to_blacklist(instance_families: list) -> list:
    add_blacklist_url: str = "https://api.cast.ai/v1/inventory/blacklist/add"
    responses: list = []
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
    families = extract_instance_families()
    while True:
        print("Choose an option:")
        print("1: Add to blacklist")
        print("2: Get blacklist")
        print("3: Remove from blacklist")
        print("4: Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_responses = add_to_blacklist(families)
            print(add_responses)
        elif choice == "2":
            blacklist = get_blacklist()
            print(blacklist)
        elif choice == "3":
            remove_responses = remove_from_blacklist(families)
            print(remove_responses)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    interactive_mode()
