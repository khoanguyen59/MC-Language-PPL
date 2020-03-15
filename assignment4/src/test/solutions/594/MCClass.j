.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo()V
.var 0 is a [F from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is y [F from Label0 to Label1
	bipush 10
	newarray float
	astore_1
.var 2 is z [I from Label0 to Label1
	bipush 10
	newarray int
	astore_2
	aload_1
	invokestatic MCClass/foo()V
	aload_2
	invokestatic MCClass/foo()V
Label1:
	return
.limit stack 2
.limit locals 3
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
