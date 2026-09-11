import os
import pytest
from unittest.mock import MagicMock, patch
from src.llm_service import LLMService

def test_mock_mode_generation():
    
    service = LLMService(mode="mock")
    context = "Sample policy outlines rules. It provides clarity."
    answer = service.generate_answer("What is this?", context)
    assert answer == "Sample policy outlines rules. It provides clarity."

def test_insufficient_context_handling():
   
    service_mock = LLMService(mode="mock")
    assert service_mock.generate_answer("Question", "   ") == "The available document context is insufficient to answer this question."

    with patch.dict(os.environ, {"GEMINI_API_KEY": "fake_key"}):
        with patch("google.genai.Client"):
            service_gemini = LLMService(mode="gemini")
            assert service_gemini.generate_answer("Question", "") == "The available document context is insufficient to answer this question."

def test_missing_api_key_raises_error():
    
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError, match="Missing GEMINI_API_KEY"):
            LLMService(mode="gemini")

@patch("google.genai.Client")
def test_gemini_mode_successful_generation(mock_client_cls):
   
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.text = "  Grounded LLM Answer.  "
    mock_client.models.generate_content.return_value = mock_response
    mock_client_cls.return_value = mock_client

    with patch.dict(os.environ, {"GEMINI_API_KEY": "fake_key"}):
        service = LLMService(mode="gemini")
        answer = service.generate_answer("What is policy?", "Policy outlines rules.")
        
        assert answer == "Grounded LLM Answer."
        mock_client.models.generate_content.assert_called_once()

@patch("google.genai.Client")
def test_gemini_api_failure_handling(mock_client_cls):
    
    mock_client = MagicMock()
    mock_client.models.generate_content.side_effect = Exception("404 NOT_FOUND")
    mock_client_cls.return_value = mock_client

    with patch.dict(os.environ, {"GEMINI_API_KEY": "fake_key"}):
        service = LLMService(mode="gemini")
        answer = service.generate_answer("What is policy?", "Policy outlines rules.")
        
        assert "Error communicating with LLM Provider" in answer
        assert "404 NOT_FOUND" in answer
