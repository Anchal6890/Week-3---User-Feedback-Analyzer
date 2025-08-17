import json
import matplotlib.pyplot as plt
import os

DATA_FILE = "data/feedback.json"
OUTPUT_FILE = "output/sentiment_chart.png"

os.makedirs("data", exist_ok=True)
os.makedirs("output", exist_ok=True)

def load_feedback():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_feedback(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def analyze_sentiment(feedback):
    positive_words = ["good", "love", "excellent", "great", "satisfied", "useful"]
    negative_words = ["bad", "terrible", "poor", "slow", "hate", "problem"]

    f = feedback.lower()
    if any(word in f for word in positive_words):
        return "Positive"
    elif any(word in f for word in negative_words):
        return "Negative"
    else:
        return "Neutral"

def generate_chart(feedback_list):
    results = {"Positive": 0, "Negative": 0, "Neutral": 0}
    for f in feedback_list:
        sentiment = analyze_sentiment(f)
        results[sentiment] += 1

    plt.bar(results.keys(), results.values(), color=["green", "red", "blue"])
    plt.title("Sentiment Analysis of Feedback")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.savefig(OUTPUT_FILE)
    plt.show()
    print(f"✅ Chart saved as {OUTPUT_FILE}")

def menu():
    feedback_list = load_feedback()
    while True:
        print("\n=== Feedback Analyzer Menu ===")
        print("1. Add New Feedback")
        print("2. View All Feedback")
        print("3. Analyze Feedback & Generate Chart")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            new_feedback = input("Enter your feedback: ")
            feedback_list.append(new_feedback)
            save_feedback(feedback_list)
            print("✅ Feedback saved successfully!")
        elif choice == "2":
            if feedback_list:
                print("\nAll Feedback:")
                for i, f in enumerate(feedback_list, start=1):
                    print(f"{i}. {f}")
            else:
                print("⚠️ No feedback available.")
        elif choice == "3":
            if feedback_list:
                print("\nSentiment Analysis Results:")
                for f in feedback_list:
                    print(f"{f} → {analyze_sentiment(f)}")
                generate_chart(feedback_list)
            else:
                print("⚠️ No feedback to analyze.")
        elif choice == "4":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    menu()
