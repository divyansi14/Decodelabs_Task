import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_dataset(csv_path):
    "D:\\DecodeLabs_Internship\\raw_skills.csv"
    df = pd.read_csv(csv_path)
    return df


def build_vectorizer(skills_series):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(skills_series)
    return vectorizer, tfidf_matrix


def get_user_skills():
    print("Enter your skills one at a time. Type 'done' when finished.")
    print("(You must enter at least 3 skills)\n")

    skills = []
    while True:
        skill = input(f"Skill {len(skills) + 1}: ").strip()

        if skill.lower() == "done":
            if len(skills) < 3:
                print(f"You've only entered {len(skills)} skill(s). "
                      f"Please enter at least 3 before typing 'done'.\n")
                continue
            break

        if skill:
            skills.append(skill)

    return " ".join(skills)


def vectorize_user_input(vectorizer, user_skills_string):
    user_vector = vectorizer.transform([user_skills_string])
    return user_vector


def compute_similarity_scores(user_vector, role_vectors):
    scores = cosine_similarity(user_vector, role_vectors)
    return scores.flatten()  # shape (1, 20) -> (20,)


def get_top_n_recommendations(df, scores, n=3):
    results = list(zip(df["role"], scores))
    results.sort(key=lambda pair: pair[1], reverse=True)
    return results[:n]


if __name__ == "__main__":
    # Step 1: Ingestion - load the dataset
    df = load_dataset("raw_skills.csv")
    print(f"Loaded {len(df)} job roles from raw_skills.csv\n")
    print(df.head(), "\n")

    # Step 2 (part 1): Vectorize the dataset's skills column
    vectorizer, role_vectors = build_vectorizer(df["skills"])

    print(f"Vocabulary size (unique skill terms): {len(vectorizer.vocabulary_)}")
    print(f"TF-IDF matrix shape: {role_vectors.shape}")
    print(f"  -> {role_vectors.shape[0]} roles x {role_vectors.shape[1]} unique skill terms\n")

    print("Sample of learned vocabulary:")
    sample_terms = list(vectorizer.vocabulary_.keys())[:10]
    print(sample_terms)

    # Step 1 (Ingestion): get the user's skills
    print("\n" + "=" * 50)
    user_skills_string = get_user_skills()
    print(f"\nCaptured skills: {user_skills_string}")

    # Step 2: vectorize the user's input into the same space
    user_vector = vectorize_user_input(vectorizer, user_skills_string)
    print(f"User vector shape: {user_vector.shape}")
    print(f"Non-zero terms matched in vocabulary: {user_vector.nnz}")

    # Step 2 (Scoring): cosine similarity against every role
    scores = compute_similarity_scores(user_vector, role_vectors)
    print("\nRaw similarity scores (unsorted, in dataset order):")
    for role_name, score in zip(df["role"], scores):
        print(f"  {role_name:<30} {score:.4f}")

    # Steps 3 & 4 (Sorting + Filtering): Top-3 recommendations
    top_matches = get_top_n_recommendations(df, scores, n=3)
    print("\n" + "=" * 50)
    print("TOP 3 RECOMMENDED CAREER PATHS")
    print("=" * 50)
    for rank, (role_name, score) in enumerate(top_matches, start=1):
        match_pct = score * 100
        print(f"{rank}. {role_name} — {match_pct:.1f}% match")