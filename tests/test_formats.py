"""Malformed tables, literal preservation and the bounded native data path."""
import importlib.util
from pathlib import Path
import struct
import unittest

ROOT=Path(__file__).resolve().parents[1]
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path);obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj
FORMATS=module('formats','tools/t8_formats.py')
TOKENS=module('tokens','tools/recovered_tokens.py')
NATIVE=module('native','src/native/scalar_append_model.py')

class Formats(unittest.TestCase):
    def fixture(self):
        b=bytearray(180);b[:8]=bytes.fromhex('804753430d0a0036')
        struct.pack_into('<H',b,0x1e,1);struct.pack_into('<I',b,0x20,92);struct.pack_into('<I',b,0x54,4);struct.pack_into('<I',b,0x30,100)
        struct.pack_into('<5IBBH',b,100,123,92,1,2,3,0,0x86,0);return b
    def test_export_role_is_data_not_missing_function_count(self):
        v=FORMATS.tables(self.fixture());self.assertEqual(0x86,v['exports'][0]['flags']);self.assertEqual(92,v['exports'][0]['address'])
    def test_truncated_and_wrong_revision_rejected(self):
        for data in [b'',bytes(100),self.fixture()[:110]]:
            with self.assertRaises(ValueError):FORMATS.tables(data)
    def test_import_address_outside_buffer_rejected(self):
        b=self.fixture();struct.pack_into('<H',b,0x28,1);struct.pack_into('<I',b,0x38,130);struct.pack_into('<IIHBBI',b,130,1,2,1,0,0,9999)
        with self.assertRaises(ValueError):FORMATS.tables(b)
    def test_literal_regressions(self):
        self.assertTrue(TOKENS.challenge_cases()['passed'])

class NativeModel(unittest.TestCase):
    def environment(self,top=4096,limit=5000,scalar=50,guard=0,count=3):
        memory={0x1cf8458:scalar,0x3bff850:guard,0x3bf7038:top,0x3bf7028:limit,0x3bff84c:count};events=[]
        def read(width,address):events.append(('read',width,address));return memory[address]
        def write(width,address,value):events.append(('write',width,address,value));memory[address]=value
        return memory,events,read,write
    def test_signed_payload_count_wrap_and_write_order(self):
        m,e,r,w=self.environment(scalar=0xffffffff,count=0xffffffff);self.assertEqual(4096,NATIVE.run(r,w,lambda *_:self.fail('unexpected opaque')))
        self.assertEqual((1<<64)-1,m[4112]);self.assertEqual(0,m[0x3bff84c]);self.assertEqual([0x3bf7038,0x3bff84c,4120,4112],[x[2] for x in e if x[0]=='write'])
    def test_opaque_call_may_change_memory_and_rbx(self):
        m,e,r,w=self.environment(guard=1)
        def opaque(rva,edi,rbx):self.assertEqual(0xaaca70,rva);m[0x3bf7038]=8192;m[0x3bf7028]=9999;return -9
        self.assertEqual(8192,NATIVE.run(r,w,opaque));self.assertEqual(((1<<64)-9),m[8208])
    def test_equal_limit_calls_error_then_traps_without_wrapper_writes(self):
        m,e,r,w=self.environment(top=5000);calls=[]
        with self.assertRaises(NATIVE.NativeTrap):NATIVE.run(r,w,lambda *args:calls.append(args))
        self.assertEqual(0x14f2dd0,calls[0][0]);self.assertFalse(any(x[0]=='write' for x in e))
    def test_greater_than_limit_is_not_a_guard(self):
        m,e,r,w=self.environment(top=6000);self.assertEqual(6000,NATIVE.run(r,w,lambda *_:None))
    def test_fault_retains_prior_write(self):
        m,e,r,w=self.environment()
        def fault(width,address,value):
            if address==0x3bff84c:raise RuntimeError('fixture fault')
            w(width,address,value)
        with self.assertRaises(RuntimeError):NATIVE.run(r,fault,lambda *_:None)
        self.assertEqual(4112,m[0x3bf7038]);self.assertNotIn(4120,m)

if __name__=='__main__':unittest.main()
