import json
from pprint import pp

path = 'data/candidates.json'

def load_candidates_from_json():
    """Возвращает список всех кандидатов"""
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_all_candidates():
    candidates = load_candidates_from_json()
    return candidates


def get_candidate_by_id(candidate_id):
    """возвращает одного кандидата по его id"""
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """Возвращает кандидатов по имени"""
    candidates = load_candidates_from_json()
    candidates_found = []

    for candidate in candidates:
        if candidate_name in candidate.get("name"):
            candidates_found.append(candidate)
    return candidates_found


def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""
    skill_name = skill_name.lower()
    candidates = load_candidates_from_json()
    candidates_found = []

    for candidate in candidates:
        skills = candidate.get("skills")
        list_candidates = skills.lower().split(", ")
        if skill_name in list_candidates:
            candidates_found.append(candidate)
    return candidates_found




#pp(get_candidates_by_name("Adela"))