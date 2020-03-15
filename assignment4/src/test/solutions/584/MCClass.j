.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a Z from Label0 to Label1
.var 2 is b Z from Label0 to Label1
.var 3 is c Z from Label0 to Label1
.var 4 is d Z from Label0 to Label1
	iconst_1
	istore_2
	iconst_0
	istore_3
	iconst_0
	istore 4
	iload_2
	iload_3
	ior
	iload 4
	ior
	istore_1
	iload_1
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 15
.limit locals 5
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
