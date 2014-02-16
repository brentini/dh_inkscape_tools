#!/usr/bin/pyhton
import create_xml_guides

if __name__ == '__main__':
    print "script to create goggle main part is running"

    # this script help to build guides for a cardboard laser cut.
    # in way to ease the creation of cardboard goggles.
    thickness = 2;  # cardboard thinkness
    height = 75;  # height of the goggles
    width = 135;  # width of the goggles

    horizontal_list = [ 0, 50, 20, 20, 7,
                        thickness/2, thickness/2, height,
                        thickness/2, thickness/2, 20];
    horizontal_guides = create_xml_guides.GuideList();
    horizontal_guides.add_relative_position_list(horizontal_list);
    horizontal_guides.offset(10);

    vertical_list = [ 0, height,
                      thickness/2, thickness/2, width/2, width/2,
                      thickness/2, thickness/2, height,
                      thickness/2, thickness/2, width/2, width/2,
                      thickness/2, thickness/2, height];
    vertical_guides = create_xml_guides.GuideList();
    vertical_guides.add_relative_position_list(vertical_list);
    vertical_guides.offset(10);

    guide_creator = create_xml_guides.GuideCreator();
    guide_creator.add_all_horizontal_guides(horizontal_guides);
    guide_creator.add_all_vertical_guides(vertical_guides);
    guide_creator.write_output_file("goggles_mains_guides.txt");

    print "script done"




