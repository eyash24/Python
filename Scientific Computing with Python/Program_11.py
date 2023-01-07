# lesson: Using web services: XML Schema
# Source: https://www.freecodecamp.org/learn/scientific-computing-with-python, https://www.youtube.com/watch?v=8DvywoWv6fI&list=PPSV
# for making notes inside the commented part I am using "//", so look out for it
'''
XML Document
<person>
    <lastname>xyz</lastname>
    <age>17</age>
    <dob>2007-01-01</dob>
</person>

XML Schema Contract 
XSD Structure
<xs:complexType name="person">
    <xs:sequence>
        <xs:element name="lastname" type="xs:string"/>
        <xs:element name="age" type="xs:integer"/>
        <xs:element name="dob" type="xs:date"/>
    </xs:sequence>
</xs:complexType>
'''

'''
XML Document
<person>
    <full_name>Tom Cat</full_name>
    <child_name>x_1</child_name>
    <child_name>x_2</child_name>
    <child_name>x_3</child_name>
    <child_name>x_4</child_name>
</person>

XSD Constraits
<xs: element name="person">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="full_name" type="xs:string" minOccurs="1" maxOccurs="1"/>  
            // can occur only 1 time
            <xs:element name="child_name" type="xs:string" minOccurs="0" maxOccurs="10"/> 
            // can occur 10 times
            // for infinite time set maxOccurs:"unbounded"
        </sx:sequence>
    </xs:complexType>
</xs:element>
'''

'''
XML Data types
<customer>Name</customer>
<start>2001-01-01</start>
<startdatetime>2001-01-01T00:00:00Z</startdatetime> 
// Year-Month-DateTtime-of-dayZ
// Z:Timezone specified according to UTC/GMT
<dec>12.038920</dec>
<num>20</num>

XSD Data types
<xs:element name="customer" typer="xs:string">
<xs:element name="start" typer="xs:date">
<xs:element name="startdatetime" typer="xs:dateTime">
<xs:element name="dec" typer="xs:decimal">
<xs:element name="num" typer="xs:integer">
'''

