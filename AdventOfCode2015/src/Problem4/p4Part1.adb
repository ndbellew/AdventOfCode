with Ada.Text_IO; use Ada.Text_IO;
with Ada.Strings.Fixed;
with Ada.Containers; use Ada.Containers;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Containers.Vectors;
with Ada.Exceptions; use Ada.Exceptions;
with GNAT.MD5; use GNAT.MD5;



procedure Main is


   package Int_Vectors is new Ada.Containers.Vectors(Index_Type => Positive, Element_Type => Integer );
   subtype Vector is Int_Vectors.Vector;
   use all type Vector;

   Houses                : Vector;
   InputFile             : File_Type;
   FileName              : String := "C:\GNAT\2021\bin\textfiles\problem3.txt";
   A                     : String := "yzbqklnj";
   ToHash                : Unbounded_String;
   BoyNotFound           : Boolean := True;
   Hasher                : Message_Digest;
   Numbies, NumOfZeroes  : Integer := 0;

   procedure PrintVector(V : Vector)
   is
   begin
      for Elem of V loop
        Put_Line(Integer'Image(Elem));
      end loop;
   end PrintVector;

   function GenerateHash(HashString : Unbounded_String)
   return Message_Digest
   is
      HashingBoy     : Context;
   begin
      GNAT.MD5.Update(HashingBoy,To_String(HashString));
      return Digest(HashingBoy);
   end GenerateHash;

begin
   ToHash := To_Unbounded_String(A);
   ToHash := ToHash & Integer'Image(1);
   while BoyNotFound loop
      --Numbies := 609043;
      ToHash :=  To_Unbounded_String(A & Ada.Strings.Fixed.Trim(Integer'Image(Numbies), Ada.Strings.Left));
      Hasher := GenerateHash(ToHash);
      -- Put_Line(Hasher);
      for I in Hasher'Range loop
         if Hasher(I) = '0' then
            NumOfZeroes := NumOfZeroes + 1;
         else
            if NumOfZeroes = 5 then
               BoyNotFound := False;
               Put_Line("Hash Identified as "&Hasher);
               exit;
            else
               -- That wasn't it!
               NumOfZeroes := 0;
               Numbies := Numbies + 1;
               exit;
            end if;
         end if;
      end loop;
   end loop;
   Put_Line(Hasher);
   Put_Line("Hash has been identified. The answer is " & To_String(ToHash) & " So the value we are looking for is" & Integer'Image(Numbies));
end Main;
