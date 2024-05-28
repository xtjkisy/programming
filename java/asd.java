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


public class Shape{
    private double height;
    private double width;
    public void setValues(double height, double width)
    {
        this.height = height;
        this.width = width;
    }
    public double getHeight(){
        return height;
    }
    public double getWidth(){
        return width;
    }
}
public class Rectangle extends Shape{
    public double getArea(){
        return getHeight() *getWidth();
    }
}
public class Triangle extends Shape{
    public double getArea(){
        return (getHeight()* getWidth())/2;
    }
}
public class Main{
    public static void main(String args[]){
        Shape shape;
        Rectangle rect = new Rectangle();
        shape = rect;
        
        shape.setValues(78, 5);
        
        System.out.println("Area of a rectangle: " +rect.getArea());
        
        Triangle tri = new Triangle();
        shape = tri;
        shape.setValues(34, 3);
        
        System.out.println("Area of a trianlge: " +rect.getArea());
    }
}
//here some errors, check and write it again
--------------------------------------------------------------------------------------------



import java.util.List;
import java.util.ArrayList;
public class ListExample {
    public static void main(String[] args){
        List<String> gameList = new ArrayList<String>();
        gameList.add("Football");
        gameList.add("Cricket");
        gameList.add("Hockey");
        System.out.println("*****|terating**********");
        gameList.forEach(games->System.out.println(games));
    }
}
