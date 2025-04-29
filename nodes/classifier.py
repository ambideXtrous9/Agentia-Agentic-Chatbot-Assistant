def classify_input(input_data):
    # Define complete greeting phrases (must match exactly)
    greeting_phrases = [
        "hello", "hi", "hey", 
        "good morning", "good evening", 
        "how are you", "what's up"
    ]
    
    # Define trigger phrases for other categories
    coder_phrases = [
        "write code", "code for", "algorithm",
        "programming", "python code", "function to"
    ]
    
    news_phrases = [
        "news about", "latest on", "current events", "latest news",
        "breaking news", "updates on", "news headlines",
        "news today", "news articles", "news stories",
        "news updates", "news report", "news summary", "latest", "news",
        "headlines for", "recent updates"
    ]
    
    
    processed_input = input_data.lower().strip()
    
    # Check for news requests
    if any(phrase in processed_input for phrase in news_phrases):
        return "duck_search"
    
    # Check for code requests
    if any(phrase in processed_input for phrase in coder_phrases):
        return "code"
    
    # Check for exact greeting matches first
    if any(f" {phrase} " in f" {processed_input} " for phrase in greeting_phrases):
        return "greeting"
    
    return "general_query"