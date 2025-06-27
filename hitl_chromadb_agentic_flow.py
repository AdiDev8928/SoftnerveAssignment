from typing import List
import google.generativeai as genai
import chromadb
from datetime import datetime
import os
import random

#Api key 
genai.configure(api_key="AIzaSyCa0so4Fz28UXLsM3OQa7bD2B4h_m30nYs")

#Human in the iteration loop function
def hitl_loop(file_path="spun_chapter.txt"):
    roles = ["writer", "reviewer", "editor"]
    for role in roles:
        print(f"\n{role.capitalize()}'s Turn to Review: Opening file...")
        os.system(f"notepad {file_path}" if os.name == "nt" else f"xdg-open {file_path}")
        input(f"Press Enter after the {role} has finished editing...")
    print("\nHITL process complete.")


class Agent:
    def __init__(self, name, prompt):
        self.name = name
        self.prompt = prompt
        self.model = genai.GenerativeModel("gemma-3n-e2b-it")

    def process(self, text):
        response = self.model.generate_content(f"{self.prompt}\n\n{text}")
        return response.text

def run_agentic_pipeline(text):
    agents = [
        Agent("DraftingAgent", "Write a clear and concise modern version of this chapter."),
        Agent("StyleAgent", "Improve the tone and style to make it more engaging."),
        Agent("ComplianceAgent", "Ensure the content adheres to academic integrity and ethical standards."),
    ]
    for agent in agents:
        text = agent.process(text)
        print(f"[{agent.name}] processing complete.")
    return text

#ChromaDB data Storage
client = chromadb.Client()
collection = client.get_or_create_collection("chapters")

def save_version(chapter_id, content, metadata=None):
    timestamp = datetime.now().isoformat()
    collection.add(
        documents=[content],
        ids=[f"{chapter_id}_{timestamp}"],
        metadatas=[metadata or {"version": timestamp}]
    )
    print(f"Saved version: {chapter_id}_{timestamp}")

#RL Search
def compute_reward(version_text):
    """ Dummy reward function — replace with real feedback or scoring logic. """
    reward = 0
    if "concise" in version_text.lower():
        reward += 0.5
    if "academic" in version_text.lower():
        reward += 0.5
    return reward

def rl_select_best_version(query, versions, epsilon=0.1):
    """ Epsilon-greedy RL-based version selector """
    if random.random() < epsilon:
        return random.choice(versions)
    else:
        scored = [(v, compute_reward(v)) for v in versions]
        return max(scored, key=lambda x: x[1])[0]

def retrieve_best_version(query, top_k=5):
    results = collection.query(query_texts=[query], n_results=top_k)
    docs = [doc[0] for doc in results["documents"]] if results["documents"] else []
    if not docs:
        return "No match found."
    best = rl_select_best_version(query, docs)
    return best


if __name__ == "__main__":
    
    with open("chapter1.txt", "r", encoding="utf-8") as f:
        original = f.read()

    #Running the agents
    ai_output = run_agentic_pipeline(original)

    save_version("chapter1", ai_output, {"stage": "AI Draft"})

    with open("spun_chapter.txt", "w", encoding="utf-8") as f:
        f.write(ai_output)

    #Human in the iteration loop
    hitl_loop("spun_chapter.txt")

    #Save final version
    with open("spun_chapter.txt", "r", encoding="utf-8") as f:
        final_content = f.read()
    save_version("chapter1", final_content, {"stage": "Final Human-Approved"})

    #Retrieve using RL retrieval
    query = input("Enter a search phrase to retrieve best version (e.g., 'concise academic version'): ")
    best_version = retrieve_best_version(query)

    print("\nBest matching version (RL-selected):\n")
    print(best_version)
