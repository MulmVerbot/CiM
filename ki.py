import openai

openai.api_key = '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'

# Ersetzen Sie "text-davinci-003" durch ein aktuelles Modell, z.B. "gpt-3.5-turbo" oder, wenn verfügbar, ein GPT-4-Modell
response = openai.Completion.create(
  model="gpt-4",  # Beispiel für ein aktuelles Modell
  prompt="Das ist ein Test.",
  max_tokens=50
)

print(response.choices[0].text.strip())

