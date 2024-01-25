library country_icons;

import 'dart:async';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

class CountryIcons {
  static Widget getSvgFlag(String country) {
    String path = 'icons/flags/svg/' + country.toLowerCase() + '.svg';
    return SvgPicture.asset(path, package: 'country_icons');
  }
}

/// Simple scanner to output the path for all icons in console
class Scanner {
  static Future<List<FileSystemEntity>> dirContents(Directory dir) {
    var files = <FileSystemEntity>[];
    var completer = new Completer<List<FileSystemEntity>>();
    var lister = dir.list(recursive: false);
    lister.listen((file) => files.add(file),
        onDone: () => completer.complete(files));
    return completer.future;
  }
}

Future main() async {
  var files = await Scanner.dirContents(new Directory("icons/flags"));
  print("  assets:");
  files.forEach((file) {
    print("    - ${file.path}");
  });
}
