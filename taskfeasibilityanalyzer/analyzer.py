from projectstructor.detector import ProjectStructureDetector
from gptintegration import GPTIntegration  # Make sure this import points to your GPTIntegration module

class TaskFeasibilityAnalyzer:
    def __init__(self, directory, openai_api_key, model="gpt-3.5-turbo", max_tokens=5):
        self.detector = ProjectStructureDetector(directory, openai_api_key)
        self.gpt_integration = GPTIntegration(openai_api_key, model=model, max_tokens=max_tokens)  # Initialize GPTIntegration

    def analyze_task(self, task_description):
        # Detect the structure of the project and languages used
        project_structure = self.detector.detect_structure(ignore_gitignore=True)
        project_languages = self.detector.detect_languages()

        # Build the prompt for GPT
        system_message = self._build_system_message(project_structure, project_languages)
        user_message = self._build_user_message(task_description)

        # Query GPT through GPTIntegration module
        response = self.gpt_integration.query_gpt(system_message, user_message)

        # Extract the probability from the response
        probability = self._interpret_response(response.choices[0].message.content.strip())
        return probability

    def _build_system_message(self, project_structure, project_languages):
        # Construct a system message with project details and strict response format rules
        return f"""The system will analyze the given task description based on the project's file structure and technology stack. Provide only a numerical estimate of the probability that the task can be completed successfully without further clarification. The response must strictly be a single number between 0 and 1, inclusive, where 1 represents absolute certainty of success and 0 represents impossibility.

    Project Structure:
    {project_structure}

    Project Languages:
    {project_languages}

    Strict format for response: A single floating-point number between 0 and 1 (e.g., 0.75, 0.9, 0.45). Avoid any additional text or commentary."""

    def _build_user_message(self, task_description):
        # Construct the user message with the task description
        return f"Please assess the feasibility of the following task based on the project's details provided above:\n\nTask Description: {task_description}\n\nRespond with only a numerical probability as instructed."

    def _interpret_response(self, response_text):
        # Convert the response text to a floating-point number
        try:
            print(response_text)
            probability = float(response_text)
            return max(0.0, min(probability, 1.0))  # Ensure it's within [0, 1]
        except ValueError:
            raise ValueError(f"Received invalid response from GPT-3: {response_text}")

# Usage example
# analyzer = TaskFeasibilityAnalyzer('/path/to/your/project', 'your-openai-api-key')
# probability = analyzer.analyze_task("Refactor the database schema to improve performance.")
# print(probability)
