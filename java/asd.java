class Teacher{
    String designation = "Teacher";
    String collegeName = "Ala-Too";
    void does(){
        System.out.println("Teaching...");
    }
}
public class PhysicsTeacher extends Teacher{
    String mainSubject = "Physics";
    public static void main (String args[]){
        PhysicsTeacher obj = new PhysicsTeacher();
        System.out.println(obj.collegeName);
        System.out.println(obj.designation);
        System.out.println(obj.mainSubject);
        obj.does();
    }
}

----------------------------------------------------------------------------------
class Person{
    private String name;
    Person(String name){
        this.name=name;
    }
    public String getname(){
        return name;
    }
}
class Student extends Person{
    private int num;
    public Student(String newn, int num){
        super(newn);
        this.num = num;
    }
    public void display(){
        System.out.println(getname() +" "+ this.num);
    }
}
public class New{
public static void main(String args[]){
    Student n = new Student("Syrga", 2004);
    n.display();
}
}
--------------------------------------------------------------------------------

class Vehicle{
    void run(){
        System.out.println("Vehicle running");
    }
}
public class Bike2 extends Vehicle{
        void run(){
            super.run();
            System.out.println("Bike is running!");
        }
        public static void main(String args[]){
            Bike2 b = new Bike2();
            b.run();
        }
}
    
---------------------------------------------------------------------------------
