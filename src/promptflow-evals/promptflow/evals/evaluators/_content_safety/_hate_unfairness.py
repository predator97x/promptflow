from pathlib import Path

from promptflow.client import load_flow

from .flow.constants import EvaluationMetrics


class HateUnfairnessEvaluator:
    def __init__(self, project_scope: dict, credential=None):
        """
        Initialize an evaluator for hate unfairness score.

        :param project_scope: The scope of the Azure AI project.
            It contains subscription id, resource group, and project name.
        :type project_scope: dict
        :param credential: The credential for connecting to Azure AI project.
        :type credential: TokenCredential

        **Usage**

        .. code-block:: python

            project_scope = {
                "subscription_id": "<subscription_id>",
                "resource_group_name": "<resource_group_name>",
                "project_name": "<project_name>",
            }
            eval_fn = HateUnfairnessEvaluator(project_scope)
            result = eval_fn(question="What is the capital of France?", answer="Paris.")
        """

        self._project_scope = project_scope
        self._credential = credential

        # Load the flow as function
        current_dir = Path(__file__).resolve().parent
        flow_dir = current_dir / "flow"
        self._flow = load_flow(source=flow_dir)

    def __call__(self, *, question: str, answer: str, **kwargs):
        """Evaluates hate unfairness content.

        :param question: The question to be evaluated.
        :type question: str
        :param answer: The answer to be evaluated.
        :type answer: str
        :return: The hate unfairness score.
        :rtype: dict
        """

        # Run the evaluation flow
        output = self._flow(
            metric_name=EvaluationMetrics.HATE_FAIRNESS,
            question=question,
            answer=answer,
            project_scope=self._project_scope,
            credential=self._credential,
        )

        return output["result"]
