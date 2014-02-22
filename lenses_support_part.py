#!/usr/bin/pyhton
import create_xml_guides

if __name__ == '__main__':
    print "script to create goggle main part is running"

    # this script help to build guides for a cardboard laser cut.
    # in way to ease the creation of cardboard goggles.
    thickness = 2;  # cardboard thinkness
    height = 75;  # height of the goggles
    width = 135;  # width of the goggles
    eyes_distance = 70;
    lenses_diameters = 38;

    horizontal_list = [ 0, thickness,
                      height/2, height/2,
                      thickness
                    ];
    horizontal_guides = create_xml_guides.GuideList();
    horizontal_guides.add_relative_position_list(horizontal_list);
    horizontal_guides.offset(200);

    vertical_list = [ 0, thickness,
                        width/2 - eyes_distance/2 - lenses_diameters/2,
                        lenses_diameters/2, lenses_diameters/2,
                        eyes_distance/2 - lenses_diameters/2, # middle
                        eyes_distance/2 - lenses_diameters/2,
                        lenses_diameters/2, lenses_diameters/2,
                        width/2 - eyes_distance/2 - lenses_diameters/2,
                        thickness
                    ];
    vertical_guides = create_xml_guides.GuideList();
    vertical_guides.add_relative_position_list(vertical_list);
    vertical_guides.offset(200);

    guide_creator = create_xml_guides.GuideCreator();
    guide_creator.add_all_horizontal_guides(horizontal_guides);
    guide_creator.add_all_vertical_guides(vertical_guides);
    guide_creator.write_output_file("goggles_lenses_guides.txt");

    print "script done"




