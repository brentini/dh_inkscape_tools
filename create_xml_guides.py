#!/usr/bin/pyhton
# Damien Henry
# 2014-02-16
#
# This helper script file ease the creatation of guides for inskape.
#
# manual settings of guide is error prone and time consuming.
# This script will generate guide as XML,
# You'll need to manualy add the generated guide in your inscape document.

# Unit is mm
# but inkscape internal unit is px with 90dpi.

# The GuideList Class has the responsability to manage a list of Guide position
class GuideList(object):
    def __init__(self):
        self._guides_positions = [ 0 ];

    def offset(self, offset_mm):
        temp_list = [];
        for position in self._guides_positions:
            temp_list.append(position + offset_mm);
        self._guides_positions = temp_list;

    def add_relative_position(self, position_mm):
        last_guide = self._guides_positions[-1];
        self._guides_positions.append(last_guide + position_mm);

    def add_relative_position_list(self, position_list_mm):
        for position in position_list_mm:
            self.add_relative_position(position)

# The GuideList class has the responsability to create the xml output
class GuideCreator(object):
    _kInch = 25.4;  # 1 inch  = 25.4mm
    _kDpi = 90;

    def __init__(self):
        self._guides_count = 0;
        self._output_buffer = "";

    def dpi_from_mm(self, mm):
        return mm/self._kInch*self._kDpi;

    def add_horizontal_guides(self, mm):
        self._guides_count += 1;
        self._output_buffer += """
    <sodipodi:guide
       orientation="0,1"
       position="0, """ + str(self.dpi_from_mm(mm)) + """"
       id="guide""" + str(self._guides_count) + """" />"""

    def add_vertical_guide(self, mm):
        self._guides_count += 1;
        self._output_buffer += """
    <sodipodi:guide
       orientation="1,0"
       position=" """ + str(self.dpi_from_mm(mm)) + """, 0 "
       id="guide""" + str(self._guides_count) + """" />"""

    def add_all_vertical_guides(self, guides_list):
        for guide in guides_list._guides_positions:
            self.add_vertical_guide(guide);

    def add_all_horizontal_guides(self, guides_list):
        for guide in guides_list._guides_positions:
            self.add_horizontal_guides(guide);

    def write_output_file(self, filename):
        myfile = open(filename,'w');
        myfile.write(self._output_buffer);
        myfile.close();


if __name__ == '__main__':
    print "script create_xml_guides is running"

    # this script help to build guides for a cardboard laser cut.
    # This example add guide for a simple rectangle.
    height = 100;  #height of the rectangle
    width = 200;  #width of the rectangle

    horizontal_list = [0, height];
    horizontal_guides = GuideList();
    horizontal_guides.add_relative_position_list(horizontal_list);
    horizontal_guides.offset(10);

    vertical_list = [0, width];
    vertical_guides = GuideList();
    vertical_guides.add_relative_position_list(vertical_list);
    vertical_guides.offset(10);

    guide_creator = GuideCreator();
    guide_creator.add_all_horizontal_guides(horizontal_guides);
    guide_creator.add_all_vertical_guides(vertical_guides);
    guide_creator.write_output_file("output_xml_guides.txt");

    print "script create_xml_guides done"




