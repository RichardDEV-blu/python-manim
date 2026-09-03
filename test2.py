from manim import *
import numpy as np

# ============================================================
# VERTICAL 9:16 — 1080p
# ============================================================

config.frame_height = 8.0
config.frame_width = 4.5

config.pixel_width = 1080
config.pixel_height = 1920

config.background_color = "#000000"
config.frame_rate = 60

# ============================================================
# COLORS
# ============================================================

COLOR_TEXT = "#F5F5F7"

# ------------------------------------------------------------
# WORD / VECTOR COLORS
# ------------------------------------------------------------

# BENIGN
COLOR_BENIGN = "#2EC4D6"

# MALIGNANT
COLOR_MALIGNANT = "#FF7043"

# FIBROMA
COLOR_FIBROMA = "#58D68D"

# FIBROSARCOMA
COLOR_FIBROSARCOMA = "#B57EF7"

# ------------------------------------------------------------
# RELATION COLOR
# ------------------------------------------------------------

# Same color for both translated semantic relations
COLOR_RELATION = "#FFD166"

# ------------------------------------------------------------
# UI
# ------------------------------------------------------------

COLOR_GRID = "#2B2F3A"
COLOR_OPERATOR = "#8E95A8"
COLOR_MUTED = "#AAB0BF"

# ============================================================
# TYPOGRAPHY
# ============================================================

FONT = "Montserrat"

# ============================================================
# GLOBAL TIMING
# ============================================================

# 1.35 = 35% slower

SPEED_FACTOR = 1.35

# Ambient camera rotation also becomes 35% slower.
AMBIENT_ROTATION_RATE = 0.06 / SPEED_FACTOR

# ============================================================
# SAFE DIMENSIONS
# ============================================================

SAFE_W = 4.0
GRID_W = 3.7
GRID_H = 4.8

# ============================================================
# UI POSITIONS
# ============================================================

CAPTION_Y = -1.80
EQUATION_Y = -2.80

# ============================================================
# 3D SCENE SHIFT
# ============================================================

SCENE_SHIFT = np.array([0.28, 0.0, 0.0])


# ============================================================
# SCENE
# ============================================================

class BenignMalignantVertical(ThreeDScene):

    def construct(self):

        self.camera.background_color = "#000000"

        # ====================================================
        # CAMERA
        # ====================================================

        self.set_camera_orientation(
            phi=65 * DEGREES,
            theta=-45 * DEGREES,
            distance=10
        )

        # ====================================================
        # GRID
        # ====================================================

        grid = NumberPlane(
            x_range=[-2.2, 2.2, 1],
            y_range=[-2.8, 2.8, 1],
            x_length=GRID_W,
            y_length=GRID_H,

            background_line_style={
                "stroke_color": COLOR_GRID,
                "stroke_width": 1,
                "stroke_opacity": 0.45,
            },

            axis_config={
                "stroke_color": "#555B70",
                "stroke_opacity": 0.4,
            }
        )

        grid.shift(SCENE_SHIFT)

        self.play(
            Create(grid),
            run_time=1.9 * SPEED_FACTOR
        )

        self.begin_ambient_camera_rotation(
            rate=AMBIENT_ROTATION_RATE
        )

        # ====================================================
        # HEADER
        # ====================================================

        title = Text(
            "EMBEDDING ALGEBRA",
            font=FONT,
            font_size=28,
            color=COLOR_TEXT,
            weight=BOLD
        )

        if title.width > SAFE_W:
            title.scale(
                SAFE_W / title.width
            )

        subtitle = Text(
            "SEMANTIC RELATIONS AS VECTORS",
            font=FONT,
            font_size=14,
            color=COLOR_OPERATOR,
            weight=BOLD
        )

        if subtitle.width > SAFE_W:
            subtitle.scale(
                SAFE_W / subtitle.width
            )

        header = VGroup(
            title,
            subtitle
        ).arrange(
            DOWN,
            buff=0.08
        )

        header.to_edge(
            UP,
            buff=0.25
        )

        self.add_fixed_in_frame_mobjects(
            header
        )

        self.play(
            FadeIn(header),
            run_time=1.1 * SPEED_FACTOR
        )

        # ====================================================
        # COLOR LEGEND
        # ====================================================

        def make_legend_item(label, color):

            dot = Dot(
                radius=0.045,
                color=color
            )

            text = Text(
                label,
                font=FONT,
                font_size=9.5,
                color=COLOR_TEXT,
                weight=BOLD
            )

            return VGroup(
                dot,
                text
            ).arrange(
                RIGHT,
                buff=0.07
            )

        legend_benign = make_legend_item(
            "BENIGN",
            COLOR_BENIGN
        )

        legend_malignant = make_legend_item(
            "MALIGNANT",
            COLOR_MALIGNANT
        )

        legend_fibroma = make_legend_item(
            "FIBROMA",
            COLOR_FIBROMA
        )

        legend_fibrosarcoma = make_legend_item(
            "FIBROSARCOMA",
            COLOR_FIBROSARCOMA
        )

        legend_row_1 = VGroup(
            legend_benign,
            legend_malignant
        ).arrange(
            RIGHT,
            buff=0.20
        )

        legend_row_2 = VGroup(
            legend_fibroma,
            legend_fibrosarcoma
        ).arrange(
            RIGHT,
            buff=0.20
        )

        legend = VGroup(
            legend_row_1,
            legend_row_2
        ).arrange(
            DOWN,
            buff=0.07
        )

        legend.move_to(
            np.array([
                0,
                2.30,
                0
            ])
        )

        self.add_fixed_in_frame_mobjects(
            legend
        )

        # Initially invisible
        legend.set_opacity(0)

        # ====================================================
        # ANALOGY
        #
        # BENIGN : MALIGNANT :: FIBROMA : FIBROSARCOMA
        #
        # This remains the visual equation throughout.
        # ====================================================

        eq_benign = Text(
            "BENIGN",
            font=FONT,
            font_size=13,
            color=COLOR_BENIGN,
            weight=BOLD
        )

        eq_colon_1 = Text(
            ":",
            font=FONT,
            font_size=15,
            color=COLOR_OPERATOR,
            weight=BOLD
        )

        eq_malignant = Text(
            "MALIGNANT",
            font=FONT,
            font_size=13,
            color=COLOR_MALIGNANT,
            weight=BOLD
        )

        eq_double_colon = Text(
            "::",
            font=FONT,
            font_size=15,
            color=COLOR_OPERATOR,
            weight=BOLD
        )

        eq_fibroma = Text(
            "FIBROMA",
            font=FONT,
            font_size=13,
            color=COLOR_FIBROMA,
            weight=BOLD
        )

        eq_colon_2 = Text(
            ":",
            font=FONT,
            font_size=15,
            color=COLOR_OPERATOR,
            weight=BOLD
        )

        eq_fibrosarcoma = Text(
            "FIBROSARCOMA",
            font=FONT,
            font_size=13,
            color=COLOR_FIBROSARCOMA,
            weight=BOLD
        )

        full_equation = VGroup(
            eq_benign,
            eq_colon_1,
            eq_malignant,
            eq_double_colon,
            eq_fibroma,
            eq_colon_2,
            eq_fibrosarcoma
        )

        full_equation.arrange(
            RIGHT,
            buff=0.09
        )

        if full_equation.width > SAFE_W:
            full_equation.scale(
                SAFE_W / full_equation.width
            )

        full_equation.move_to(
            np.array([
                0,
                EQUATION_Y,
                0
            ])
        )

        self.add_fixed_in_frame_mobjects(
            full_equation
        )

        # Initially invisible
        for item in full_equation:
            item.set_opacity(0)

        # ====================================================
        # VECTOR POSITIONS
        # ====================================================

        origin = (
            np.array([
                0.0,
                0.0,
                0.0
            ])
            + SCENE_SHIFT
        )

        # ----------------------------------------------------
        # BENIGN
        # ----------------------------------------------------

        v_benign = (
            np.array([
                -1.35,
                -0.85,
                0.35
            ])
            + SCENE_SHIFT
        )

        # ----------------------------------------------------
        # MALIGNANT
        # ----------------------------------------------------

        v_malignant = (
            np.array([
                -0.30,
                0.78,
                0.58
            ])
            + SCENE_SHIFT
        )

        # ----------------------------------------------------
        # FIBROMA
        # ----------------------------------------------------

        v_fibroma = (
            np.array([
                0.72,
                -0.45,
                0.20
            ])
            + SCENE_SHIFT
        )

        # ----------------------------------------------------
        # SAME DISPLACEMENT
        #
        # BENIGN -> MALIGNANT
        #
        # translated to:
        #
        # FIBROMA -> FIBROSARCOMA
        # ----------------------------------------------------

        relation_vector = (
            v_malignant
            - v_benign
        )

        v_fibrosarcoma = (
            v_fibroma
            + relation_vector
        )

        # ====================================================
        # VECTOR HELPER
        # ====================================================

        def make_vector(
            start,
            end,
            color,
            thickness=0.035
        ):

            return Arrow3D(
                start=start,
                end=end,
                color=color,
                thickness=thickness,
                height=0.22,
                base_radius=0.065
            )

        # ====================================================
        # BASE VECTORS
        # ====================================================

        benign_vector = make_vector(
            origin,
            v_benign,
            COLOR_BENIGN,
            thickness=0.040
        )

        malignant_vector = make_vector(
            origin,
            v_malignant,
            COLOR_MALIGNANT,
            thickness=0.040
        )

        fibroma_vector = make_vector(
            origin,
            v_fibroma,
            COLOR_FIBROMA,
            thickness=0.040
        )

        # ====================================================
        # CAPTION HELPER
        # ====================================================

        def make_caption(
            text,
            color,
            font=FONT,
            font_size=16,
            max_width=SAFE_W
        ):

            if "BENIGN to MALIGNANT" in text:

                lines = [
                    "The relation from BENIGN",
                    "to MALIGNANT"
                ]

                fs = 15

            elif "same relation" in text:

                lines = [
                    "Apply the same relation",
                    "to FIBROMA"
                ]

                fs = 15

            elif "FIBROSARCOMA" in text:

                lines = [
                    "The translated relation",
                    "points toward FIBROSARCOMA"
                ]

                fs = 15

            else:

                lines = [text]
                fs = font_size

            group = VGroup()

            for line in lines:

                t = Text(
                    line,
                    font=font,
                    font_size=fs,
                    color=color,
                    weight=BOLD
                )

                if t.width > max_width:
                    t.scale(
                        max_width / t.width
                    )

                group.add(t)

            group.arrange(
                DOWN,
                buff=0.05
            )

            group.move_to(
                np.array([
                    0,
                    CAPTION_Y,
                    0
                ])
            )

            return group

        # ====================================================
        # INITIAL CAPTION
        # ====================================================

        caption = make_caption(
            "An embedding can represent linguistic relations geometrically",
            COLOR_MUTED,
            font_size=16
        )

        self.add_fixed_in_frame_mobjects(
            caption
        )

        # ====================================================
        # STEP 1 — BENIGN
        # ====================================================

        self.play(
            FadeIn(legend),

            GrowFromPoint(
                benign_vector,
                origin
            ),

            FadeIn(
                eq_benign,
                shift=UP * 0.08
            ),

            FadeIn(caption),

            run_time=2.1 * SPEED_FACTOR
        )

        self.wait(
            1.5 * SPEED_FACTOR
        )

        # ====================================================
        # STEP 2 — MALIGNANT
        # ====================================================

        relation_caption = make_caption(
            "The relation from BENIGN to MALIGNANT",
            COLOR_MALIGNANT,
            font_size=16
        )

        self.add_fixed_in_frame_mobjects(
            relation_caption
        )

        self.play(
            FadeOut(caption),

            GrowFromPoint(
                malignant_vector,
                origin
            ),

            FadeIn(
                eq_colon_1,
                shift=UP * 0.05
            ),

            FadeIn(
                eq_malignant,
                shift=UP * 0.05
            ),

            FadeIn(relation_caption),

            run_time=1.7 * SPEED_FACTOR
        )

        self.wait(
            1.3 * SPEED_FACTOR
        )

        # ====================================================
        # STEP 3 — EXPLICIT RELATION VECTOR
        # ====================================================

        semantic_relation = make_vector(
            v_benign,
            v_malignant,
            COLOR_RELATION,
            thickness=0.045
        )

        relation_caption_2 = make_caption(
            "The relation from BENIGN to MALIGNANT",
            COLOR_RELATION,
            font_size=16
        )

        self.add_fixed_in_frame_mobjects(
            relation_caption_2
        )

        self.play(
            FadeOut(relation_caption),

            GrowFromPoint(
                semantic_relation,
                v_benign
            ),

            FadeIn(relation_caption_2),

            run_time=1.8 * SPEED_FACTOR
        )

        self.wait(
            1.4 * SPEED_FACTOR
        )

        # ====================================================
        # STEP 4 — FIBROMA
        # ====================================================

        fibroma_caption = make_caption(
            "Now apply the same relation to FIBROMA",
            COLOR_FIBROMA,
            font_size=16
        )

        self.add_fixed_in_frame_mobjects(
            fibroma_caption
        )

        self.play(
            FadeOut(relation_caption_2),

            GrowFromPoint(
                fibroma_vector,
                origin
            ),

            FadeIn(
                eq_double_colon,
                shift=UP * 0.05
            ),

            FadeIn(
                eq_fibroma,
                shift=UP * 0.05
            ),

            FadeIn(fibroma_caption),

            run_time=1.7 * SPEED_FACTOR
        )

        self.wait(
            1.3 * SPEED_FACTOR
        )

        # ====================================================
        # STEP 5 — TRANSLATE THE RELATION
        # ====================================================

        translated_relation = make_vector(
            v_fibroma,
            v_fibrosarcoma,
            COLOR_RELATION,
            thickness=0.045
        )

        translated_caption = make_caption(
            "Apply the same relation to FIBROMA",
            COLOR_RELATION,
            font_size=16
        )

        self.add_fixed_in_frame_mobjects(
            translated_caption
        )

        self.play(
            FadeOut(fibroma_caption),

            GrowFromPoint(
                translated_relation,
                v_fibroma
            ),

            FadeIn(
                eq_colon_2,
                shift=UP * 0.05
            ),

            FadeIn(translated_caption),

            run_time=2.0 * SPEED_FACTOR
        )

        self.wait(
            1.5 * SPEED_FACTOR
        )

        # ====================================================
        # STEP 6 — RESULT VECTOR
        # ====================================================

        result_vector = make_vector(
            origin,
            v_fibrosarcoma,
            COLOR_FIBROSARCOMA,
            thickness=0.043
        )

        result_caption = make_caption(
            "The translated relation points toward FIBROSARCOMA",
            COLOR_FIBROSARCOMA,
            font_size=16
        )

        self.add_fixed_in_frame_mobjects(
            result_caption
        )

        self.play(
            FadeOut(translated_caption),

            GrowFromPoint(
                result_vector,
                origin
            ),

            FadeIn(
                eq_fibrosarcoma,
                shift=UP * 0.05
            ),

            FadeIn(result_caption),

            run_time=1.9 * SPEED_FACTOR
        )

        self.wait(
            1.5 * SPEED_FACTOR
        )

        # ====================================================
        # STEP 7 — HIGHLIGHT BOTH RELATIONS
        # ====================================================

        # Add visible copies so the thicker highlight actually
        # appears in the scene.

        relation_highlight_1 = semantic_relation.copy()
        relation_highlight_2 = translated_relation.copy()

        self.add(
            relation_highlight_1,
            relation_highlight_2
        )

        self.play(
            relation_highlight_1.animate.set_stroke(
                width=0.07
            ),

            relation_highlight_2.animate.set_stroke(
                width=0.07
            ),

            run_time=0.9 * SPEED_FACTOR
        )

        self.wait(
            1.0 * SPEED_FACTOR
        )

        # ====================================================
        # STEP 8 — FINAL CAPTION
        # ====================================================

        line1 = Text(
            "The two relations are approximately analogous",
            font=FONT,
            font_size=14.5,
            color=COLOR_MUTED,
            weight=BOLD
        )

        line2 = Text(
            "in embedding space",
            font=FONT,
            font_size=14.5,
            color=COLOR_MUTED,
            weight=BOLD
        )

        for line in (line1, line2):

            if line.width > SAFE_W:
                line.scale(
                    SAFE_W / line.width
                )

        final_caption = VGroup(
            line1,
            line2
        ).arrange(
            DOWN,
            buff=0.05
        )

        final_caption.move_to(
            np.array([
                0,
                CAPTION_Y,
                0
            ])
        )

        self.add_fixed_in_frame_mobjects(
            final_caption
        )

        self.play(
            FadeOut(result_caption),
            FadeIn(final_caption),
            run_time=0.9 * SPEED_FACTOR
        )

        # ====================================================
        # FINAL RINGS
        # ====================================================

        ring_malignant = Circle(
            radius=0.22,
            color=COLOR_MALIGNANT,
            stroke_width=3
        )

        ring_malignant.rotate(
            90 * DEGREES,
            axis=RIGHT
        )

        ring_malignant.move_to(
            v_malignant
        )

        ring_result = Circle(
            radius=0.28,
            color=COLOR_FIBROSARCOMA,
            stroke_width=4
        )

        ring_result.rotate(
            90 * DEGREES,
            axis=RIGHT
        )

        ring_result.move_to(
            v_fibrosarcoma
        )

        self.play(
            Create(ring_malignant),
            Create(ring_result),
            run_time=0.8 * SPEED_FACTOR
        )

        self.play(
            ring_malignant.animate
                .scale(1.6)
                .set_opacity(0),

            ring_result.animate
                .scale(1.8)
                .set_opacity(0),

            run_time=1.5 * SPEED_FACTOR
        )

        # ====================================================
        # END
        # ====================================================

        self.stop_ambient_camera_rotation()

        self.wait(
            3.2 * SPEED_FACTOR
        )

        # self.interactive_embed()