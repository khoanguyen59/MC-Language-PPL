.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is temp I from Label0 to Label1
	iconst_4
	istore_1
	bipush 6
	istore_2
	iload_1
	istore_3
	iload_2
	istore_1
	iload_3
	istore_2
	iload_2
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 11
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
