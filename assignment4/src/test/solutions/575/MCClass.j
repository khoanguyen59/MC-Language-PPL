.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [I from Label0 to Label1
	iconst_5
	newarray int
	astore_1
.var 2 is b [I from Label0 to Label1
	iconst_5
	newarray int
	astore_2
	aload_1
	iconst_4
	iconst_4
	isub
	bipush 76
	iastore
	aload_1
	astore_2
	aload_2
	iconst_4
	iconst_3
	isub
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 7
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
