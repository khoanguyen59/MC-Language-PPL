.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_0
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_2
	iconst_1
	if_icmple Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label7
	iconst_3
	iconst_2
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
	iconst_4
	iconst_3
	if_icmple Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label13
	iconst_5
	iconst_4
	if_icmple Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
	bipush 6
	iconst_5
	if_icmple Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label19
	invokestatic io/putLn()V
Label19:
Label16:
Label13:
Label10:
Label7:
Label4:
Label1:
	return
.limit stack 13
.limit locals 1
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
