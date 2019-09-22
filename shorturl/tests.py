from django.test import TestCase
import json


class MainTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_can_query_known_url_entry(self):
        # setup: creating a new short url entry
        response = self.client.post('/graphql/', {'query': '''
            mutation {
                addUrlEntry(value: "http://testme123.com") {
                    urlEntry { 
                        shortId 
                        value 
                    }
                }
            }
        '''})
        response_json = json.loads(response.content)
        generated_short_id = response_json["data"]["addUrlEntry"]["urlEntry"]["shortId"]

        # act: query created entry using graphql endpoint
        response = self.client.get('/graphql/', {'query': '''
            query {
                url(shortId: "''' + generated_short_id + '''") {
                    shortId
                    value
                }
            }
        '''})

        # verify
        response_json = json.loads(response.content)
        self.assertEqual(response.status_code, 200)

        response_url_value = response_json['data']['url']['value']
        self.assertEqual(response_url_value, 'http://testme123.com')

        response_short_id = response_json['data']['url']['shortId']
        self.assertEqual(response_short_id, generated_short_id)

    def test_redirects_for_known_short_id(self):
        # setup: creating a new short url entry
        response = self.client.post('/graphql/', {'query': '''
            mutation {
                addUrlEntry(value: "http://testme.com") {
                    urlEntry { 
                        shortId 
                        value 
                    }
                }
            }
        '''})
        response_json = json.loads(response.content)
        short_id = response_json["data"]["addUrlEntry"]["urlEntry"]["shortId"]

        # act
        response = self.client.get(f'/{short_id}')

        # verify: redirects user to expected URL
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, 'http://testme.com')

    def test_displays_error_message_for_unknown_short_id(self):
        # act
        response = self.client.get('/jhgjhgjgiuih')

        # verify
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'was not found', response.content)
