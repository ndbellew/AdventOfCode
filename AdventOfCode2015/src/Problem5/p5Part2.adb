with Ada.Text_IO; use Ada.Text_IO;
with Ada.Strings.Fixed;
with Ada.Containers; use Ada.Containers;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Exceptions; use Ada.Exceptions;
with NiceString; use NiceString;

procedure Main is

   type NiceWords is new NiceString.NiceWord;

   InputFile             : File_Type;
   FileName              : String  := "C:\cygwin64\home\e399514\Ada\AdventOfCode\AdventOfCode2015\textfiles\problem5_test.txt";
   NumOfNices, Pass      : Integer := 0;
   A                     : Unbounded_String;
   procedure ProcessWords(Word : Unbounded_String; NiceCounter : in out Integer)
   is
      Words : NiceWords;
   begin
      IsThreeVowel   (NW => Words, NString => Word );
      ContainsPairs  (NW => Words, NString => Word );
      HasBaddies     (NW => Words, NString => Word );
      if Words.AppearsTwice then
         Put_Line(To_String(Word) & " is a nice word!");
         NiceCounter := NiceCounter + 1;
      else
         --Put_Line(To_String(A) & " is a naughty word!");
         --Put_Line("Has Three Vowel "   & Words.ThreeVowel'Image);
         --Put_Line("Has double Letter " & Words.TwoLetter'Image);
         --Put_Line("Has no Baddies "    & Words.NoBaddies'Image);
         Pass := 1;
      end if;
   end ProcessWords;

begin
   Open (InputFile, In_File, Filename);
   while not End_Of_File (InputFile) loop
      A   :=   To_Unbounded_String (Get_Line(InputFile));
      ProcessWords(Word => A, NiceCounter => NumOfNices);
   end loop;
   Put_Line("There are " & Integer'Image(NumOfNices) & " nice words.");
end Main;
