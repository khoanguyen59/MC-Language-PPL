.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main()I
Label0:
.var 0 is a Z from Label0 to Label1
.var 1 is b Z from Label0 to Label1
.var 2 is c Z from Label0 to Label1
.var 3 is d Z from Label0 to Label1
.var 4 is e Z from Label0 to Label1
	iconst_1
	istore_0
	iconst_0
	istore_1
	iload_0
	iload_1
	iand
	istore_2
	iload_0
	iload_1
	ior
	iload_2
	ior
	istore_3
	iload_0
	iload_1
	iand
	iload_2
	iand
	istore 4
	iload_0
	iload_1
	iload_2
	iand
	ior
	iload_3
	iload 4
	iand
	ior
	ireturn
Label1:
.limit stack 17
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
