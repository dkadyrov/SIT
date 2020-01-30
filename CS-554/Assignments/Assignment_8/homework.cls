\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{homework}[2014/08/16 Example LaTeX class]
\LoadClass{article}

\RequirePackage{geometry}
\geometry{letterpaper, margin=1in}

\RequirePackage{hyperref}
\RequirePackage{fancyhdr}

\pagestyle{fancy}
\lhead{\ClassNumber}
\chead{\Title}
\rhead{Page \thepage}
\lfoot{}
\cfoot{\ClassName}
\rfoot{}

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

\newenvironment{problem}[2][]{
    \textbf{Scenario #1: #2} 
    \vskip 2mm
}{\vspace{2mm}}

\newenvironment{solution}{
    \textbf{Solution}
    \vskip 2mm
}{\vspace{4mm}}