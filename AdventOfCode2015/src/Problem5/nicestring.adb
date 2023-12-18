with Ada.Text_IO; use Ada.Text_IO;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Strings.Fixed;

package body NiceString is
   procedure IsThreeVowel(NW : in out NiceWord; nString : in Unbounded_String)
   is
      A,E,II,O,U   : Boolean   := False;
      Counter     : Integer   := 0;
      currChar    : Character;
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

end NiceString;
