"""LLM provider abstract base class."""
from abc import ABC, abstractmethod

from llm_agent_toolkit.llm.types import LLMRequest, LLMResponse


class LLMProvider(ABC):
    @abstractmethod
    def complete(self, request: LLMRequest) -> LLMResponse:
        raise NotImplementedError
