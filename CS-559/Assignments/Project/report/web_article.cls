% \NeedsTeXFormat{LaTeX2e}
% \ProvidesPackage{web_article}[2018/07/24 Kadyrov, Daniel Article Template]
%
% \LoadClass{article}
% \RequirePackage{geometry}
%
% \setlength{\parindent}{0pt}
% \setlength{\parskip}{6pt plus 2pt minus 1pt}
%
% \RequirePackage{fancyhdr}
% \pagestyle{fancy}
% \fancyhf{}
% \lhead{\title}
% \chead{}
% \rhead{\leftmark}
% \rfoot{Page \thepage}
% \lfoot{}
% \renewcommand{\headrulewidth}{1pt}
% \renewcommand{\footrulewidth}{1pt}
%
% \RequirePackage[dvipsnames]{xcolor}
%
% \RequirePackage{hyperref}
% \hypersetup{
%         colorlinks,%
%   citecolor=blue,%
%   filecolor=blue,%
%   linkcolor=blue,%
%   urlcolor=blue,
%   breaklinks=true}
% \urlstyle{same}  % don't use monospace font for urls
%
% % Quotations
% % Define Quote Font
% \RequirePackage{lmodern}
%
% \RequirePackage{mdframed}
% \definecolor{blockquote-border}{RGB}{221,221,221}
% \definecolor{blockquote-text}{RGB}{119,119,119}
% \newmdenv[rightline=false,bottomline=false,topline=false,linewidth=3pt,linecolor=blockquote-border,skipabove=\parskip]{customblockquote}
% \renewenvironment{quote}{\begin{customblockquote}\fontfamily{lmtt}\selectfont\list{}{\rightmargin=0em\leftmargin=0em}%
% \item\relax\color{blockquote-text}\ignorespaces}{\unskip\unskip\endlist\end{customblockquote}}
%
% \RequirePackage{graphicx,grffile}
% \RequirePackage{float}
% \makeatletter
% % \def\maxwidth{\ifdim\Gin@nat@width>\linewidth\linewidth\else\Gin@nat@width\fi}
% % \def\maxheight{\ifdim\Gin@nat@height>\textheight\textheight\else\Gin@nat@height\fi}
% \makeatother
%
% \setkeys{Gin}{width=\maxwidth,height=\maxheight,keepaspectratio}
% \let\origfigure=\figure
% \let\endorigfigure=\endfigure
% \renewenvironment{figure}[1][]{%
%    \origfigure[H]
% }{%
%    \endorigfigure
% }
%
% \RequirePackage{listings}
% \newcommand{\passthrough}[1]{#1}
% \lstnewenvironment{code}{\lstset{language=Haskell,basicstyle=\small\ttfamily}}{}
%
% %
% % listing colors
% %
% \definecolor{listing-background}{HTML}{F7F7F7}
% \definecolor{listing-rule}{HTML}{B3B2B3}
% \definecolor{listing-numbers}{HTML}{B3B2B3}
% \definecolor{listing-text-color}{HTML}{000000}
% \definecolor{listing-keyword}{HTML}{435489}
% \definecolor{listing-identifier}{HTML}{435489}
% \definecolor{listing-string}{HTML}{00999A}
% \definecolor{listing-comment}{HTML}{8E8E8E}
% \definecolor{listing-javadoc-comment}{HTML}{006CA9}
%
% \lstdefinestyle{eisvogel_listing_style}{
%   language         = java,
%   numbers          = left,
%   backgroundcolor  = \color{listing-background},
%   basicstyle       = \color{listing-text-color}\small\ttfamily{}\linespread{1.15}, % print whole listing small
%   xleftmargin=.075\textwidth,
%   xrightmargin=.01\textwidth,
%   breaklines       = true,
%   frame            = single,
%   framesep         = 10 pt,
%   rulecolor        = \color{listing-rule},
%   frameround       = ffff,
%   % framexleftmargin = 2.5em,
%   tabsize          = 4,
%   numberstyle      = \color{listing-numbers},
%   numbersep        = 20pt,
%   aboveskip        = 1.0em,
%   keywordstyle     = \bfseries\color{listing-keyword},
%   classoffset      = 0,
%   sensitive        = true,
%   identifierstyle  = \color{listing-identifier},
%   commentstyle     = \color{listing-comment},
%   morecomment      = [s][\color{listing-javadoc-comment}]{/**}{*/},
%   stringstyle      = \color{listing-string},
%   showstringspaces = false,
%   escapeinside     = {/*@}{@*/}, % Allow LaTeX inside these special comments
%   literate         =
%   {á}{{\'a}}1 {é}{{\'e}}1 {í}{{\'i}}1 {ó}{{\'o}}1 {ú}{{\'u}}1
%   {Á}{{\'A}}1 {É}{{\'E}}1 {Í}{{\'I}}1 {Ó}{{\'O}}1 {Ú}{{\'U}}1
%   {à}{{\`a}}1 {è}{{\'e}}1 {ì}{{\`i}}1 {ò}{{\`o}}1 {ù}{{\`u}}1
%   {À}{{\`A}}1 {È}{{\'E}}1 {Ì}{{\`I}}1 {Ò}{{\`O}}1 {Ù}{{\`U}}1
%   {ä}{{\"a}}1 {ë}{{\"e}}1 {ï}{{\"i}}1 {ö}{{\"o}}1 {ü}{{\"u}}1
%   {Ä}{{\"A}}1 {Ë}{{\"E}}1 {Ï}{{\"I}}1 {Ö}{{\"O}}1 {Ü}{{\"U}}1
%   {â}{{\^a}}1 {ê}{{\^e}}1 {î}{{\^i}}1 {ô}{{\^o}}1 {û}{{\^u}}1
%   {Â}{{\^A}}1 {Ê}{{\^E}}1 {Î}{{\^I}}1 {Ô}{{\^O}}1 {Û}{{\^U}}1
%   {œ}{{\oe}}1 {Œ}{{\OE}}1 {æ}{{\ae}}1 {Æ}{{\AE}}1 {ß}{{\ss}}1
%   {ç}{{\c c}}1 {Ç}{{\c C}}1 {ø}{{\o}}1 {å}{{\r a}}1 {Å}{{\r A}}1
%   {€}{{\EUR}}1 {£}{{\pounds}}1 {«}{{\guillemotleft}}1
%   {»}{{\guillemotright}}1 {ñ}{{\~n}}1 {Ñ}{{\~N}}1 {¿}{{?`}}1
%   {…}{{\ldots}}1 {≥}{{>=}}1 {≤}{{<=}}1 {„}{{\glqq}}1 {“}{{\grqq}}1
%   {”}{{''}}1
% }
% \lstset{style=eisvogel_listing_style}
%
% \lstdefinelanguage{XML}{
%   morestring      = [b]",
%   moredelim       = [s][\bfseries\color{listing-keyword}]{<}{\ },
%   moredelim       = [s][\bfseries\color{listing-keyword}]{</}{>},
%   moredelim       = [l][\bfseries\color{listing-keyword}]{/>},
%   moredelim       = [l][\bfseries\color{listing-keyword}]{>},
%   morecomment     = [s]{<?}{?>},
%   morecomment     = [s]{<!--}{-->},
%   commentstyle    = \color{listing-comment},
%   stringstyle     = \color{listing-string},
%   identifierstyle = \color{listing-identifier}
% }

\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{web_article}[2018/07/24 Kadyrov, Daniel Article Template]

\LoadClass{article}
\RequirePackage{geometry}

\RequirePackage{lipsum}
% Remove Paragraph Indents
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt plus 2pt minus 1pt}

% TODO Black and White
% TODO Finish Markdown

% Colors
\RequirePackage[dvipsnames]{xcolor}

% Get Markdown Variables
% $if(Title)$
% \title{$Title$}
% $endif$
% \author{$for(Author)$$Author$$sep$\\$endfor$}
% $if(Date)$
% \date{$Date$}
% $endif$

% Headers and Footer
\RequirePackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\lhead{\title}
\chead{}
\rhead{\leftmark}
\rfoot{Page \thepage}
\lfoot{}
\renewcommand{\headrulewidth}{1pt}
\renewcommand{\footrulewidth}{1pt}

% Hyperref
\RequirePackage{hyperref}
% \hypersetup{
%   $if(title-meta)$
%     pdftitle={$title-meta$},
%   $endif$
%   $if(author-meta)$
%     pdfauthor={$author-meta$},
%   $endif$
%   $if(keywords)$
%     pdfkeywords={$for(keywords)$$keywords$$sep$, $endfor$},
%   $endif$
%   colorlinks,%
%   citecolor=black,%
%   filecolor=black,%
%   linkcolor=black,%
%   urlcolor=black,
%   breaklinks=true}
% \urlstyle{same}  % don't use monospace font for urls

% Quotations
% Define Quote Font

% $if(blockquote)$
\RequirePackage{lmodern}
\RequirePackage{mdframed}
\definecolor{blockquote-border}{RGB}{221,221,221}
\definecolor{blockquote-text}{RGB}{119,119,119}
\newmdenv[rightline=false,bottomline=false,topline=false,linewidth=3pt,linecolor=blockquote-border,skipabove=\parskip]{customblockquote}
\renewenvironment{quote}{\vspace{6pt plus 2pt minus 1pt}\begin{customblockquote}\fontfamily{lmtt}\selectfont\list{}{\rightmargin=0em\leftmargin=0em}%
\item\relax\color{blockquote-text}\ignorespaces}{\unskip\unskip\endlist\end{customblockquote}}
% $endif$
% Graphics / Images

% $if(graphics)$
\RequirePackage{graphicx,grffile}
\RequirePackage{float}
\makeatletter
\def\maxwidth{\ifdim\Gin@nat@width>\linewidth\linewidth\else\Gin@nat@width\fi}
\def\maxheight{\ifdim\Gin@nat@height>\textheight\textheight\else\Gin@nat@height\fi}
\makeatother
% Scale images if necessary, so that they will not overflow the page
% margins by default, and it is still possible to overwrite the defaults
% using explicit options in \includegraphics[width, height, ...]{}
\setkeys{Gin}{width=\maxwidth,height=\maxheight,keepaspectratio}
\let\origfigure=\figure
\let\endorigfigure=\endfigure
\renewenvironment{figure}[1][]{%
   \origfigure[H]
}{%
   \endorigfigure
}
% $endif$

% $if(listings)$
\RequirePackage{listings}
\newcommand{\passthrough}[1]{#1}
% $endif$
% $if(lhs)$
\lstnewenvironment{code}{\lstset{language=Haskell,basicstyle=\small\ttfamily}}{}
% $endif$

%
% listing colors
%
\definecolor{listing-background}{HTML}{F7F7F7}
\definecolor{listing-rule}{HTML}{B3B2B3}
\definecolor{listing-numbers}{HTML}{B3B2B3}
\definecolor{listing-text-color}{HTML}{000000}
\definecolor{listing-keyword}{HTML}{435489}
\definecolor{listing-identifier}{HTML}{435489}
\definecolor{listing-string}{HTML}{00999A}
\definecolor{listing-comment}{HTML}{8E8E8E}
\definecolor{listing-javadoc-comment}{HTML}{006CA9}

% Listings
%
%

% $if(listings)$
\lstdefinestyle{eisvogel_listing_style}{
  language         = java,
  numbers          = left,
  backgroundcolor  = \color{listing-background},
  basicstyle       = \color{listing-text-color}\small\ttfamily{}\linespread{1.15}, % print whole listing small
  xleftmargin=.075\textwidth,
  xrightmargin=.01\textwidth,
  breaklines       = true,
  frame            = single,
  framesep         = 10 pt,
  rulecolor        = \color{listing-rule},
  frameround       = ffff,
  % framexleftmargin = 2.5em,
  tabsize          = 4,
  numberstyle      = \color{listing-numbers},
  numbersep        = 20pt,
  aboveskip        = 1.0em,
  keywordstyle     = \bfseries\color{listing-keyword},
  classoffset      = 0,
  sensitive        = true,
  identifierstyle  = \color{listing-identifier},
  commentstyle     = \color{listing-comment},
  morecomment      = [s][\color{listing-javadoc-comment}]{/**}{*/},
  stringstyle      = \color{listing-string},
  showstringspaces = false,
  escapeinside     = {/*@}{@*/}, % Allow LaTeX inside these special comments
  literate         =
  {á}{{\'a}}1 {é}{{\'e}}1 {í}{{\'i}}1 {ó}{{\'o}}1 {ú}{{\'u}}1
  {Á}{{\'A}}1 {É}{{\'E}}1 {Í}{{\'I}}1 {Ó}{{\'O}}1 {Ú}{{\'U}}1
  {à}{{\`a}}1 {è}{{\'e}}1 {ì}{{\`i}}1 {ò}{{\`o}}1 {ù}{{\`u}}1
  {À}{{\`A}}1 {È}{{\'E}}1 {Ì}{{\`I}}1 {Ò}{{\`O}}1 {Ù}{{\`U}}1
  {ä}{{\"a}}1 {ë}{{\"e}}1 {ï}{{\"i}}1 {ö}{{\"o}}1 {ü}{{\"u}}1
  {Ä}{{\"A}}1 {Ë}{{\"E}}1 {Ï}{{\"I}}1 {Ö}{{\"O}}1 {Ü}{{\"U}}1
  {â}{{\^a}}1 {ê}{{\^e}}1 {î}{{\^i}}1 {ô}{{\^o}}1 {û}{{\^u}}1
  {Â}{{\^A}}1 {Ê}{{\^E}}1 {Î}{{\^I}}1 {Ô}{{\^O}}1 {Û}{{\^U}}1
  {œ}{{\oe}}1 {Œ}{{\OE}}1 {æ}{{\ae}}1 {Æ}{{\AE}}1 {ß}{{\ss}}1
  {ç}{{\c c}}1 {Ç}{{\c C}}1 {ø}{{\o}}1 {å}{{\r a}}1 {Å}{{\r A}}1
  {€}{{\EUR}}1 {£}{{\pounds}}1 {«}{{\guillemotleft}}1
  {»}{{\guillemotright}}1 {ñ}{{\~n}}1 {Ñ}{{\~N}}1 {¿}{{?`}}1
  {…}{{\ldots}}1 {≥}{{>=}}1 {≤}{{<=}}1 {„}{{\glqq}}1 {“}{{\grqq}}1
  {”}{{''}}1
}
\lstset{style=eisvogel_listing_style}

\lstdefinelanguage{XML}{
  morestring      = [b]",
  moredelim       = [s][\bfseries\color{listing-keyword}]{<}{\ },
  moredelim       = [s][\bfseries\color{listing-keyword}]{</}{>},
  moredelim       = [l][\bfseries\color{listing-keyword}]{/>},
  moredelim       = [l][\bfseries\color{listing-keyword}]{>},
  morecomment     = [s]{<?}{?>},
  morecomment     = [s]{<!--}{-->},
  commentstyle    = \color{listing-comment},
  stringstyle     = \color{listing-string},
  identifierstyle = \color{listing-identifier}
}
% $endif$
