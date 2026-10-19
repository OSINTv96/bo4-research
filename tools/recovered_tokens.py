"""Compare literal token streams, ignoring only comments and whitespace.

This does not rename identifiers, evaluate constants, rewrite branches or claim
that recovered text faithfully represents the original VM behavior.
"""
from pathlib import Path
import hashlib
import json
import re

RUN=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
NAME=re.compile(r'[A-Za-z_][A-Za-z_0-9]*')
NUMBER=re.compile(r'(?:0[xX][0-9a-fA-F]+(?:\.[0-9a-fA-F]*)?(?:[pP][+-]?[0-9]+)?|(?:[0-9]+(?:\.(?!\.)[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?)')
LONG=re.compile(r'\[(=*)\[')

def tokens(text,language):
    if language not in ('lua','gsc'):raise ValueError('Unknown language')
    out=[];i=0
    def long_end(at):
        m=LONG.match(text,at)
        if not m:return None
        end=text.find(']'+m[1]+']',m.end())
        if end<0:raise ValueError('Unclosed long string or comment')
        return end+len(m[1])+2
    while i<len(text):
        c=text[i]
        if c.isspace():i+=1;continue
        if language=='lua' and text.startswith('--',i):
            end=long_end(i+2)
            if end is None:
                match=re.search(r'[\r\n]',text[i+2:]);end=i+2+match.start() if match else -1
                if end<0:end=len(text)
            i=end;continue
        if language=='gsc' and text.startswith('//',i):
            match=re.search(r'[\r\n]',text[i+2:]);end=i+2+match.start() if match else -1;i=len(text) if end<0 else end;continue
        if language=='gsc' and text.startswith('/*',i):
            end=text.find('*/',i+2)
            if end<0:raise ValueError('Unclosed block comment')
            i=end+2;continue
        if c in ('"',"'"):
            start=i;i+=1;closed=False
            while i<len(text):
                if text[i]=='\\':i+=2;continue
                if text[i]==c:i+=1;closed=True;break
                i+=1
            if not closed:raise ValueError('Unclosed quoted string')
            out.append(('string',text[start:i]));continue
        if language=='lua' and c=='[':
            end=long_end(i)
            if end is not None:out.append(('long-string',text[i:end]));i=end;continue
        m=NAME.match(text,i)
        if m:out.append(('name',m[0]));i=m.end();continue
        m=NUMBER.match(text,i)
        if m:out.append(('number',m[0]));i=m.end();continue
        punctuation = ('...','==','~=','<=','>=','::','..','//','<<','>>') if language=='lua' else ('>>=','<<=','...','===','!==','->','=>','??','?.','**','&=','|=','^=','%=','[[',']]','/#','#/','==','~=','!=','<=','>=','::','..','&&','||','++','--','+=','-=','*=','/=','<<','>>')
        punct=next((p for p in punctuation if text.startswith(p,i)),c)
        out.append(('symbol',punct));i+=len(punct)
    return out

def digest(ts):return sha(json.dumps(ts,separators=(',',':'),ensure_ascii=True).encode())

def challenge_cases():
    equal=[('lua','return "-- keep" -- remove\n','return "-- keep"'),
           ('lua','a=1 --[[ @ 0]]\nb=2','a = 1\n b = 2'),
           ('lua','--[=[ comment ]] stays comment ]=]\nreturn [==[-- literal]==]','return [==[-- literal]==]'),
           ('lua','x="quote \\\" -- literal" -- comment','x = "quote \\\" -- literal"'),
           ('gsc','return "https://x/*y*/"; // comment','return "https://x/*y*/";'),
           ('gsc','a/* comment */+b','a + b')]
    different=[('lua','return false','return 0'),('lua','return 0x1','return 1'),('lua','not x','notx'),
               ('lua','x and y','x or y'),('lua','x="a b"','x="ab"'),('lua','x=[=[a -- b]=]','x=[=[a b]=]'),
               ('lua','f(a,b)','f(b,a)'),('gsc','if(a) b();','if(!a) b();'),('gsc','return 8;','return false;'),
               ('gsc','f(x);','f(y);'),('gsc','a < = b','a <= b'),('lua','x=1 .. 2','x=1.2')]
    equal += [('lua','a=1 -- comment\rb=2','a=1 b=2'), ('gsc','a=1; // comment\rb=2;','a=1; b=2;')]
    different += [(lang,'x="a\rb"','x="a\nb"') for lang in ('lua','gsc')]
    different += [('lua','x=[=[a\r\nb]=]','x=[=[a\nb]=]'), ('gsc','a->b','a- >b'), ('gsc','x>>=1','x> >=1'), ('gsc','/# x(); #/','/ # x(); # /')]
    equal += [('lua','x=a[b[c]]','x=a[b[c] ]'), ('lua','x=a[b[c]]','x=a[b[c]--comment\n]'), ('lua','x=a[b[c[d]]]','x=a[b[c[d] ] ]')]
    for language,a,b in equal:assert tokens(a,language)==tokens(b,language)
    for language,a,b in different:assert tokens(a,language)!=tokens(b,language)
    bad=[('lua','--[=[never closed'),('lua','"not closed'),('gsc','/* no close')]
    for language,s in bad:
        try:tokens(s,language)
        except ValueError:pass
        else:raise AssertionError('Malformed literal/comment accepted')
    return dict(equal_cases=len(equal),distinct_cases=len(different),malformed_cases=len(bad),passed=True)
