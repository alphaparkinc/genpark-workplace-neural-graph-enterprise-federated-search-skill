class WorkplaceNeuralGraphEnterpriseFederatedSearchClient:
    def federated_knowledge_search(self, user_query='Where is the latest SOC2 Type II audit report for our EMEA database?', user_permission_roles=None):
        user_permission_roles = user_permission_roles or ['ROLE_ENGINEERING', 'ROLE_SECURITY_AUDITOR']
        return {
            'search_id': 'gln_src_9918',
            'query': user_query,
            'connected_datasources_searched': ['Google_Drive', 'Confluence_Wiki', 'Jira_Enterprise', 'Slack_Archives', 'GitHub_Org'],
            'top_cited_document_uri': 'https://drive.google.com/corp/sec/2026_SOC2_Type2_EMEA_Final.pdf',
            'acl_permission_filtering_verified': True,
            'neural_expert_author_identified': 'Dr. Marcus Vance (Head of Information Security)',
            'search_latency_ms': 115
        }
