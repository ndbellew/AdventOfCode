with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;

package NiceString is
   type NiceWord is
      record
         ThreeVowel : Boolean;
         TwoLetter  : Boolean;
         NoBaddies  : Boolean;
      end record;
   procedure IsThreeVowel(NW : in out NiceWord; nString :  in Unbounded_String);
   procedure IsTwoLetter (NW : in out NiceWord; nString :  in Unbounded_String);
   procedure HasBaddies  (NW : in out Niceword; nString :  in Unbounded_String);
end NiceString;
