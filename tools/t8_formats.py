"""Bounded T8 0x36 script table reader, authored by this project.

Layout reference: ACTS gsc_data_t8.hpp at 5d4d1ee6f7676f4529b99fc89c2382dde8b856b7.
Reading a table does not establish an export's engine role or invocation.
"""
import struct

def checked_region(data, offset, size):
    if offset < 0 or size < 0 or offset > len(data) or size > len(data)-offset:
        raise ValueError('Table exceeds saved buffer')
    return data[offset:offset+size]

def tables(data):
    checked_region(data,0,0x5c)
    if data[:8] != bytes.fromhex('804753430d0a0036'):
        raise ValueError('Not the assigned T8 PS4 0x36 format')
    u16=lambda off:struct.unpack_from('<H',data,off)[0]
    u32=lambda off:struct.unpack_from('<I',data,off)[0]
    code=(u32(0x20),u32(0x54));checked_region(data,*code)
    export_offset=u32(0x30);export_count=u16(0x1e)
    checked_region(data,export_offset,24*export_count)
    exports=[]
    for i in range(export_count):
        checksum,address,name,namespace,event,argc,flags,pad=struct.unpack_from('<5IBBH',data,export_offset+i*24)
        checked_region(data,address,1)
        exports.append(dict(index=i,offset=export_offset+i*24,checksum=checksum,address=address,name=f'{name:08x}',namespace=f'{namespace:08x}',event=f'{event:08x}',argc=argc,flags=flags,pad=pad))
    imports=[];at=u32(0x38)
    for i in range(u16(0x28)):
        checked_region(data,at,12)
        name,namespace,n,argc,flags=struct.unpack_from('<IIHBB',data,at)
        checked_region(data,at+12,n*4)
        addresses=list(struct.unpack_from('<'+'I'*n,data,at+12))
        for address in addresses:checked_region(data,address,1)
        imports.append(dict(index=i,offset=at,name=f'{name:08x}',namespace=f'{namespace:08x}',argc=argc,flags=flags,addresses=addresses))
        at+=12+4*n
    return {'code':code,'exports_offset':export_offset,'exports':exports,'imports_offset':u32(0x38),'imports_end':at,'imports':imports,'strings_offset':u32(0x24),'globals_offset':u32(0x44),'header_size':0x5c}
