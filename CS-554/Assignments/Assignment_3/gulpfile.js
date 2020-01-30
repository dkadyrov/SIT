const gulp = require("gulp");
const concatenate = require("gulp-concat");
const cleanCSS = require("gulp-clean-css");
const autoPrefix = require("gulp-autoprefixer");
const gulpSASS = require("gulp-sass");
const rename = require("gulp-rename");
const minify = require("gulp-minify")

const sassFiles = [
  "./node_modules/tether/dist/css/tether.css",
  "./src/styles/variables.scss",
  "./src/styles/custom.scss"
];


const vendorJsFiles = [
  "./node_modules/jquery/dist/jquery.min.js",
  "./node_modules/tether/dist/js/tether.min.js",
  "./node_modules/bootstrap/dist/js/bootstrap.min.js",
];

// Mod gulp task async for proper callback
gulp.task("sass", async () => {
  gulp
    .src(sassFiles)
    .pipe(gulpSASS())
    .pipe(concatenate("styles.css"))
    .pipe(gulp.dest("./public/css/"))
    .pipe(
      autoPrefix({
        overrideBrowserslist: ["last 2 versions"],
        cascade: false
      })
    )
    .pipe(cleanCSS())
    .pipe(rename("styles.min.css"))
    .pipe(gulp.dest("./public/css/"));
});


// Mod gulp task async for proper callback
gulp.task("js:vendor", async () => {
  gulp
    .src(vendorJsFiles)
    .pipe(concatenate("vendor.min.js"))
    .pipe(gulp.dest("./public/js/"));
  // .pipe(cleanCSS())
  // .pipe(rename("bootstrap.min.js"))
  // .pipe(gulp.dest("./public/js/"));
});

// Altered for gulp v4, use gulp.series and gulp.parralel
gulp.task("build", gulp.series("sass", "js:vendor"));

gulp.task("watch", () => {
  gulp.watch(sassFiles, gulp.series("sass"));
});

gulp.task("default", gulp.series("watch"));