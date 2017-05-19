#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'duyhsieh'

import traceback
import pymongo
import logging


class AccountManager(object):
    def __init__(self):
        logging.basicConfig()
        self.logger = logging.getLogger('SimpleLogger')
        self.logger.setLevel(logging.DEBUG)
        '''
        User DB

        Account {
            'account':
            'nickname':
            'serial':
        }

        SerialNumber {
            '_id': 0
            'counter' : 0
        }
        '''
        self.mongo = pymongo.MongoClient(host='mongo', port=27017)
        self.db = self.mongo['User']

        self.col_serial = self.db['SerialNumber']
        self.col_account = self.db['Account']
        self.col_account.create_index([ ('account',pymongo.ASCENDING) ],unique=True)

    def create_account(self,account, nickname=None):
        try:
            doc = self.col_serial.find_and_modify({'_id':'0'}, {'$inc':{'counter':1}},upsert=True,new=True) # override _id
            serial = '%08d' % doc['counter']

            name = nickname if nickname is not None and nickname != '' else account
            self.col_account.insert({'account':account, 'nickname':name, 'serial':serial })
            return True, {'account':account, 'nickname':name, 'serial':serial }
        except Exception as e:
            self.logger.error('create account error!{}'.format(traceback.format_exc()))
            return False, {'create account error':str(e)}
        
        return False, None

    def get_account(self,account):
        try:
            doc = self.col_account.find_one({'account':account}, {'_id':False})
            if doc is not None:
                return True, doc
        except Exception as e:
            self.logger.error('get account error!{}'.format(traceback.format_exc()))
            return False, {'get account error':str(e)}
        
        return False, {'get account error':'account not exist'}

    def patch_account(self, account, nickname):
        try:
            ret = self.col_account.update({'account':account},{'$set':{'nickname':nickname } } )
            if ret['updatedExisting'] is True:
                return True, {"patch account":"ok"}

        except Exception as e:
            self.logger.error('update account error!{}'.format(traceback.format_exc()))
            return False, {'patch account error':str(e)}
        
        return False, {'patch account error':'account not exist'}

    def delete_account(self, account):
        try:
            ret = self.col_account.remove({'account':account})
            if ret['n'] > 0:
                return True, {"delete account":"ok"}
        except Exception as e:
            self.logger.error('delete account error!{}'.format(traceback.format_exc()))
            return False, {'delete account error':str(e)}
    
        return False, {'delete account error':'account not exist'}
