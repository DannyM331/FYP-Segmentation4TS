def calculate_coverage_score(true_cps, detected_cps, tolerance):
    # Initialize counters
    true_positive = 0
    false_positive = 0

    # Create a set to keep track of matched detected change points
    matched_detected_cps = set()

    # Check for true positives and match detected change points
    for true_cp in true_cps:
        nearest_detected_cp = min(detected_cps, key=lambda x: abs(x - true_cp))
        if abs(nearest_detected_cp - true_cp) <= tolerance:
            true_positive += 1
            matched_detected_cps.add(nearest_detected_cp)

    # Count false positives
    for detected_cp in detected_cps:
        if detected_cp not in matched_detected_cps:
            false_positive += 1

    # Calculate precision and recall
    precision = true_positive / (true_positive + false_positive) if detected_cps else 0
    recall = true_positive / len(true_cps) if true_cps else 0

    # Calculate F1 score as the harmonic mean of precision and recall
    if precision + recall == 0:
        return 0
    else:
        return 2 * (precision * recall) / (precision + recall)