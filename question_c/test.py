import os
import json
import unittest
import main as question_c


class TestQuestionC(unittest.TestCase):
    
    def test_must_read_config_file(self):
        filename = "config.json"
        if not os.path.isfile(filename):
            config = {"api_key": "abc", "cse_id": "789"}
            with open(filename, "w") as f:
                f.write(json.dumps(config))
        _key, _id = question_c.__load_config__()
        self.assertIsNotNone(_key)
        self.assertIsNotNone(_id)
    
    
    def test_must_check_results_length(self):
        # Actualy this tests is an integration test,
        # not an unit tests. It should be refactored
        # in the same way the fuction it tests should

        res = question_c.__google_search__("teste")
        self.assertTrue(len(res) == 5)
        
    def test_must_check_result_data(self):
        k, v = "undesiredKey", "useless"
        data= { "link":["link"], "snippet": ["snippet"], "htmlSnippet": ["htmlSnippet"] }
        data[k] = v
        res = question_c.__format_data__(data)
        self.assertNotIn(k, res.keys())
        

        
    