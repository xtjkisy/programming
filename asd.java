
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
package com.mycompany.oop2;

/**
 *
 * @author user
 */
public class Oop2 {

    public static void main(String[] args) {
        System.out.println("This program will calculate the avarage of the grade!");
        System.out.println("a ist of (nonegative)exam score ");
        double sum;
        int numStudent;
        double next;
        String answer;
        Scanner keyboard = new Scanner(System.in);
        do{
            System.out.println();
            System.out.println("Enter all scores to be avaraged: ");
            System.out.println("you have entered all the scores");
            System.out.println("Enter a negative number after");
            sum= 0;
            numStudent = 0;
            next = keyboard.nextDouble();
        
        while(next>=0)
        {
            sum = sum+next;
            numStudent++;
            next = keyboard.nextDouble();
            
        }
        if(numStudent>0)
            System.out.println("The avarage is "+(sum/numStudent));
        else
            System.out.println("No scores to avarage!");
        System.out.println("Want to avarage anpther exam?");
        System.out.println("Enter yes or no");
        answer = keyboard.next();
        }while(answer.equalsIgnoreCase("yes"));
        
}
}
