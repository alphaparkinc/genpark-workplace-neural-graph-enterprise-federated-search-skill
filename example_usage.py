from client import WorkplaceNeuralGraphEnterpriseFederatedSearchClient

def main():
    client = WorkplaceNeuralGraphEnterpriseFederatedSearchClient()
    res = client.federated_knowledge_search('Onboarding setup guide for distributed microservices')
    print('Search ID: ' + res['search_id'] + ' (Latency: ' + str(res['search_latency_ms']) + 'ms)')
    print('Sources: ' + ', '.join(res['connected_datasources_searched']))
    print('Top Doc: ' + res['top_cited_document_uri'] + ' (Author: ' + res['neural_expert_author_identified'] + ')')

if __name__ == '__main__':
    main()
