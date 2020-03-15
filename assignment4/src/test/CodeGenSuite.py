import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Test case 1"""
        input = """void main() {
        putInt(100);
        }"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
        
    def test_int_ast(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("putInt"),[IntLiteral(5)])]))])
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,501))
        
    def test_bool(self):
        """Test case 3"""
        input = """void main() {
        putBool(true);
        }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,502))
        
    def test_string(self):
        """Test case 4"""
        input = """void main() {
        putString("Test case");
        }"""
        expect = "Test case"
        self.assertTrue(TestCodeGen.test(input,expect,503))
        
    def test_float(self):
        """Test case 5"""
        input = """void main() {
        putFloat(12.3);
        }"""
        expect = "12.3"
        self.assertTrue(TestCodeGen.test(input,expect,504))
        
    def test_float_exponent(self):
        """Test case 6"""
        input = """void main() {
        putFloat(12.1e3);
        }"""
        expect = "12100.0"
        self.assertTrue(TestCodeGen.test(input,expect,505))
        
    def test_float_negative_exponent(self):
        """Test case 7"""
        input = """void main() {
        putFloat(12.1e-3);
        }"""
        expect = "0.0121"
        self.assertTrue(TestCodeGen.test(input,expect,506))
        
    def test_builtin_func_putIntLn(self):
        """Test case 8"""
        input = """void main() {
        putIntLn(8);
        }"""
        expect = "8\n"
        self.assertTrue(TestCodeGen.test(input,expect,507))
        
    def test_builtin_func_putFloatLn(self):
        """Test case 9"""
        input = """void main() {
        putFloatLn(1.2345);
        }"""
        expect = "1.2345\n"
        self.assertTrue(TestCodeGen.test(input,expect,508))
        
    def test_builtin_func_putBoolLn(self):
        """Test case 10"""
        input = """void main() {
        putBoolLn(false);
        }"""
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,509))
        
    def test_builtin_func_putStringLn(self):
        """Test case 11"""
        input = """void main() {
        putStringLn("Test case 11");
        }"""
        expect = "Test case 11\n"
        self.assertTrue(TestCodeGen.test(input,expect,510))
        
    def test_builtin_func_putLn(self):
        """Test case 12"""
        input = """void main() {
        putLn();
        }"""
        expect = "\n"
        self.assertTrue(TestCodeGen.test(input,expect,511))
        
    def test_add_operator(self):
        """Test case 13"""
        input = """void main() {
        putIntLn(9 + 4); 
        return;
        }"""
        expect = "13\n"
        self.assertTrue(TestCodeGen.test(input,expect,512))
    
    def test_sub_operator(self):
        """Test case 14"""
        input = """void main() {
        putIntLn(9 - 4); 
        return;
        }"""
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input,expect,513))
        
    def test_sub_operator_on_float(self):
        """Test case 15"""
        input = """void main() {
        putFloatLn(9.5 - 4.78); 
        return;
        }"""
        expect = "4.72\n"
        self.assertTrue(TestCodeGen.test(input,expect,514))
        
    def test_sub_operator_type_coercion(self):
        """Test case 16"""
        input = """void main() {
        putFloatLn(100 - 1256.e-2); 
        return;
        }"""
        expect = "87.44\n"
        self.assertTrue(TestCodeGen.test(input,expect,515))
        
    def test_mul_operator(self):
        """Test case 17"""
        input = """void main() {
        putInt(13 * 4); 
        return;
        }"""
        expect = "52"
        self.assertTrue(TestCodeGen.test(input,expect,516))
        
    def test_mul_operator_on_float(self):
        """Test case 18"""
        input = """void main() {
        putFloat(6.9 * 9.6); 
        return;
        }"""
        expect = "66.240005"
        self.assertTrue(TestCodeGen.test(input,expect,517))

    def test_mul_operator_type_coercion(self):
        """Test case 19"""
        input = """void main() {
        putFloat(2.5 * 8); 
        return;
        }"""
        expect = "20.0"
        self.assertTrue(TestCodeGen.test(input,expect,518))

    def test_div_operator(self):
        """Test case 20"""
        input = """void main() {
        putInt(12 / 4); 
        return;
        }"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,519))
        
    def test_div_operator_on_float(self):
        """Test case 21"""
        input = """void main() {
        putFloat(6.9 / 1.15); 
        return;
        }"""
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input,expect,520))

    def test_mul_operator_type_coercion(self):
        """Test case 22"""
        input = """void main() {
        putFloat(8 / 2.5); 
        return;
        }"""
        expect = "3.2"
        self.assertTrue(TestCodeGen.test(input,expect,521)) 

    def test_div_operator_on_float_not_divisible(self):
        """Test case 23"""
        input = """void main() {
        putFloat(9.6 / 6.9); 
        return;
        }"""
        expect = "1.3913044"
        self.assertTrue(TestCodeGen.test(input,expect,522))      

    def test_mod_operator(self):
        """Test case 24"""
        input = """void main() {
        putInt(137 % 16); 
        return;
        }"""
        expect = "9"
        self.assertTrue(TestCodeGen.test(input,expect,523))

    def test_mod_operator_with_0(self):
        """Test case 25"""
        input = """void main() {
        putInt(137 % 0); 
        return;
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,524))        
    
    def test_cmplt_operator(self):
        """Test case 26"""
        input = """void main() {
        putBool(137 < 16); 
        return;
        }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,525))
        
    def test_cmpgt_operator(self):
        """Test case 27"""
        input = """void main() {
        putBool(27 > 16); 
        return;
        }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,526))
        
    def test_cmpge_operator(self):
        """Test case 28"""
        input = """void main() {
        putBool(16 >= 16); 
        return;
        }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,527))
        
    def test_cmple_operator(self):
        """Test case 29"""
        input = """void main() {
        putBool(16 <= 16); 
        return;
        }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,528))
        
    def test_eq_operator(self):
        """Test case 30"""
        input = """void main() {
        putBool(192 == 193); 
        return;
        }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,529))
        
    def test_neq_operator(self):
        """Test case 31"""
        input = """void main() {
        putBool(192 != 193); 
        return;
        }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,530))
        
    def test_compare_operator_on_float(self):
        """Test case 32"""
        input = """void main() {
        putBool(12.5000003 == 12.5); 
        return;
        }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,531))
        
    def test_compare_operator_on_bool(self):
        """Test case 33"""
        input = """void main() {
        putBool(true == false); 
        return;
        }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,532))
        
    def test_and_operator(self):
        """Test case 34"""
        input = """void main() {
        putBool(true && false); 
        return;
        }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,533))
        
    def test_or_operator(self):
        """Test case 35"""
        input = """void main() {
        putBool(true || false); 
        return;
        }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,534))
        
    def test_not_operator(self):
        """Test case 36"""
        input = """void main() {
        putBool(!(3>2)); 
        return;
        }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,535))   
        
    def test_sub_unary_operator(self):
        """Test case 37"""
        input = """void main() {
        putInt(-4); 
        return;
        }"""
        expect = "-4"
        self.assertTrue(TestCodeGen.test(input,expect,536))
        
    def test_assign_operator_int(self):
        """Test case 38"""
        input = """void main() {
        int a; 
        a = 3;
        putInt(a);
        return;
        }"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,537))
        
    def test_assign_operator_float(self):
        """Test case 39"""
        input = """void main() {
        float a; 
        a = 3; 
        putFloat(a); 
        return;
        }"""
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input,expect,538))
        
    def test_assign_operator_bool(self):
        """Test case 40"""
        input = """void main() {
        boolean isTrue; 
        isTrue = false; 
        putBool(isTrue); 
        return;
        }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,539))
        
    def test_assign_operator_string(self):
        """Test case 41"""
        input = """void main() {
        string str; 
        str = "Test case 41"; 
        putString(str); 
        return;
        }"""
        expect = "Test case 41"
        self.assertTrue(TestCodeGen.test(input,expect,540)) 
        
    def test_if_with_else(self):
        """Test case 42"""
        input = """int a; 
        void main() {
        int b; 
        if (3<2) 
            putInt(3); 
        else 
            putInt(2);
        }"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,541))
        
    def test_if_no_else(self):
        """Test case 43"""
        input = """void main() {
        if (2<3) 
        putInt(3);
        }"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,542))
    
    def test_nested_if_else(self):
        """Test case 44"""
        input = """int a; 
        void main() {
        a = 3; 
        int b; 
        b = 2; 
        if (a<b) {
            if (a == 3) 
                putInt(a);
        } 
        else 
            putInt(b);}"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,543))
        
    def test_return(self):
        """Test case 45"""
        input = """void main() {
        putInt(4); 
        return; 
        putInt(5);
        }"""
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,544))
        
    def test_return_primitive_type(self):
        """Test case 46"""
        input = """int foo() { 
        return 3; 
        }
        void main(){
        foo(); 
        putInt(46);
        }"""
        expect = "46"
        self.assertTrue(TestCodeGen.test(input,expect,545))
        
    def test_dowhile(self):
        """Test case 47"""
        input = """void main() {
        do 
            putInt(3); 
        while 
            3<2;
        }"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,546))
        
    def test_unsatisfied_dowhile_many_stmts(self):
        """Test case 48"""
        input = """void main() {
        do 
            putInt(3);  
            putFloat(4.5); 
        while 
            3<2;
        }"""
        expect = "34.5"
        self.assertTrue(TestCodeGen.test(input,expect,547))
        
    def test_satisfied_dowhile_many_stmts(self):
        """Test case 49"""
        input = """void main() {
        int i; 
        i = 1; 
        do 
            putInt(3);  
            putFloat(4.5); 
            i = i + 1; 
        while 
            i < 3;
        }"""
        expect = "34.534.5"
        self.assertTrue(TestCodeGen.test(input,expect,548))
        
    def test_nested_dowhile(self):
        """Test case 50"""
        input = """void main() {
        int i; 
        i = 1; 
        do 
            putInt(3);  
            do
                putString("negative");
            while 
                i < 0;
            i = i + 1; 
        while i < 3;
        }"""
        expect = "3negative3negative"
        self.assertTrue(TestCodeGen.test(input,expect,549))
    
    def test_for(self):
        """Test case 51"""
        input = """
        void main() {
        int i; 
        i = 0; 
        for (i; i < 4; i = i + 1)
            putInt(i);
        }"""
        expect = "0123"
        self.assertTrue(TestCodeGen.test(input,expect,550))
        
    def test_unsatisfied_for(self):
        """Test case 52"""
        input = """
        void main() {
        int i; 
        i = 0; 
        for (i; i < 0; i = i + 1){
            putInt(i);
        }
        putString("No Loop");
        }"""
        expect = "No Loop"
        self.assertTrue(TestCodeGen.test(input,expect,551))

    def test_nested_for(self):
        """Test case 53"""
        input = """
        void main() {
        int i; 
        int j;
        i = 0;
        j = 0;
        for (i; i < 3; i = i + 1){
            j = 0;
            for (j; j < i; j = j + 1)
                putInt(j);
        }
        }"""
        expect = "001012"
        self.assertTrue(TestCodeGen.test(input,expect,552)) 

    def test_break_in_dowhile(self):
        """Test case 54"""
        input = """void main() {
        do 
            break;
            putInt(3); 
        while 
            3<2;
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,553))    
    
    def test_break_in_dowhile_2(self):
        """Test case 55"""
        input = """void main() {
        do 
            putInt(3);
            break;
        while 
            3<2;
        }"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,554))
        
    def test_break_in_for(self):
        """Test case 56"""
        input = """
        void main() {
        int i; 
        i = 0; 
        for (i; i < 4; i = i + 1){
            break;
            putInt(i);
        }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,555))
    
    def test_break_in_for_2(self):
        """Test case 57"""
        input = """
        void main() {
        int i; 
        i = 0; 
        for (i; i < 4; i = i + 1){
            putInt(i);
            break;
        }
        }"""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,556))
        
    def test_for_loop_block(self):
        """Test case 58"""
        input = """
        void main() {
        int i; 
        i = 0; 
        for (i; i < 4; i = i + 1){
            putInt(i);
        }
        }"""
        expect = "0123"
        self.assertTrue(TestCodeGen.test(input,expect,557))
        
    def test_break_with_condition_in_for(self):
        """Test case 59"""
        input = """
        void main() {
        int i; 
        i = 0; 
        for (i; i < 5; i = i + 1){
            putInt(i);
            if (i == 3)
                break;
        }
        }"""
        expect = "0123"
        self.assertTrue(TestCodeGen.test(input,expect,558))
        
    def test_break_with_condition_in_dowhile(self):
        """Test case 60"""
        input = """void main() {
        int i;
        i = 0;
        do{
            i = i + 1;
            putInt(3);
            if (i > 4)
                break;
        }
        while 
            2 < 3;
        }"""
        expect = "33333"
        self.assertTrue(TestCodeGen.test(input,expect,559))
        
    def test_continue_in_dowhile(self):
        """Test case 61"""
        input = """void main() {
        do 
            putInt(3);
            continue;
        while 
            3 < 2;
        }"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,560))
        
    def test_continue_with_condition_in_dowhile(self):
        """Test case 62"""
        input = """void main() {
        int i;
        i = 0;
        do 
            i = i + 1;
            putInt(3);
            if (i > 1)
                continue;
        while 
            i < 2;
        }"""
        expect = "33"
        self.assertTrue(TestCodeGen.test(input,expect,561))
        
    def test_continue_in_for(self):
        """Test case 63"""
        input = """
        void main() {
        int i; 
        i = 0; 
        for (i; i < 4; i = i + 1){
            putInt(i);
            continue;
        }
        }"""
        expect = "0123"
        self.assertTrue(TestCodeGen.test(input,expect,562))
        
    def test_continue_in_for_2(self):
        """Test case 64"""
        input = """
        void main() {
        int i; 
        i = 0; 
        for (i; i < 4; i = i + 1){
            continue;
            putInt(i);
        }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,563))
        
    def test_continue_with_condition_in_for(self):
        """Test case 65"""
        input = """
        void main() {
        int i; 
        i = 0; 
        for (i; i < 4; i = i + 1){
            if (i < 2)
                continue;
            putInt(i);
        }
        }"""
        expect = "23"
        self.assertTrue(TestCodeGen.test(input,expect,564))
        
    def test_return_in_for(self):
        """Test case 66"""
        input = """
        void main() {
        int i; 
        i = 0; 
        for (i; i < 4; i = i + 1){
            putInt(i);
            return;
        }
        }"""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,565))
        
    def test_return_in_for_2(self):
        """Test case 67"""
        input = """
        void main() {
        int i; 
        i = 0; 
        for (i; i < 4; i = i + 1){
            return;
            putInt(i);
        }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,566))
        
    def test_return_in_dowhile(self):
        """Test case 68"""
        input = """void main() {
        do 
            putInt(3);
            return;
        while 
            3<2;
        }"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,567)) 

    def test_return_in_dowhile_2(self):
        """Test case 69"""
        input = """void main() {
        do 
            return;
            putInt(3);
        while 
            3<2;
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,568))         
    
    def test_call_expr(self):
        """Test case 70"""
        input = """int a; int foo() {return 2;} 
        void main() {a = foo(); putInt(2);}"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,569))
        
    def test_func_call_in_scope_of_callexpr(self):
        """Test case 71"""
        input = """int foo() { 
        putIntLn(4);
        return 3; 
        }
        void main(){foo(); putInt(46);}"""
        expect = "4\n46"
        self.assertTrue(TestCodeGen.test(input,expect,570))
        
    def test_call_expr_with_param(self):
        """Test case 72"""
        input = """int double(int a) {
        int b; 
        b = a * 2; 
        return b;
        } 
        void main() {
        int a;
        a = double(4); 
        putInt(a);
        }"""
        expect = "8"
        self.assertTrue(TestCodeGen.test(input,expect,571))
        
    def test_array_cell(self):
        """Test case 73"""
        input = """
        void main() {
        int a[5];
        a[4] = 73; 
        putInt(a[4]);
        }"""
        expect = "73"
        self.assertTrue(TestCodeGen.test(input,expect,572))
        
    def test_array_cell_assign(self):
        """Test case 74"""
        input = """
        void main() {
        int a[5];
        int b[6];
        a[4] = 74;
        b[5] = a[4];
        putInt(b[5]);
        }"""
        expect = "74"
        self.assertTrue(TestCodeGen.test(input,expect,573))
        
    def test_array_cell_assign_2(self):
        """Test case 75"""
        input = """void main() {
        int a[5];
        int b[5];
        a[4] = 75;
        b = a;
        putInt(b[4]);
        }"""
        expect = "75"
        self.assertTrue(TestCodeGen.test(input,expect,574))
        
    def test_array_cell_assign_3(self):
        """Test case 76"""
        input = """
        void main() {
        int a[5];
        int b[5];
        a[4] = 76;
        b = a;
        putInt(b[3]);
        }"""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,575))
        
    def test_func_call_many_param(self):
        """Test case 77"""
        input = """
        int foo(int a, float b, string c){
            return 1;
        }
        void main() {
        putInt(foo(1, 1.0, "a"));
        }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,576))
        
    def test_func_call_many_param_2(self):
        """Test case 78"""
        input = """
        int foo(int a, float b, string c){
            putString(c);
            return a + b;
        }
        void main() {
        putInt(foo(1, 1.5, "Tong: "));
        }"""
        expect = "Tong: 2.5"
        self.assertTrue(TestCodeGen.test(input,expect,577))

    def test_operation_in_array_cell(self):
        """Test case 79"""
        input = """
        void main() {
        int a[100];
        a[96] = 79;
        putInt(a[24*4]);
        }"""
        expect = "79"
        self.assertTrue(TestCodeGen.test(input,expect,578))


    def test_nested_array_cell(self):
        """Test case 80"""
        input = """
        void main() {
        int a[100];
        int b[10];
        b[9] = 80;
        a[80] = 9;
        putInt(a[b[9]]);
        }"""
        expect = "9"
        self.assertTrue(TestCodeGen.test(input,expect,579)) 

    def test_redeclaration_inside_scope(self):
        """Test case 81"""
        input = """
        void main() {
        int a;
        a = 10;
        if (a > 0){
            int a;
            a = 9;
        }
        putInt(a);
        }"""
        expect = "9"
        self.assertTrue(TestCodeGen.test(input,expect,580)) 

    def test_declaration_inside_scope(self):
        """Test case 82"""
        input = """
        void main() {
        int a;
        a = 10;
        if (a > 0){
            int b;
            b = 9;
            putInt(b);
        }
        putInt(a);
        }"""
        expect = "910"
        self.assertTrue(TestCodeGen.test(input,expect,581))
        
    def test_operator_association(self):
        """Test case 83"""
        input = """
        void main() {
        int a;
        a = 3 * 9 + 224 / 4;
        putInt(a);
        }"""
        expect = "83"
        self.assertTrue(TestCodeGen.test(input,expect,582))
        
    def test_operator_association_algebra(self):
        """Test case 84"""
        input = """
        void main() {
        int a;
        a = 3 * --9 + 224 / 4 + 17 % 16;
        putInt(a);
        }"""
        expect = "84"
        self.assertTrue(TestCodeGen.test(input,expect,583))
        
    def test_operator_association_logical(self):
        """Test case 85"""
        input = """
        void main() {
        boolean a, b, c, d;
        b = true;
        c = false;
        d = false;
        a = b || c || d ;
        putBool(a);
        }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,584))
        
    def test_global_variable(self):
        """Test case 86"""
        input = """
        void main() {
        boolean b, c, d;
        b = true;
        c = false;
        d = false;
        a = b || c || d ;
        putBool(a);
        }
        boolean a;"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,585))
        
    def test_global_declaration(self):
        """Test case 87"""
        input = """
        void main() {
        putInt(foo);
        }
        int foo(){
        return 1;
        }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,586))
        
    def test_many_returns(self):
        """Test case 88"""
        input = """
        void main() {
        int a;
        a = 3;
        if (a < 0){
            return;
        }
        return;
        putInt(a);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,587))
        
    def test_given_program(self):
        """Test case 89"""
        input = """
        int i ;
        int f(){
        return 200;
        }
        void main (){
            int main;
            main = f();
            putIntLn(main);
            {
            int i;
            int main;
            int f;
            main = 100;
            f = 100;
            i = 100;
            putIntLn(i);
            putIntLn(main);
            putIntLn(f);
            }
            putIntLn(main);
        }
        """
        expect = "200\n100\n100\n100\n200\n"
        self.assertTrue(TestCodeGen.test(input,expect,588))
        
    def test_complex_program_1(self):
        """Test case 90"""
        input ="""int main(){
        boolean a,b,c,d,e;
        a = true; 
        b = false;
        c = a && b;
        d = a || b || c;
        e = a && b && c;
        return a || b && c || d && e;
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,589))
        
    def test_complex_program_2(self):
        """Test case 91"""
        input ="""int multiplyNumbers(int n){
        if (n >= 1)
            return n*multiplyNumbers(n-1);
        else
            return 1;
        }
        void main(){
            putInt(multiplyNumbers(3));
        }"""
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,590))
        
    def test_complex_program_3(self):
        """Test case 92"""
        input ="""int addNumbers(int n){
        if(n != 0)
            return n + addNumbers(n-1);
        else
            return n;
        }
        void main(){
            putInt(multiplyNumbers(3));
        }"""
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,591))
        
    def test_complex_program_4(self):
        """Test case 93"""
        input ="""
        void main(){
            int a, b, temp;
            a = 4;
            b = 6;
            temp = a;
            a = b;
            b = temp;
            putInt(b);
        }"""
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,592))
        
    def test_complex_program_5(self):
        """Test case 94"""
        input ="""
        void main(){
            putLn();
            putString("igga");
            putLn();
            putString("ever");
            putLn();
            putString("aked");
        }"""
        expect = "\nigga\never\naked"
        self.assertTrue(TestCodeGen.test(input,expect,593))
        
    def test_complex_program_6(self):
        """Test case 95"""
        input ="""void foo ( float a[]){}
        void main () {
        float y [10] ;
        int z [10] ;
        foo (y) ; //CORRECT
        foo (z) ; //WRONG
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,594))
        
    def test_complex_program_7(self):
        """Test case 96"""
        input ="""
        void main () {
            for(1; 1 > 0; 3)
                continue;
                putInt(1977);
                break;
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,595))
        
    def test_complex_program_8(self):
        """Test case 97"""
        input ="""
        void main () {
            putString("Hello World");
        }"""
        expect = "Hello World"
        self.assertTrue(TestCodeGen.test(input,expect,596))
        
    def test_complex_program_9(self):
        """Test case 98"""
        input ="""
        void main () {
            putString("Goodbye World");
        }"""
        expect = "Goodbye World"
        self.assertTrue(TestCodeGen.test(input,expect,597))
        
    def test_complex_program_10(self):
        """Test case 99"""
        input ="""
        void main () {
            if (1 > 0)
                if (2 > 1)
                    if (3 > 2)
                        if (4 > 3)
                            if (5 > 4)
                                if ( 6 > 5)
                                    putLn();
        }"""
        expect = "\n"
        self.assertTrue(TestCodeGen.test(input,expect,598))
        
    def test_complex_program_11(self):
        """Test case 100"""
        input ="""
        void main () {
            putStringLn("Last testcase ever");
        }"""
        expect = "Last testcase ever\n"
        self.assertTrue(TestCodeGen.test(input,expect,599))
        
    
        
    
        
    
        
