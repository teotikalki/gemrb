/* GemRB - Infinity Engine Emulator
 * Copyright (C) 2003 The GemRB Project
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.

 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.

 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
 *
 * $Header: /data/gemrb/cvs2svn/gemrb/gemrb/gemrb/plugins/Core/Polygon.h,v 1.7 2004/09/12 21:58:48 avenger_teambg Exp $
 */
#ifndef POLYGON_H
#define POLYGON_H

#include "Sprite2D.h"
#include "Region.h"
#include "../../includes/RGBAColor.h"
#include "../../includes/globals.h"

#ifdef WIN32

#ifdef GEM_BUILD_DLL
#define GEM_EXPORT __declspec(dllexport)
#else
#define GEM_EXPORT __declspec(dllimport)
#endif

#else
#define GEM_EXPORT
#endif

class GEM_EXPORT Gem_Polygon {
public:
	Gem_Polygon(Point* points, int count, Region *bbox = NULL,
		bool precalculate = false, Color* color = NULL);
	~Gem_Polygon(void);
	Region BBox;
	Point* points;
	int count;
	Sprite2D* fill;
	bool PointIn(Point &p);
	bool PointIn(int x, int y);
	void RecalcBBox();
};

#endif
