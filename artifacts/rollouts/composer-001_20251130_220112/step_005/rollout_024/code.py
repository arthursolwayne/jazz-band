
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 1.125, end=bar1_start + 1.5)

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=110, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.875)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=bar1_start + 1.875, end=bar1_start + 2.0)

# Hihat on every eighth
hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=bar1_start, end=bar1_start + 0.1875)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.375, end=bar1_start + 0.5625)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.75, end=bar1_start + 0.9375)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 1.125, end=bar1_start + 1.3125)
hihat5 = pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 1.5, end=bar1_start + 1.6875)
hihat6 = pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 1.875, end=bar1_start + 2.0625)

drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4, hihat5, hihat6])

# Bars 2-4: Full quartet (1.5 - 6.0s)
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Marcus: Walking bass line in D (D, F#, A, B, D, F#, A, B)
# Bar 2
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=bar2_start, end=bar2_start + 0.375),    # D
    pretty_midi.Note(velocity=80, pitch=67, start=bar2_start + 0.375, end=bar2_start + 0.75),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=bar2_start + 0.75, end=bar2_start + 1.125),  # F#
    pretty_midi.Note(velocity=80, pitch=69, start=bar2_start + 1.125, end=bar2_start + 1.5),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=bar2_start + 1.5, end=bar2_start + 1.875),   # A
    pretty_midi.Note(velocity=80, pitch=71, start=bar2_start + 1.875, end=bar2_start + 2.25),  # B
    pretty_midi.Note(velocity=80, pitch=71, start=bar2_start + 2.25, end=bar2_start + 2.625),  # B
    pretty_midi.Note(velocity=80, pitch=62, start=bar2_start + 2.625, end=bar2_start + 3.0),   # D
]

# Bar 3
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=62, start=bar3_start, end=bar3_start + 0.375),    # D
    pretty_midi.Note(velocity=80, pitch=67, start=bar3_start + 0.375, end=bar3_start + 0.75),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=bar3_start + 0.75, end=bar3_start + 1.125),  # F#
    pretty_midi.Note(velocity=80, pitch=69, start=bar3_start + 1.125, end=bar3_start + 1.5),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=bar3_start + 1.5, end=bar3_start + 1.875),   # A
    pretty_midi.Note(velocity=80, pitch=71, start=bar3_start + 1.875, end=bar3_start + 2.25),  # B
    pretty_midi.Note(velocity=80, pitch=71, start=bar3_start + 2.25, end=bar3_start + 2.625),  # B
    pretty_midi.Note(velocity=80, pitch=62, start=bar3_start + 2.625, end=bar3_start + 3.0),   # D
])

# Bar 4
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=62, start=bar4_start, end=bar4_start + 0.375),    # D
    pretty_midi.Note(velocity=80, pitch=67, start=bar4_start + 0.375, end=bar4_start + 0.75),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=bar4_start + 0.75, end=bar4_start + 1.125),  # F#
    pretty_midi.Note(velocity=80, pitch=69, start=bar4_start + 1.125, end=bar4_start + 1.5),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=bar4_start + 1.5, end=bar4_start + 1.875),   # A
    pretty_midi.Note(velocity=80, pitch=71, start=bar4_start + 1.875, end=bar4_start + 2.25),  # B
    pretty_midi.Note(velocity=80, pitch=71, start=bar4_start + 2.25, end=bar4_start + 2.625),  # B
    pretty_midi.Note(velocity=80, pitch=62, start=bar4_start + 2.625, end=bar4_start + 3.0),   # D
])

bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4, D7 (D, F#, A, C#)
bar2_diane = [
    pretty_midi.Note(velocity=90, pitch=62, start=bar2_start + 0.75, end=bar2_start + 1.125),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=bar2_start + 0.75, end=bar2_start + 1.125),  # F#
    pretty_midi.Note(velocity=90, pitch=69, start=bar2_start + 0.75, end=bar2_start + 1.125),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=bar2_start + 0.75, end=bar2_start + 1.125),  # C#

    pretty_midi.Note(velocity=90, pitch=62, start=bar2_start + 1.875, end=bar2_start + 2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=bar2_start + 1.875, end=bar2_start + 2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=69, start=bar2_start + 1.875, end=bar2_start + 2.25),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=bar2_start + 1.875, end=bar2_start + 2.25),  # C#

    pretty_midi.Note(velocity=90, pitch=62, start=bar2_start + 3.0, end=bar2_start + 3.375),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=bar2_start + 3.0, end=bar2_start + 3.375),   # F#
    pretty_midi.Note(velocity=90, pitch=69, start=bar2_start + 3.0, end=bar2_start + 3.375),   # A
    pretty_midi.Note(velocity=90, pitch=64, start=bar2_start + 3.0, end=bar2_start + 3.375),   # C#
]

bar3_diane = [
    pretty_midi.Note(velocity=90, pitch=62, start=bar3_start + 0.75, end=bar3_start + 1.125),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=bar3_start + 0.75, end=bar3_start + 1.125),  # F#
    pretty_midi.Note(velocity=90, pitch=69, start=bar3_start + 0.75, end=bar3_start + 1.125),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=bar3_start + 0.75, end=bar3_start + 1.125),  # C#

    pretty_midi.Note(velocity=90, pitch=62, start=bar3_start + 1.875, end=bar3_start + 2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=bar3_start + 1.875, end=bar3_start + 2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=69, start=bar3_start + 1.875, end=bar3_start + 2.25),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=bar3_start + 1.875, end=bar3_start + 2.25),  # C#

    pretty_midi.Note(velocity=90, pitch=62, start=bar3_start + 3.0, end=bar3_start + 3.375),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=bar3_start + 3.0, end=bar3_start + 3.375),   # F#
    pretty_midi.Note(velocity=90, pitch=69, start=bar3_start + 3.0, end=bar3_start + 3.375),   # A
    pretty_midi.Note(velocity=90, pitch=64, start=bar3_start + 3.0, end=bar3_start + 3.375),   # C#
]

bar4_diane = [
    pretty_midi.Note(velocity=90, pitch=62, start=bar4_start + 0.75, end=bar4_start + 1.125),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=bar4_start + 0.75, end=bar4_start + 1.125),  # F#
    pretty_midi.Note(velocity=90, pitch=69, start=bar4_start + 0.75, end=bar4_start + 1.125),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=bar4_start + 0.75, end=bar4_start + 1.125),  # C#

    pretty_midi.Note(velocity=90, pitch=62, start=bar4_start + 1.875, end=bar4_start + 2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=bar4_start + 1.875, end=bar4_start + 2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=69, start=bar4_start + 1.875, end=bar4_start + 2.25),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=bar4_start + 1.875, end=bar4_start + 2.25),  # C#

    pretty_midi.Note(velocity=90, pitch=62, start=bar4_start + 3.0, end=bar4_start + 3.375),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=bar4_start + 3.0, end=bar4_start + 3.375),   # F#
    pretty_midi.Note(velocity=90, pitch=69, start=bar4_start + 3.0, end=bar4_start + 3.375),   # A
    pretty_midi.Note(velocity=90, pitch=64, start=bar4_start + 3.0, end=bar4_start + 3.375),   # C#
]

piano.notes.extend(bar2_diane + bar3_diane + bar4_diane)

# Dante: Sax motif: D, F#, B, D (start on bar 2)
note1 = pretty_midi.Note(velocity=110, pitch=62, start=bar2_start, end=bar2_start + 0.375)
note2 = pretty_midi.Note(velocity=110, pitch=67, start=bar2_start + 0.375, end=bar2_start + 0.75)
note3 = pretty_midi.Note(velocity=110, pitch=71, start=bar2_start + 0.75, end=bar2_start + 1.125)
note4 = pretty_midi.Note(velocity=110, pitch=62, start=bar2_start + 1.125, end=bar2_start + 1.5)

# Repeat
note5 = pretty_midi.Note(velocity=110, pitch=62, start=bar3_start, end=bar3_start + 0.375)
note6 = pretty_midi.Note(velocity=110, pitch=67, start=bar3_start + 0.375, end=bar3_start + 0.75)
note7 = pretty_midi.Note(velocity=110, pitch=71, start=bar3_start + 0.75, end=bar3_start + 1.125)
note8 = pretty_midi.Note(velocity=110, pitch=62, start=bar3_start + 1.125, end=bar3_start + 1.5)

# Final iteration
note9 = pretty_midi.Note(velocity=110, pitch=62, start=bar4_start, end=bar4_start + 0.375)
note10 = pretty_midi.Note(velocity=110, pitch=67, start=bar4_start + 0.375, end=bar4_start + 0.75)
note11 = pretty_midi.Note(velocity=110, pitch=71, start=bar4_start + 0.75, end=bar4_start + 1.125)
note12 = pretty_midi.Note(velocity=110, pitch=62, start=bar4_start + 1.125, end=bar4_start + 1.5)

sax.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8, note9, note10, note11, note12])

# Drums: Bar 2-4
bar2_drums = [
    pretty_midi.Note(velocity=100, pitch=36, start=bar2_start, end=bar2_start + 0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + 0.75, end=bar2_start + 0.875),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=bar2_start + 1.125, end=bar2_start + 1.3125),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=bar2_start + 1.5, end=bar2_start + 1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + 2.25, end=bar2_start + 2.375),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=bar2_start + 2.625, end=bar2_start + 2.8125),  # Hihat
]

bar3_drums = [
    pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 0.75, end=bar3_start + 0.875),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 1.125, end=bar3_start + 1.3125),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=bar3_start + 1.5, end=bar3_start + 1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 2.25, end=bar3_start + 2.375),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + 2.625, end=bar3_start + 2.8125),  # Hihat
]

bar4_drums = [
    pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 0.75, end=bar4_start + 0.875),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 1.125, end=bar4_start + 1.3125),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=bar4_start + 1.5, end=bar4_start + 1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 2.25, end=bar4_start + 2.375),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + 2.625, end=bar4_start + 2.8125),  # Hihat
]

drums.notes.extend(bar2_drums + bar3_drums + bar4_drums)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
