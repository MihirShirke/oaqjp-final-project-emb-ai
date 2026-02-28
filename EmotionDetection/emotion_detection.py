def emotion_detector(text_to_analyze):

    if not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Simulated response (Mocked Watson Output)
    emotions = {
        "anger": 0.89 if "angry" in text_to_analyze.lower() else 0.01,
        "disgust": 0.02,
        "fear": 0.03,
        "joy": 0.05 if "happy" in text_to_analyze.lower() else 0.02,
        "sadness": 0.01
    }

    dominant_emotion = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant_emotion

    return emotions