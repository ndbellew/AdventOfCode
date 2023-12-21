with Ada.Text_IO; use Ada.Text_IO;
with Ada.Strings.Fixed;
with Ada.Containers; use Ada.Containers;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Exceptions; use Ada.Exceptions;
with NiceString; use NiceString;

procedure Main is

   type NiceWords is new NiceString.NiceWord;

   InputFile             : File_Type;
   FileName              : String  := "C:\Users\shepe\AdventOfCode\AdventOfCode2015\textfiles\problem5.txt";
   NumOfNices, Pass      : Integer := 0;
   A                     : Unbounded_String;
   procedure ProcessWords(Word : Unbounded_String; NiceCounter : in out Integer)
   is
      Words : NiceWords;
   begin
      ContainsPairs      (NW => Words, NString => Word );
      RepeatedLetter     (NW => Words, NString => Word );
      if Words.LetterWrap and Words.AppearsTwice then
         NiceCounter := NiceCounter + 1;
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
