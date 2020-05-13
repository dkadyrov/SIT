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

\RequirePackage{courier}

\RequirePackage{listings}
\lstset{
    numbers=left,
    xleftmargin=2em,
    frame=single,
    framexleftmargin=0em,
    basicstyle=\footnotesize\ttfamily,
    xleftmargin=.075\textwidth,
    xrightmargin=.075\textwidth,
    numberstyle=\footnotesize\ttfamily,
    upquote=true,
    framesep=10pt,
    numbersep=20pt,
    keywordstyle=\bfseries,
    stringstyle=\textit,
    showstringspaces=false,
    columns=fixed,
    breaklines=true,
}

\newenvironment{problem}[1][]{
    \textbf{Problem #1}\\
    \linebreak
    % \vspace{2mm}
}{
    \vspace{4mm}
}

\newenvironment{solution}{
    \textbf{Solution} \\
    \linebreak
    % \vspace{2mm}
}{
    \vspace{4mm}
}


\renewcommand\headrulewidth{0.4pt}
\renewcommand\footrulewidth{0.4pt}

\setlength\parindent{0pt}

\newcommand{\Title}[1]{\gdef\Title{#1}}
\newcommand{\DueDate}[1]{\gdef\DueDate{#1}}
\newcommand{\ClassName}[1]{\gdef\ClassName{#1}}
\newcommand{\ClassNumber}[1]{\gdef\ClassNumber{#1}}
\newcommand{\ClassSection}[1]{\gdef\ClassSection{#1}}
\newcommand{\Instructor}[1]{\gdef\Instructor{#1}}
\newcommand{\Author}[1]{\gdef\Author{#1}}
\newcommand{\AuthorID}[1]{\gdef\AuthorID{#1}}
%
% Title Page
%
\RequirePackage[shortlabels]{enumitem}
\RequirePackage{amsmath}

\renewcommand{\maketitle}{%
    \thispagestyle{empty}
    \begin{center}
        \Large
        \Title \\
        \vspace{4mm}
        \large
        Due on \DueDate \\
        \ClassName \\ 
        \ClassNumber$-$\ClassSection \\
        \Instructor \\
        \vspace{4mm}
        \Author\\
        \AuthorID\\
        \vspace{4mm}
    \end{center}
}

\RequirePackage{csquotes}
\RequirePackage{hyperref}
\RequirePackage{caption}