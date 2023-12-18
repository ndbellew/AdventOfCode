with Ada.Text_IO; use Ada.Text_IO;
with Ada.Strings.Fixed;
with Ada.Containers; use Ada.Containers;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Exceptions; use Ada.Exceptions;
with NiceString; use NiceString;

procedure Main is

   type NiceWords is new NiceString.NiceWord;

   InputFile             : File_Type;
   FileName              : String  := "C:\GNAT\2021\bin\textfiles\problem5.txt";
   NumOfNices            : Integer := 0;
   A                     : Unbounded_String;
   procedure ProcessWords(Word : Unbounded_String; NiceCounter : in out Integer)
   is
      Words : NiceWords;
   begin
      IsThreeVowel (NW => Words, NString => A );
      IsTwoLetter  (NW => Words, NString => A );
      HasBaddies   (NW => Words, NString => A );
      if Words.ThreeVowel and Words.TwoLetter and Words.NoBaddies then
         Put_Line(To_String(A) & " is a nice word!");
         NiceCounter := NiceCounter + 1;
      else
         Put_Line(To_String(A) & " is a naughty word!");
         --Put_Line("Has Three Vowel "   & Words.ThreeVowel'Image);
         --Put_Line("Has double Letter " & Words.TwoLetter'Image);
         --Put_Line("Has no Baddies "    & Words.NoBaddies'Image);
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
