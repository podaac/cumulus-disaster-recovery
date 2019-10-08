"""
Name: test_requests_postgres.py

Description:  Unit tests for requests.py that hit a postgres db running in docker.
"""

import os
import time
import unittest
from unittest.mock import Mock

import requests
from requests import create_data
from requests import result_to_json
import db_config
#from request_helpers import print_rows

UTC_NOW_EXP_1 = requests.get_utc_now_iso()
time.sleep(1)
REQUEST_ID_EXP_1 = requests.request_id_generator()
UTC_NOW_EXP_2 = requests.get_utc_now_iso()
time.sleep(1)
REQUEST_ID_EXP_2 = requests.request_id_generator()
UTC_NOW_EXP_3 = requests.get_utc_now_iso()
time.sleep(1)
UTC_NOW_EXP_4 = requests.get_utc_now_iso()
time.sleep(1)
REQUEST_ID_EXP_3 = requests.request_id_generator()
UTC_NOW_EXP_5 = requests.get_utc_now_iso()
time.sleep(1)
UTC_NOW_EXP_6 = requests.get_utc_now_iso()
time.sleep(1)
REQUEST_ID_EXP_4 = requests.request_id_generator()
UTC_NOW_EXP_7 = requests.get_utc_now_iso()
time.sleep(1)
UTC_NOW_EXP_8 = requests.get_utc_now_iso()
time.sleep(1)
REQUEST_ID_EXP_5 = requests.request_id_generator()
UTC_NOW_EXP_9 = requests.get_utc_now_iso()
time.sleep(1)
REQUEST_ID_EXP_6 = requests.request_id_generator()
UTC_NOW_EXP_10 = requests.get_utc_now_iso()
time.sleep(1)
UTC_NOW_EXP_11 = requests.get_utc_now_iso()

class TestRequestsPostgres(unittest.TestCase): #pylint: disable-msg=too-many-instance-attributes
    """
    TestRequestFiles.
    """


    def setUp(self):

        prefix = "lab"
        os.environ["PREFIX"] = prefix
        db_config.set_env()

        self.job_id_1 = None
        self.job_id_2 = None
        self.job_id_3 = None
        self.job_id_4 = None
        self.job_id_5 = None
        self.job_id_6 = None
        self.job_id_7 = None
        self.job_id_8 = None
        self.job_id_9 = None
        self.job_id_10 = None
        self.job_id_11 = None

        self.mock_utcnow = requests.get_utc_now_iso
        self.mock_request_id = requests.request_id_generator


    def tearDown(self):
        requests.request_id_generator = self.mock_request_id
        requests.get_utc_now_iso = self.mock_utcnow
        try:
            requests.delete_all_requests()
        except requests.NotFound:
            pass
        except requests.DatabaseError:
            pass

        del os.environ["PREFIX"]
        del os.environ["DATABASE_HOST"]
        del os.environ["DATABASE_NAME"]
        del os.environ["DATABASE_USER"]
        del os.environ["DATABASE_PW"]

    def create_test_requests(self):   #pylint: disable-msg=too-many-statements
        """
        creates jobs in the db
        """
        requests.get_utc_now_iso = Mock(side_effect=[UTC_NOW_EXP_1, UTC_NOW_EXP_4,
                                                     UTC_NOW_EXP_2, UTC_NOW_EXP_5,
                                                     UTC_NOW_EXP_3, UTC_NOW_EXP_6,
                                                     UTC_NOW_EXP_4, UTC_NOW_EXP_4,
                                                     UTC_NOW_EXP_5, UTC_NOW_EXP_5,
                                                     UTC_NOW_EXP_6, UTC_NOW_EXP_6,
                                                     UTC_NOW_EXP_7, UTC_NOW_EXP_7,
                                                     UTC_NOW_EXP_8, UTC_NOW_EXP_8,
                                                     UTC_NOW_EXP_9, UTC_NOW_EXP_9,
                                                     UTC_NOW_EXP_10, UTC_NOW_EXP_10,
                                                     UTC_NOW_EXP_11, UTC_NOW_EXP_11])
        requests.request_id_generator = Mock(side_effect=[REQUEST_ID_EXP_1,
                                                          REQUEST_ID_EXP_2,
                                                          REQUEST_ID_EXP_3,
                                                          REQUEST_ID_EXP_4,
                                                          REQUEST_ID_EXP_5,
                                                          REQUEST_ID_EXP_6])
        obj = {}
        try:
            obj["request_id"] = REQUEST_ID_EXP_1
            obj["granule_id"] = "granule_1"
            obj["key"] = "objectkey_1"
            obj["glacier_bucket"] = "my_s3_bucket"
            data = create_data(obj, "restore",
                               "complete", UTC_NOW_EXP_1, UTC_NOW_EXP_4)
            self.job_id_1 = requests.submit_request(data)

            obj["request_id"] = REQUEST_ID_EXP_1
            obj["granule_id"] = "granule_2"
            obj["key"] = "objectkey_2"
            data = create_data(obj, "restore",
                               "complete", UTC_NOW_EXP_2, UTC_NOW_EXP_5)
            self.job_id_2 = requests.submit_request(data)

            obj["request_id"] = REQUEST_ID_EXP_1
            obj["granule_id"] = "granule_3"
            obj["key"] = "objectkey_3"
            data = create_data(obj, "restore",
                               "complete", UTC_NOW_EXP_3, UTC_NOW_EXP_6)
            self.job_id_3 = requests.submit_request(data)

            obj["request_id"] = REQUEST_ID_EXP_2
            obj["granule_id"] = "granule_4"
            obj["key"] = "objectkey_4"
            data = create_data(obj, "restore",
                               "error", UTC_NOW_EXP_4, None, "oh oh, an error happened")
            self.job_id_4 = requests.submit_request(data)

            obj["request_id"] = REQUEST_ID_EXP_3
            obj["granule_id"] = "granule_5"
            obj["key"] = "objectkey_5"
            data = create_data(obj, "restore",
                               "inprogress", UTC_NOW_EXP_5, UTC_NOW_EXP_5)
            self.job_id_5 = requests.submit_request(data)

            obj["request_id"] = REQUEST_ID_EXP_3
            obj["granule_id"] = "granule_6"
            obj["key"] = "objectkey_6"
            data = create_data(obj, "restore",
                               "inprogress", UTC_NOW_EXP_6, UTC_NOW_EXP_6)
            self.job_id_6 = requests.submit_request(data)

            obj["request_id"] = REQUEST_ID_EXP_4
            obj["granule_id"] = "granule_4"
            obj["key"] = "objectkey_4"
            data = create_data(obj, "restore",
                               "inprogress", UTC_NOW_EXP_7, UTC_NOW_EXP_7)
            self.job_id_7 = requests.submit_request(data)

            obj["request_id"] = REQUEST_ID_EXP_5
            obj["granule_id"] = "granule_1"
            obj["key"] = "objectkey_1"
            data = create_data(obj, "restore",
                               "inprogress", UTC_NOW_EXP_8, UTC_NOW_EXP_8)
            self.job_id_8 = requests.submit_request(data)

            obj["request_id"] = REQUEST_ID_EXP_5
            obj["granule_id"] = "granule_2"
            obj["key"] = "objectkey_2"
            data = create_data(obj, "restore",
                               "inprogress", UTC_NOW_EXP_9, UTC_NOW_EXP_9)
            self.job_id_9 = requests.submit_request(data)

            obj["request_id"] = REQUEST_ID_EXP_5
            obj["granule_id"] = "granule_3"
            obj["key"] = "objectkey_3"
            data = create_data(obj, "restore",
                               "inprogress", UTC_NOW_EXP_10, UTC_NOW_EXP_10)
            self.job_id_10 = requests.submit_request(data)

            obj["request_id"] = REQUEST_ID_EXP_6
            obj["granule_id"] = "granule_7"
            obj["key"] = "objectkey_7"
            obj["glacier_bucket"] = None
            data = create_data(obj, "regenerate",
                               "inprogress", UTC_NOW_EXP_11, UTC_NOW_EXP_11)
            self.job_id_11 = requests.submit_request(data)

            results = requests.get_all_requests()
            return results
        except requests.DatabaseError as err:
            self.fail(f"submit_request. {str(err)}")


    def test_submit_request_inprogress_status(self):
        """
        Tests that a job is written to the db
        """
        self.create_test_requests()
        utc_now_exp = "2019-07-31 18:05:19.161362+00:00"
        request_id_exp = "0000a0a0-a000-00a0-00a0-0000a0000000"
        requests.get_utc_now_iso = Mock(return_value=utc_now_exp)
        requests.request_id_generator = Mock(return_value=request_id_exp)

        data = {}
        data["request_id"] = requests.request_id_generator()
        data["granule_id"] = "granule_1"
        data["object_key"] = "thisisanobjectkey"
        data["job_type"] = "restore"
        data["restore_bucket_dest"] = "my_s3_bucket"
        data["job_status"] = "inprogress"
        data["request_time"] = utc_now_exp
        try:
            job_id = requests.submit_request(data)
            self.assertGreater(job_id, 0, "job_id should be greater than 0")
        except requests.DatabaseError as err:
            self.fail(f"submit_request. {str(err)}")

        try:
            result = requests.get_job_by_job_id(job_id)
            result[0].pop("job_id")
            data["last_update_time"] = utc_now_exp
            self.assertEqual(data, result[0])
        except requests.DatabaseError as err:
            self.fail(f"get_job_by_job_id. {str(err)}")

    def test_submit_request_error_status(self):
        """
        Tests that a job is written to the db
        """
        self.create_test_requests()
        utc_now_exp = "2019-07-31 18:05:19.161362+00:00"
        request_id_exp = "0000a0a0-a000-00a0-00a0-0000a0000000"
        requests.get_utc_now_iso = Mock(return_value=utc_now_exp)
        requests.request_id_generator = Mock(return_value=request_id_exp)

        data = {}
        data["err_msg"] = "restore request error message here"
        data["request_id"] = requests.request_id_generator()
        data["granule_id"] = "granule_1"
        data["object_key"] = "thisisanobjectkey"
        data["job_type"] = "restore"
        data["restore_bucket_dest"] = "my_s3_bucket"
        data["job_status"] = "error"
        data["request_time"] = utc_now_exp

        try:
            job_id = requests.submit_request(data)
            self.assertGreater(job_id, 0, "job_id should be greater than 0")
        except requests.DatabaseError as err:
            self.fail(f"submit_request. {str(err)}")

        try:
            result = requests.get_job_by_job_id(job_id)
            result[0].pop("job_id")
            data["last_update_time"] = utc_now_exp
            self.assertEqual(data, result[0])
        except requests.DatabaseError as err:
            self.fail(f"get_job_by_job_id. {str(err)}")


    def test_update_request_status_for_job_inprogress(self):
        """
        Tests updating an 'error' job to an 'inprogress' status
        """
        self.create_test_requests()
        #print_rows("begin")
        #utc_now_exp = "2019-07-31 21:07:15.234362+00:00"
        utc_now_exp = requests.get_utc_now_iso()
        requests.get_utc_now_iso = Mock(return_value=utc_now_exp)
        job_id = self.job_id_4
        job_status = "inprogress"
        try:
            result = requests.update_request_status_for_job(job_id, job_status)
            #print_rows("end")
            self.assertEqual([], result)
            row = requests.get_job_by_job_id(job_id)
            self.assertEqual(job_status, row[0]["job_status"])
            self.assertEqual(None, row[0]["err_msg"])

        except requests.DatabaseError as err:
            self.fail(f"update_request_status_for_job. {str(err)}")

    def test_update_request_status_for_job_error(self):
        """
        Tests updating an inprogress job to an 'error' status
        """
        self.create_test_requests()
        job_id = self.job_id_8
        row = requests.get_job_by_job_id(job_id)
        self.assertEqual("inprogress", row[0]["job_status"])
        #print_rows("begin")
        utc_now_exp = "2019-07-31 21:07:15.234362+00:00"
        requests.get_utc_now_iso = Mock(return_value=utc_now_exp)
        job_status = "error"
        err_msg = "oh no an error"
        #exp_result = []
        try:
            result = requests.update_request_status_for_job(job_id, job_status, err_msg)
            #print_rows("end")
            self.assertEqual([], result)
            row = requests.get_job_by_job_id(job_id)
            self.assertEqual(job_status, row[0]["job_status"])
            self.assertEqual(err_msg, row[0]["err_msg"])
            self.assertIn(utc_now_exp, row[0]["last_update_time"])
        except requests.DatabaseError as err:
            self.fail(f"update_request_status_for_job. {str(err)}")

    def test_update_request_status_complete(self):
        """
        Tests updating a job to a 'complete' status
        """
        self.create_test_requests()
        utc_now_exp = "2019-07-31 21:07:15.234362+00:00"
        requests.get_utc_now_iso = Mock(return_value=utc_now_exp)
        object_key = "thisisanobjectkey"
        old_status = "inprogress"
        job_status = "complete"
        try:
            result = requests.update_request_status(object_key, old_status, job_status)
            self.assertEqual([], result)
        except requests.DatabaseError as err:
            self.fail(f"update_request_status. {str(err)}")

    def test_update_request_status_error(self):
        """
        Tests updating a job to a 'error' status
        """
        self.create_test_requests()
        utc_now_exp = "2019-07-31 19:21:38.263364+00:00"
        requests.get_utc_now_iso = Mock(return_value=utc_now_exp)
        object_key = "objectkey_5"
        granule_id = "granule_5"
        old_status = "inprogress"
        job_status = "error"
        err_msg = "copy error msg goes here"
        try:
            result = requests.update_request_status(object_key, old_status, job_status, err_msg)
            self.assertEqual([], result)
        except requests.DatabaseError as err:
            self.fail(f"update_request_status. {str(err)}")
        result = requests.get_jobs_by_granule_id(granule_id)
        self.assertEqual(err_msg, result[0]["err_msg"])


    def test_get_all_requests(self):
        """
        Tests reading all requests
        """
        qresult = self.create_test_requests()
        expected = result_to_json(qresult)
        result = requests.get_all_requests()
        self.assertEqual(expected, result)

    def test_get_jobs_by_status(self):
        """
        Tests reading by status
        """
        self.create_test_requests()
        status = "noexist"
        result = requests.get_jobs_by_status(status)
        self.assertEqual([], result)

        status = "complete"
        result = requests.get_jobs_by_status(status)
        exp_ids = [self.job_id_1, self.job_id_2, self.job_id_3]
        idx = 0
        for job in result:
            self.assertEqual(exp_ids[idx], job["job_id"])
            idx = idx + 1


    def test_get_jobs_by_status_max_days(self):
        """
        Tests reading by status
        """
        self.create_test_requests()
        status = "noexist"
        result = requests.get_jobs_by_status(status)
        self.assertEqual([], result)

        status = "complete"
        result = requests.get_jobs_by_status(status, 5)
        exp_ids = [self.job_id_1, self.job_id_2, self.job_id_3]
        idx = 0
        print(" ")
        print("exp_ids: ", exp_ids)
        print(" ")
        for job in result:
            print("Job: ", job)
            self.assertEqual(exp_ids[idx], job["job_id"])
            idx = idx + 1
        print(" ")


    def test_delete_request(self):
        """
        Tests deleting a job by job_id
        """
        try:
            self.create_test_requests()
            result = requests.delete_request(self.job_id_1)
            self.assertEqual([], result)
        except requests.DatabaseError as err:
            self.fail(f"delete_request. {str(err)}")


    def test_delete_all_requests(self):
        """
        Tests deleting all requests from the request_status table
        """
        try:
            self.create_test_requests()
            result = requests.delete_all_requests()
            self.assertEqual([], result)
        except requests.DatabaseError as err:
            self.fail(f"delete_all_requests. {str(err)}")