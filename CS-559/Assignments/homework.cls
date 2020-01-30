\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{homework}[2014/08/16 Example LaTeX class]
\LoadClass{article}

\RequirePackage{geometry}
\geometry{letterpaper, margin=1in}


\RequirePackage{fancyhdr}

\pagestyle{fancy}
\lhead{\ClassNumber}
\chead{\Title}
\rhead{Page \thepage}
\lfoot{\Author}
\cfoot{}
\rfoot{\ClassName}

\RequirePackage[T1]{fontenc}
\RequirePackage{textcomp}

\RequirePackage{listings}
\lstset{numbers=left,
xleftmargin=2em,
frame=single,
framexleftmargin=0em,
basicstyle=\footnotesize\ttfamily,
xleftmargin=.075\textwidth,
xrightmargin=.01\textwidth,
numberstyle=\footnotesize\ttfamily,
upquote=true,
framesep=10pt,
numbersep=20pt,
}



% \RequirePackage{titlesec}
% \titleformat{\section}
% {\normalfont\Large\bfseries}{Problem~\thesection}{1em}{}

% \titleformat{\subsection}
% {\normalfont\large\bfseries}{Part~\thesubsection}{1em}{}

\newenvironment{problem}[1][]{
    \textbf{Problem #1.}
}{\vspace{2mm}}

\newenvironment{solution}{
    \textbf{Solution} \\
    \linebreak
}{\vspace{4mm}}