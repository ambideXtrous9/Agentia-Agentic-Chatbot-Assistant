def extract_answer(full_response):
    """Extract the content after **Answer:** in the response"""
    if not isinstance(full_response, str):
        return str(full_response)
    
    answer_markers = ["**Answer:**", "Answer:", "**Answer**:"]
    for marker in answer_markers:
        if marker in full_response:
            parts = full_response.split(marker, 1)
            if len(parts) > 1:
                return parts[1].strip()
    return full_response.strip()