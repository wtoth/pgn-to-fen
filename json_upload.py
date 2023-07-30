import json

def create_json(path, fen):
    full_fen = []
    for fen_obj in fen:
        temp_fen = {}
        temp_fen["game_id"] = str(fen_obj.game_id)
        temp_fen["metadata"] = metadata_that_exists(fen_obj.metadata)
        #temp_fen["rank_file"] = fen_obj.rank_file
        temp_fen["game"] = fen_obj.game
        full_fen.append(temp_fen)
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(full_fen, f)

def metadata_that_exists(metadata):
    shortened_metadata = {}
    for key, val in metadata.items():
        if val is not (None or ""):
            shortened_metadata[key] = val
    return shortened_metadata
