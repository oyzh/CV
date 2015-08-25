/*********************
*HOG
*reference: Histograms of Oriented Gradients for Human Detection
*Dalal and Triggs
*There is still someting to do
**********************/

#include <cv.h>
#include <cxcore.h>

/*pixels length of each cell*/
#define CELL_LENGTH 6
/*pixels length of each block*/
#define CELL_LEN_PER_BLOCK 3
#define BLOCK_LENGTH (CELL_LENGTH * CELL_LEN_PER_BLOCK)
/*win lengths*/
#define WIN_WIDTH 96
#define WIN_HEIGHT 128
#define NBINS 9
#define THRESH 0.2
#define FEATURE_LENGTH ((WIN_WIDTH - BLOCK_LENGTH) / CELL_LENGTH + 1) * ((WIN_HEIGHT - BLOCK_LENGTH) / CELL_LENGTH + 1 ) * NBINS * CELL_LEN_PER_BLOCK * CELL_LEN_PER_BLOCK
#define BLOCK_FEAT_SIZE NBINS * CELL_LEN_PER_BLOCK * CELL_LEN_PER_BLOCK

typedef float feature;

IplImage * CheckAndResize( IplImage *src )
{
  IplImage temp , img;
  if ( src->nChannels == 1)
    temp = cvClone( src );
  else
    {
      temp = cvCreateImage( cvGetSize( src ), IPL_DEPTH_8U, 1 );
      cvCvtColor( src , img ,CV_GBR2GRAY);
    }
  img = temp;
  if( (temp->width != WIN_WIDTH) || (temp->height != WIN_HEIGHT))
    {
      img = cvCreateImage( cvSize(WIN_WIDTH,WIN_HEIGHT),temp->depth,temp->nChannels);
      cvResize( temp , img ,CV_INTER_NN );
      cvReleaseImage( temp );
    }
  return img;
}




feature * HOGDescriptor( IplImage *src,feature * feat)
{

  IplImage img;
  float dx[WIN_HEIGHT][WIN_WIDTH] , dy[WIN_HEIGHT][WIN_WIDTH] ;
  float mag[2][WIN_HEIGHT][WIN_WIDTH];
  int ori[2][WIN_HEIGHT][WIN_WIDTH];
  float block_feature[BLOCK_FEAT_SIZE];
  float cell_feature[NBINS];
  int feat_wid = (WIN_WIDTH - BLOCK_LENGTH) / CELL_LENGTH + 1;
  int feat_heg = (WIN_HEIGHT - BLOCK_LENGTH) / CELL_LENGTH + 1;
  int now,begin,count;

  
  feat = (feature *)malloc( sizeof(feature) * FEATURE_LENGTH);
  if (!src)
    return 0;
  img = CheckAndResize( src );
  computeGradient( img , dx , dy );
  MagAndOri( dx , dy , mag , ori);
  for( i = 0 ; i < feat_heg ; i++ )
    for( j = 0 ; j < feat_wid ; j++ )
      {
	x0 = i * CELL_LENGTH;
	y0 = j * CELL_LENGTH;
	for ( m = 0 ; m < BLOCK_FEAT_SIZE ; m++ )
	  {
	    block_feature[m] = 0;
	  }
	for ( k = 0 ; k < CELL_LEN_PER_BLOCK  ; k++ )
	  for( l = 0 ; l < CELL_LEN_PER_BLOCK ; l++ )
	    {
	      for ( m = 0; m < NBINS; m++ )
		cell_feature[m] = 0;
	      for ( m = x0+k*CELL_LENGTH ; m < x0+k*CELL_LENGTH+CELL_LENGTH ; m++)
		for (n = y0+l*CELL_LENGTH ; n < y0+l*CELL_LENGTH+CELL_LENGTH ; n++)
		  {
		    cell_feature[ori[1][m][n]] += mag[1][m][n];
		    cell_feature[ori[0][m][n]] += mag[0][m][n];
		  }
	      count = 0;
	      now = k*NBINS*CELL_LEN_PER_BLOCK+CELL_LEN_PER_BLOCK*l;
	      for ( m = now ; m < now + NBINS ; m++ )
		{
		  block_feature[m] = cell_feature[count];
		  count++;
		}
	    }
	normalize( block_feature );
	for ( m = 0 ; m < BLOCK_FEAT_SIZE ; m++)
	  if (block_feature[m] > THRESH)
	    block_feature[m] = THRESH;
	normalize( block_feature );
	begin = i * BLOCK_FEAT_SIZE * feat_wid + j * BLOCK_FEAT_SIZE;
	for ( m = 0 ; m < BLOCK_FEAT_SIZE ; m++)
	  feat[begin+m] = block_feature[m];
      }
  return feat;
}

    
    
