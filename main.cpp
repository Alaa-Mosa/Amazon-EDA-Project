#include <GL/glut.h>
#include <iostream>
#include <string>
#include <cmath>

int board[3][3] = {0};
int turn = 1;
bool gameOver = false;
int winner = 0;

float mouseX = -2.0f, mouseY = -2.0f;

void drawText(std::string text, float x, float y, void *font = GLUT_BITMAP_HELVETICA_18)
{
    glRasterPos2f(x, y);
    for (char c : text)
        glutBitmapCharacter(font, c);
}

void checkWinner()
{
    for (int i = 0; i < 3; i++)
    {
        if (board[i][0] != 0 && board[i][0] == board[i][1] && board[i][0] == board[i][2])
            winner = board[i][0];
        if (board[0][i] != 0 && board[0][i] == board[1][i] && board[0][i] == board[2][i])
            winner = board[0][i];
    }

    if (board[0][0] != 0 && board[0][0] == board[1][1] && board[0][0] == board[2][2])
        winner = board[0][0];
    if (board[0][2] != 0 && board[0][2] == board[1][1] && board[0][2] == board[2][0])
        winner = board[0][2];

    if (winner != 0)
        gameOver = true;


    bool full = true;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (board[i][j] == 0)
                full = false;
    if (full && winner == 0)
    {
        winner = 3;
        gameOver = true;
    }
}

void drawX(float x, float y)
{
    glLineWidth(4.0);
    glColor3f(1.0f, 0.3f, 0.3f);
    glBegin(GL_LINES);
    glVertex2f(x - 0.15f, y - 0.15f);
    glVertex2f(x + 0.15f, y + 0.15f);
    glVertex2f(x + 0.15f, y - 0.15f);
    glVertex2f(x - 0.15f, y + 0.15f);
    glEnd();
}

void drawO(float x, float y)
{
    glLineWidth(4.0);
    glColor3f(0.3f, 0.6f, 1.0f); 
    glBegin(GL_LINE_LOOP);
    for (int i = 0; i < 50; i++)
    {
        float theta = 2.0f * 3.1415926f * float(i) / 50.0f;

        glVertex2f(x + 0.15f * cos(theta), y + 0.15f * sin(theta));
    }
    glEnd();
}

void display()
{
    glClear(GL_COLOR_BUFFER_BIT);
    glLoadIdentity();


    glColor3f(1, 1, 1);
    drawText("TIC-TAC-TOE ELITE", -0.25f, 0.85f);
    glColor3f(0.5, 0.5, 0.5);
    drawText("Developed by Eng Amr Reda", -0.28f, 0.78f, GLUT_BITMAP_HELVETICA_12);


    glLineWidth(2.0);
    glColor3f(0.2f, 0.2f, 0.3f);
    glBegin(GL_LINES);
    glVertex2f(-0.25f, 0.6f);
    glVertex2f(-0.25f, -0.6f);
    glVertex2f(0.25f, 0.6f);
    glVertex2f(0.25f, -0.6f);
    glVertex2f(-0.6f, 0.25f);
    glVertex2f(0.6f, 0.25f);
    glVertex2f(-0.6f, -0.25f);
    glVertex2f(0.6f, -0.25f);
    glEnd();

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            float x = (j - 1) * 0.5f;
            float y = (1 - i) * 0.5f;

            if (!gameOver && mouseX > x - 0.25f && mouseX < x + 0.25f && mouseY > y - 0.25f && mouseY < y + 0.25f)
            {
                glColor4f(1.0f, 1.0f, 1.0f, 0.1f);
                glEnable(GL_BLEND);
                glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
                glBegin(GL_QUADS);
                glVertex2f(x - 0.23f, y - 0.23f);
                glVertex2f(x + 0.23f, y - 0.23f);
                glVertex2f(x + 0.23f, y + 0.23f);
                glVertex2f(x - 0.23f, y + 0.23f);
                glEnd();
                glDisable(GL_BLEND);
            }

            if (board[i][j] == 1)
                drawX(x, y);
            else if (board[i][j] == 2)
                drawO(x, y);
        }
    }

    if (!gameOver)
    {
        glColor3f(1, 1, 1);
        drawText(turn == 1 ? "Player X Turn" : "Player O Turn", -0.15f, -0.8f);
    }
    else
    {
        if (winner == 3)
        {
            glColor3f(0.8, 0.8, 0.8);
            drawText("DRAW GAME!", -0.15f, -0.8f);
        }
        else
        {
            glColor3f(0.2, 1.0, 0.2);
            drawText("PLAYER " + std::string(winner == 1 ? "X" : "O") + " WINS!", -0.2f, -0.8f);
        }
        glColor3f(1, 1, 0);
        drawText("Press 'R' to Restart", -0.18f, -0.9f, GLUT_BITMAP_HELVETICA_12);
    }

    glutSwapBuffers();
}

void mouse(int button, int state, int x, int y)
{
    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN && !gameOver)
    {
        float fx = (x / 400.0f) - 1.0f;
        float fy = 1.0f - (y / 400.0f);

        int col = (fx + 0.75f) / 0.5f;
        int row = (0.75f - fy) / 0.5f;

        if (row >= 0 && row < 3 && col >= 0 && col < 3 && board[row][col] == 0)
        {
            board[row][col] = turn;
            turn = (turn == 1) ? 2 : 1;
            checkWinner();
        }
    }
    glutPostRedisplay();
}

void passiveMouse(int x, int y)
{
    mouseX = (x / 400.0f) - 1.0f;
    mouseY = 1.0f - (y / 400.0f);
    glutPostRedisplay();
}

void keyboard(unsigned char key, int x, int y)
{
    if (key == 'r' || key == 'R')
    {
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                board[i][j] = 0;
        gameOver = false;
        winner = 0;
        turn = 1;
    }
    glutPostRedisplay();
}

void init()
{
    glClearColor(0.05f, 0.05f, 0.1f, 1.0f);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-1, 1, -1, 1);
}

int main(int argc, char **argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(800, 800);
    glutCreateWindow("Elite Tic-Tac-Toe - Eng Amr Reda");
    init();
    glutDisplayFunc(display);
    glutMouseFunc(mouse);
    glutPassiveMotionFunc(passiveMouse);
    glutKeyboardFunc(keyboard);
    glutMainLoop();
    return 0;
}