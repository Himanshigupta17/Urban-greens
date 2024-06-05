% Read data from the file
read_data(FileName, TreeCover, BuiltUp, Cropland, BareArea, EmptyArea, ExpectedTree) :-
    open(FileName, read, Stream),
    read_line_to_string(Stream, TreeCoverLine),
    read_line_to_string(Stream, BuiltUpLine),
    read_line_to_string(Stream, CroplandLine),
    read_line_to_string(Stream, BareAreaLine),
    read_line_to_string(Stream, EmptyAreaLine),
    read_line_to_string(Stream, ExpectedTreeLine),
    close(Stream),
    parse_data(TreeCoverLine, BuiltUpLine, CroplandLine, BareAreaLine,EmptyAreaLine, ExpectedTreeLine, TreeCover, BuiltUp, Cropland, BareArea,EmptyArea, ExpectedTree).

% Updated parse_data to handle decimal values
parse_data(TreeCoverLine, BuiltUpLine, CroplandLine, BareAreaLine,EmptyAreaLine, ExpectedTreeLine, TreeCover, BuiltUp, Cropland, BareArea,EmptyArea, ExpectedTree) :-
    % Extract the percentages from the lines
    split_string(TreeCoverLine, " ", " ", ["Tree", "Cover", "Percentage:", PercentageStr1]),
    split_string(BuiltUpLine, " ", " ", ["Built-up", "Percentage:", PercentageStr2]),
    split_string(CroplandLine, " ", " ", ["Cropland", "Percentage:", PercentageStr3]),
    split_string(BareAreaLine, " ", " ", ["Bare", "Area", "Percentage:", PercentageStr4]),
    split_string(ExpectedTreeLine, " ", " ", ["Expected", "Tree", "Percentage:", PercentageStr5]),
    split_string(EmptyAreaLine, " ", " ", ["Bare", "Area", "MeterSq.", AreaStr]),
    atom_number(AreaStr, EmptyArea),
    atom_number(PercentageStr1, TreeCover),
    atom_number(PercentageStr2, BuiltUp),
    atom_number(PercentageStr3, Cropland),
    atom_number(PercentageStr4, BareArea),
    atom_number(PercentageStr5, ExpectedTree).
% Calculate the result and check if you can plant trees
check_result(FileName) :-
    read_data(FileName, TreeCover, BuiltUp, Cropland, BareArea,EmptyArea, ExpectedTree),
    tell('output2.txt'),
    TotalPlantable is TreeCover,
    format('Expected Tree Cover: ~2f~n', [ExpectedTree]),
    format('Total Tree Cover: ~2f~n', [TreeCover]),
    (TotalPlantable < ExpectedTree ->
        Difference is ExpectedTree - TotalPlantable,
        format('Difference: ~2f~n', [Difference]),
        TotalTrees is EmptyArea / 25,
        format('Total Number of Trees Approx.: ~2f~n', [TotalTrees]),
        (Difference < BareArea -> writeln('You can plant trees.'); writeln('Sorry, you can\'t plant trees.'))
    ; writeln('You already have trees present.')
    ),
    told.