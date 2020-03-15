# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0183\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\3\2\6\2o\n\2\r\2\16\2p\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\7\3y\n\3\f\3\16\3|\13\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u0087\n\4\f\4\16\4\u008a")
        buf.write("\13\4\3\4\3\4\3\5\6\5\u008f\n\5\r\5\16\5\u0090\3\6\6\6")
        buf.write("\u0094\n\6\r\6\16\6\u0095\3\6\3\6\7\6\u009a\n\6\f\6\16")
        buf.write("\6\u009d\13\6\3\6\5\6\u00a0\n\6\3\6\3\6\6\6\u00a4\n\6")
        buf.write("\r\6\16\6\u00a5\3\6\5\6\u00a9\n\6\3\6\6\6\u00ac\n\6\r")
        buf.write("\6\16\6\u00ad\3\6\5\6\u00b1\n\6\3\7\3\7\5\7\u00b5\n\7")
        buf.write("\3\7\6\7\u00b8\n\7\r\7\16\7\u00b9\3\b\3\b\5\b\u00be\n")
        buf.write("\b\3\t\3\t\3\t\7\t\u00c3\n\t\f\t\16\t\u00c6\13\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3")
        buf.write("&\3&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\7*\u014a\n*\f*\16*\u014d")
        buf.write("\13*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\64\7\64\u0166")
        buf.write("\n\64\f\64\16\64\u0169\13\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\7\65\u0174\n\65\f\65\16\65\u0177")
        buf.write("\13\65\3\65\3\65\5\65\u017b\n\65\3\65\3\65\3\66\5\66\u0180")
        buf.write("\n\66\3\66\3\66\4z\u0167\2\67\3\3\5\4\7\5\t\6\13\7\r\2")
        buf.write("\17\b\21\t\23\2\25\2\27\n\31\13\33\f\35\r\37\16!\17#\20")
        buf.write("%\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67\329\33")
        buf.write(";\34=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60")
        buf.write("e\61g\62i\63k\64\3\2\f\5\2\13\f\17\17\"\"\4\2\f\f\17\17")
        buf.write("\3\2\62;\4\2GGgg\6\2\n\f\16\17$$^^\t\2$$^^ddhhppttvv\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\4\2$$^^\3\2^^\2\u0197\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\3n\3\2\2\2\5t")
        buf.write("\3\2\2\2\7\u0082\3\2\2\2\t\u008e\3\2\2\2\13\u00b0\3\2")
        buf.write("\2\2\r\u00b2\3\2\2\2\17\u00bd\3\2\2\2\21\u00bf\3\2\2\2")
        buf.write("\23\u00ca\3\2\2\2\25\u00cc\3\2\2\2\27\u00cf\3\2\2\2\31")
        buf.write("\u00d7\3\2\2\2\33\u00dd\3\2\2\2\35\u00e6\3\2\2\2\37\u00eb")
        buf.write("\3\2\2\2!\u00ef\3\2\2\2#\u00f5\3\2\2\2%\u00f8\3\2\2\2")
        buf.write("\'\u00fc\3\2\2\2)\u0103\3\2\2\2+\u0108\3\2\2\2-\u010b")
        buf.write("\3\2\2\2/\u0111\3\2\2\2\61\u0116\3\2\2\2\63\u011c\3\2")
        buf.write("\2\2\65\u0123\3\2\2\2\67\u0125\3\2\2\29\u0127\3\2\2\2")
        buf.write(";\u0129\3\2\2\2=\u012b\3\2\2\2?\u012d\3\2\2\2A\u012f\3")
        buf.write("\2\2\2C\u0132\3\2\2\2E\u0135\3\2\2\2G\u0138\3\2\2\2I\u013b")
        buf.write("\3\2\2\2K\u013d\3\2\2\2M\u0140\3\2\2\2O\u0142\3\2\2\2")
        buf.write("Q\u0145\3\2\2\2S\u0147\3\2\2\2U\u014e\3\2\2\2W\u0150\3")
        buf.write("\2\2\2Y\u0152\3\2\2\2[\u0154\3\2\2\2]\u0156\3\2\2\2_\u0158")
        buf.write("\3\2\2\2a\u015a\3\2\2\2c\u015c\3\2\2\2e\u015e\3\2\2\2")
        buf.write("g\u0161\3\2\2\2i\u016f\3\2\2\2k\u017f\3\2\2\2mo\t\2\2")
        buf.write("\2nm\3\2\2\2op\3\2\2\2pn\3\2\2\2pq\3\2\2\2qr\3\2\2\2r")
        buf.write("s\b\2\2\2s\4\3\2\2\2tu\7\61\2\2uv\7,\2\2vz\3\2\2\2wy\13")
        buf.write("\2\2\2xw\3\2\2\2y|\3\2\2\2z{\3\2\2\2zx\3\2\2\2{}\3\2\2")
        buf.write("\2|z\3\2\2\2}~\7,\2\2~\177\7\61\2\2\177\u0080\3\2\2\2")
        buf.write("\u0080\u0081\b\3\2\2\u0081\6\3\2\2\2\u0082\u0083\7\61")
        buf.write("\2\2\u0083\u0084\7\61\2\2\u0084\u0088\3\2\2\2\u0085\u0087")
        buf.write("\n\3\2\2\u0086\u0085\3\2\2\2\u0087\u008a\3\2\2\2\u0088")
        buf.write("\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008b\3\2\2\2")
        buf.write("\u008a\u0088\3\2\2\2\u008b\u008c\b\4\2\2\u008c\b\3\2\2")
        buf.write("\2\u008d\u008f\t\4\2\2\u008e\u008d\3\2\2\2\u008f\u0090")
        buf.write("\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091")
        buf.write("\n\3\2\2\2\u0092\u0094\t\4\2\2\u0093\u0092\3\2\2\2\u0094")
        buf.write("\u0095\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2")
        buf.write("\u0096\u0097\3\2\2\2\u0097\u009b\7\60\2\2\u0098\u009a")
        buf.write("\t\4\2\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b")
        buf.write("\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009f\3\2\2\2")
        buf.write("\u009d\u009b\3\2\2\2\u009e\u00a0\5\r\7\2\u009f\u009e\3")
        buf.write("\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00b1\3\2\2\2\u00a1\u00a3")
        buf.write("\7\60\2\2\u00a2\u00a4\t\4\2\2\u00a3\u00a2\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2")
        buf.write("\u00a6\u00a8\3\2\2\2\u00a7\u00a9\5\r\7\2\u00a8\u00a7\3")
        buf.write("\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00b1\3\2\2\2\u00aa\u00ac")
        buf.write("\t\4\2\2\u00ab\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad")
        buf.write("\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\3\2\2\2")
        buf.write("\u00af\u00b1\5\r\7\2\u00b0\u0093\3\2\2\2\u00b0\u00a1\3")
        buf.write("\2\2\2\u00b0\u00ab\3\2\2\2\u00b1\f\3\2\2\2\u00b2\u00b4")
        buf.write("\t\5\2\2\u00b3\u00b5\7/\2\2\u00b4\u00b3\3\2\2\2\u00b4")
        buf.write("\u00b5\3\2\2\2\u00b5\u00b7\3\2\2\2\u00b6\u00b8\t\4\2\2")
        buf.write("\u00b7\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00b7\3")
        buf.write("\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\16\3\2\2\2\u00bb\u00be")
        buf.write("\5/\30\2\u00bc\u00be\5\61\31\2\u00bd\u00bb\3\2\2\2\u00bd")
        buf.write("\u00bc\3\2\2\2\u00be\20\3\2\2\2\u00bf\u00c4\7$\2\2\u00c0")
        buf.write("\u00c3\5\23\n\2\u00c1\u00c3\5\25\13\2\u00c2\u00c0\3\2")
        buf.write("\2\2\u00c2\u00c1\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2")
        buf.write("\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c7\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c7\u00c8\7$\2\2\u00c8\u00c9\b\t\3\2")
        buf.write("\u00c9\22\3\2\2\2\u00ca\u00cb\n\6\2\2\u00cb\24\3\2\2\2")
        buf.write("\u00cc\u00cd\7^\2\2\u00cd\u00ce\t\7\2\2\u00ce\26\3\2\2")
        buf.write("\2\u00cf\u00d0\7d\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2\7")
        buf.write("q\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5")
        buf.write("\7c\2\2\u00d5\u00d6\7p\2\2\u00d6\30\3\2\2\2\u00d7\u00d8")
        buf.write("\7d\2\2\u00d8\u00d9\7t\2\2\u00d9\u00da\7g\2\2\u00da\u00db")
        buf.write("\7c\2\2\u00db\u00dc\7m\2\2\u00dc\32\3\2\2\2\u00dd\u00de")
        buf.write("\7e\2\2\u00de\u00df\7q\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1")
        buf.write("\7v\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4")
        buf.write("\7w\2\2\u00e4\u00e5\7g\2\2\u00e5\34\3\2\2\2\u00e6\u00e7")
        buf.write("\7g\2\2\u00e7\u00e8\7n\2\2\u00e8\u00e9\7u\2\2\u00e9\u00ea")
        buf.write("\7g\2\2\u00ea\36\3\2\2\2\u00eb\u00ec\7h\2\2\u00ec\u00ed")
        buf.write("\7q\2\2\u00ed\u00ee\7t\2\2\u00ee \3\2\2\2\u00ef\u00f0")
        buf.write("\7h\2\2\u00f0\u00f1\7n\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3")
        buf.write("\7c\2\2\u00f3\u00f4\7v\2\2\u00f4\"\3\2\2\2\u00f5\u00f6")
        buf.write("\7k\2\2\u00f6\u00f7\7h\2\2\u00f7$\3\2\2\2\u00f8\u00f9")
        buf.write("\7k\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb\7v\2\2\u00fb&\3")
        buf.write("\2\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff")
        buf.write("\7v\2\2\u00ff\u0100\7w\2\2\u0100\u0101\7t\2\2\u0101\u0102")
        buf.write("\7p\2\2\u0102(\3\2\2\2\u0103\u0104\7x\2\2\u0104\u0105")
        buf.write("\7q\2\2\u0105\u0106\7k\2\2\u0106\u0107\7f\2\2\u0107*\3")
        buf.write("\2\2\2\u0108\u0109\7f\2\2\u0109\u010a\7q\2\2\u010a,\3")
        buf.write("\2\2\2\u010b\u010c\7y\2\2\u010c\u010d\7j\2\2\u010d\u010e")
        buf.write("\7k\2\2\u010e\u010f\7n\2\2\u010f\u0110\7g\2\2\u0110.\3")
        buf.write("\2\2\2\u0111\u0112\7v\2\2\u0112\u0113\7t\2\2\u0113\u0114")
        buf.write("\7w\2\2\u0114\u0115\7g\2\2\u0115\60\3\2\2\2\u0116\u0117")
        buf.write("\7h\2\2\u0117\u0118\7c\2\2\u0118\u0119\7n\2\2\u0119\u011a")
        buf.write("\7u\2\2\u011a\u011b\7g\2\2\u011b\62\3\2\2\2\u011c\u011d")
        buf.write("\7u\2\2\u011d\u011e\7v\2\2\u011e\u011f\7t\2\2\u011f\u0120")
        buf.write("\7k\2\2\u0120\u0121\7p\2\2\u0121\u0122\7i\2\2\u0122\64")
        buf.write("\3\2\2\2\u0123\u0124\7-\2\2\u0124\66\3\2\2\2\u0125\u0126")
        buf.write("\7/\2\2\u01268\3\2\2\2\u0127\u0128\7,\2\2\u0128:\3\2\2")
        buf.write("\2\u0129\u012a\7\61\2\2\u012a<\3\2\2\2\u012b\u012c\7\'")
        buf.write("\2\2\u012c>\3\2\2\2\u012d\u012e\7#\2\2\u012e@\3\2\2\2")
        buf.write("\u012f\u0130\7~\2\2\u0130\u0131\7~\2\2\u0131B\3\2\2\2")
        buf.write("\u0132\u0133\7(\2\2\u0133\u0134\7(\2\2\u0134D\3\2\2\2")
        buf.write("\u0135\u0136\7?\2\2\u0136\u0137\7?\2\2\u0137F\3\2\2\2")
        buf.write("\u0138\u0139\7#\2\2\u0139\u013a\7?\2\2\u013aH\3\2\2\2")
        buf.write("\u013b\u013c\7>\2\2\u013cJ\3\2\2\2\u013d\u013e\7>\2\2")
        buf.write("\u013e\u013f\7?\2\2\u013fL\3\2\2\2\u0140\u0141\7@\2\2")
        buf.write("\u0141N\3\2\2\2\u0142\u0143\7@\2\2\u0143\u0144\7?\2\2")
        buf.write("\u0144P\3\2\2\2\u0145\u0146\7?\2\2\u0146R\3\2\2\2\u0147")
        buf.write("\u014b\t\b\2\2\u0148\u014a\t\t\2\2\u0149\u0148\3\2\2\2")
        buf.write("\u014a\u014d\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c\3")
        buf.write("\2\2\2\u014cT\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u014f")
        buf.write("\7*\2\2\u014fV\3\2\2\2\u0150\u0151\7+\2\2\u0151X\3\2\2")
        buf.write("\2\u0152\u0153\7}\2\2\u0153Z\3\2\2\2\u0154\u0155\7\177")
        buf.write("\2\2\u0155\\\3\2\2\2\u0156\u0157\7]\2\2\u0157^\3\2\2\2")
        buf.write("\u0158\u0159\7_\2\2\u0159`\3\2\2\2\u015a\u015b\7=\2\2")
        buf.write("\u015bb\3\2\2\2\u015c\u015d\7.\2\2\u015dd\3\2\2\2\u015e")
        buf.write("\u015f\13\2\2\2\u015f\u0160\b\63\4\2\u0160f\3\2\2\2\u0161")
        buf.write("\u0167\7$\2\2\u0162\u0163\7^\2\2\u0163\u0166\t\7\2\2\u0164")
        buf.write("\u0166\n\n\2\2\u0165\u0162\3\2\2\2\u0165\u0164\3\2\2\2")
        buf.write("\u0166\u0169\3\2\2\2\u0167\u0168\3\2\2\2\u0167\u0165\3")
        buf.write("\2\2\2\u0168\u016a\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016b")
        buf.write("\t\13\2\2\u016b\u016c\n\7\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("\u016e\b\64\5\2\u016eh\3\2\2\2\u016f\u0175\7$\2\2\u0170")
        buf.write("\u0171\7^\2\2\u0171\u0174\t\7\2\2\u0172\u0174\n\6\2\2")
        buf.write("\u0173\u0170\3\2\2\2\u0173\u0172\3\2\2\2\u0174\u0177\3")
        buf.write("\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u017a")
        buf.write("\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u017b\5k\66\2\u0179")
        buf.write("\u017b\7\2\2\3\u017a\u0178\3\2\2\2\u017a\u0179\3\2\2\2")
        buf.write("\u017b\u017c\3\2\2\2\u017c\u017d\b\65\6\2\u017dj\3\2\2")
        buf.write("\2\u017e\u0180\7\17\2\2\u017f\u017e\3\2\2\2\u017f\u0180")
        buf.write("\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0182\7\f\2\2\u0182")
        buf.write("l\3\2\2\2\32\2pz\u0088\u0090\u0095\u009b\u009f\u00a5\u00a8")
        buf.write("\u00ad\u00b0\u00b4\u00b9\u00bd\u00c2\u00c4\u014b\u0165")
        buf.write("\u0167\u0173\u0175\u017a\u017f\7\b\2\2\3\t\2\3\63\3\3")
        buf.write("\64\4\3\65\5")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    BLOCK_COMMENT = 2
    LINE_COMMENT = 3
    INTLIT = 4
    FLOATLIT = 5
    BOOLEANLIT = 6
    STRINGLIT = 7
    BOOLEAN = 8
    BREAK = 9
    CONTINUE = 10
    ELSE = 11
    FOR = 12
    FLOAT = 13
    IF = 14
    INT = 15
    RETURN = 16
    VOID = 17
    DO = 18
    WHILE = 19
    TRUE = 20
    FALSE = 21
    STRING = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    NOT = 28
    OR = 29
    AND = 30
    EQ = 31
    NEQ = 32
    LT = 33
    LEQ = 34
    GT = 35
    GEQ = 36
    ASSIGN = 37
    ID = 38
    LB = 39
    RB = 40
    LP = 41
    RP = 42
    LS = 43
    RS = 44
    SEMI = 45
    COMMA = 46
    ERROR_CHAR = 47
    ILLEGAL_ESCAPE = 48
    UNCLOSE_STRING = 49
    NL = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'break'", "'continue'", "'else'", "'for'", "'float'", 
            "'if'", "'int'", "'return'", "'void'", "'do'", "'while'", "'true'", 
            "'false'", "'string'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
            "'||'", "'&&'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'='", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "WS", "BLOCK_COMMENT", "LINE_COMMENT", "INTLIT", "FLOATLIT", 
            "BOOLEANLIT", "STRINGLIT", "BOOLEAN", "BREAK", "CONTINUE", "ELSE", 
            "FOR", "FLOAT", "IF", "INT", "RETURN", "VOID", "DO", "WHILE", 
            "TRUE", "FALSE", "STRING", "ADD", "SUB", "MUL", "DIV", "MOD", 
            "NOT", "OR", "AND", "EQ", "NEQ", "LT", "LEQ", "GT", "GEQ", "ASSIGN", 
            "ID", "LB", "RB", "LP", "RP", "LS", "RS", "SEMI", "COMMA", "ERROR_CHAR", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "NL" ]

    ruleNames = [ "WS", "BLOCK_COMMENT", "LINE_COMMENT", "INTLIT", "FLOATLIT", 
                  "EXPONENT", "BOOLEANLIT", "STRINGLIT", "STRCHAR", "ESCSEQ", 
                  "BOOLEAN", "BREAK", "CONTINUE", "ELSE", "FOR", "FLOAT", 
                  "IF", "INT", "RETURN", "VOID", "DO", "WHILE", "TRUE", 
                  "FALSE", "STRING", "ADD", "SUB", "MUL", "DIV", "MOD", 
                  "NOT", "OR", "AND", "EQ", "NEQ", "LT", "LEQ", "GT", "GEQ", 
                  "ASSIGN", "ID", "LB", "RB", "LP", "RP", "LS", "RS", "SEMI", 
                  "COMMA", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "NL" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[7] = self.STRINGLIT_action 
            actions[49] = self.ERROR_CHAR_action 
            actions[50] = self.ILLEGAL_ESCAPE_action 
            actions[51] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    s = self.text[1:-1]
                    self.text = s
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    raise ErrorToken(self.text)
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    raise IllegalEscape(self.text[1:])
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    if self.text[-1]=='\n':
                        raise UncloseString(self.text[1:-2])
                    else:
                        raise UncloseString(self.text[1:])
                
     


