with Ada.Text_IO; use Ada.Text_IO;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Strings.Fixed;
with Ada.Containers; use Ada.Containers;
with Ada.Containers.Vectors;

package body NiceString is
   procedure IsThreeVowel(NW : in out NiceWord; nString : in Unbounded_String)
   is
      A,E,II,O,U   : Boolean   := False;
      Counter      : Integer   := 0;
      currChar     : Character;
   begin
      for I in 1 .. Length (nString) loop
         CurrChar := Element (NString, I);
         if (CurrChar = 'a' or CurrChar = 'A')     then
            A := True;
            Counter := Counter + 1;
         elsif (CurrChar = 'e' or CurrChar = 'E')  then
            E := True;
            Counter := Counter + 1;
         elsif (CurrChar = 'i' or CurrChar = 'I')  then
            II := True;
            Counter := Counter + 1;
         elsif (CurrChar = 'o' or CurrChar = 'O')  then
            O := True;
            Counter := Counter + 1;
         elsif (CurrChar = 'u' or CurrChar = 'U')  then
            U := True;
            Counter := Counter + 1;
         end if;
      end loop;
      if Counter >= 3 then
         NW.ThreeVowel := True;
      end if;
   end IsThreeVowel;

   procedure IsTwoLetter (NW : in out NiceWord; nString : in Unbounded_String)
    is
      hasDouble   : Boolean := False;
      currChar    : Character;
   begin
      for letter in 1 .. Length (nString) loop
         if letter = 1 then
            CurrChar := Element (nString, letter);
         elsif Element(nString, letter) = CurrChar then
            NW.TwoLetter := True;
            exit;
         else
            CurrChar := Element(NString, letter);
         end if;
      end loop;
   end IsTwoLetter;

   procedure HasBaddies  (NW : in out Niceword; nString : in Unbounded_String)
   is

      type HasBaddiesArray is array (1 .. 4) of String(1 .. 2);
      Baddies                 : HasBaddiesArray;
      Test                    : String( 1 .. 2 );
      Isbad                   : Boolean := False;
      LeftLetter, RightLetter : Character;
   begin
      Baddies(1) := "ab";
      Baddies(2) := "cd";
      Baddies(3) := "pq";
      Baddies(4) := "xy";
      for letter in 1 .. Length (NString) loop
         if letter = 1 then
            LeftLetter := Element(NString, letter);
         else
            RightLetter := Element(NString, letter);
            Test := LeftLetter & RightLetter;
            for Bad of Baddies loop
               if Bad = Test then
                  IsBad := True;
                  exit;
               end if;
            end loop;
            if IsBad then
               exit;
            else
               LeftLetter := RightLetter;
            end if;
         end if;

      end loop;
      if not IsBad then
         NW.NoBaddies := True;
      end if;

   end HasBaddies;

   procedure ContainsPairs(NW : in out NiceWord; nString : in Unbounded_String)
   is
      subtype Tester is String(1..2);
      
      package String_Vector is new
        Ada.Containers.Vectors
          (Index_Type   => Natural,
           Element_Type => Tester);
      
      Letter_Vector   : String_Vector.Vector;
      LetterPosition1 : Character := '+';
      LetterPosition2 : Character := '+';
      Test            : Tester;
      Fail            : Boolean := True;
   begin
      for Letter in 1 .. Length (NString) loop
         if LetterPosition1 = '+' then
            LetterPosition1 := Element(NString, Letter);
         elsif LetterPosition2 = '+' then
            LetterPosition2 := Element(NString, Letter);
            Test := LetterPosition1 & LetterPosition2;
            if (Letter_Vector.Length > 0  and Fail) then
               for I in Letter_Vector.First_Index .. Letter_Vector.Last_Index loop
                  if Letter_Vector(I) = Test then
                     Fail := False;
                  end if;
               end loop;
               if Fail then
                  Letter_Vector.Append(Test);
                  LetterPosition1 := LetterPosition2;
                  LetterPosition2 := '+';
                  Test := "++";
               else
                  NW.AppearsTwice := True;
                  exit;
               end if;
            else
               Letter_Vector.Append(Test);
               LetterPosition1 := LetterPosition2;
               LetterPosition2 := '+';
            end if;
            
         end if;

      end loop;
   end ContainsPairs;

   procedure RepeatedLetter(NW : in out NiceWord; nString : in Unbounded_String)
   is
      type Tester is new String(1 .. 3);
      package Letter_Vector is new
        Ada.Containers.Vectors
          (Index_Type   => Natural,
           Element_Type => Tester);
   begin
      Put_Line("Nothing");
   end RepeatedLetter;


end NiceString;
