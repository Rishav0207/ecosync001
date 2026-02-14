# recommender.py
def recommend(alerts):
    recs = []

    for a in alerts:
        if "Dry soil" in a:
            recs.append(a + " → Irrigate this zone")
        if "High pollution" in a:
            recs.append(a + " → Check pollution source")
        if "Low water" in a:
            recs.append(a + " → Inspect tank or pipes")

    return recs
