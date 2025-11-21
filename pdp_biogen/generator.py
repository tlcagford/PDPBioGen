import json
from openai import OpenAI, APIError, RateLimitError
from .config import Config

class BiographyGenerator:
    """Generate professional biographies using OpenAI."""
    
    def __init__(self):
        self.config = Config()
        self.client = OpenAI(api_key=self.config.api_key)
    
    def generate(self, name, role, institution, expertise, style="academic", **kwargs):
        """Generate a biography based on input parameters."""
        
        prompt = self._build_prompt(name, role, institution, expertise, style)
        
        try:
            response = self.client.chat.completions.create(
                model=self.config.default_model,
                messages=[
                    {
                        "role": "system", 
                        "content": "You are a professional biography writer specializing in academic and corporate profiles."
                    },
                    {"role": "user", "content": prompt}
                ],
                max_tokens=self.config.max_tokens,
                temperature=self.config.temperature
            )
            
            return response.choices[0].message.content.strip()
            
        except RateLimitError:
            raise Exception("Rate limit exceeded. Please wait before making more requests.")
        except APIError as e:
            raise Exception(f"OpenAI API error: {e}")
        except Exception as e:
            raise Exception(f"Unexpected error: {e}")
    
    def _build_prompt(self, name, role, institution, expertise, style):
        """Build a tailored prompt based on style."""
        
        prompts = {
            "academic": f"""
Write a professional academic biography for {name}, a {role} at {institution}. 
Their expertise includes {expertise}. 

Please include:
- Their professional background and current role
- Key research interests and expertise  
- Academic achievements and contributions
- Professional narrative in third person

Write in a formal, scholarly tone appropriate for university profiles.
            """,
            
            "corporate": f"""
Write a professional corporate biography for {name}, the {role} at {institution}.
Their expertise includes {expertise}.

Please include:
- Professional background and current position
- Key skills and areas of expertise
- Career achievements and accomplishments
- Business-focused narrative

Write in a professional, business-appropriate tone.
            """,
            
            "short": f"""
Write a concise professional bio for {name}, {role} at {institution}.
Expertise: {expertise}.

Keep it brief (2-3 sentences), impactful, and professional.
            """
        }
        
        return prompts.get(style, prompts["academic"]).strip()
