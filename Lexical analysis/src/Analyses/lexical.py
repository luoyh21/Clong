from antlr4 import *
from antlr.clongParser import clongParser
from antlr.clongVisitor import clongVisitor
from antlr.clongLexer import clongLexer

def analyse(filename):
    """
    将输入的文件进行词法分析，得到token流
    Args:
        filename: 输入的文件名
    """
    lexer = clongLexer(FileStream(filename))
    stream = CommonTokenStream(lexer)
    parser=clongParser(stream)
    tree = parser.prog()
    for token in stream.tokens:
        print("Len:{0}, Type:{1}, Text:{2}".format(
            len(token.text), "EOF" if token.type<0 
            else parser.literalNames[token.type] if token.type < len(parser.literalNames) 
            else parser.symbolicNames[token.type], token.text
        ))