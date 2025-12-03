
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)

# Bass: walking line with roots and fifths, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25), # A (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625), # Bb (root)
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),  # D (fifth)
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=78, start=3.375, end=3.75), # F (chromatic)
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.125), # G (root)
    pretty_midi.Note(velocity=90, pitch=83, start=4.125, end=4.5),  # Bb (fifth)
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=83, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=85, start=4.875, end=5.25), # D (chromatic)
    pretty_midi.Note(velocity=90, pitch=86, start=5.25, end=5.625), # Eb (root)
    pretty_midi.Note(velocity=90, pitch=90, start=5.625, end=6.0),  # G (fifth)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, resolve on the last bar
# Bar 2: Fmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # E
    # Bar 3: Bm7
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.5),  # E
    pretty_midi.Note(velocity=100, pitch=81, start=2.0, end=2.5),  # G
    # Bar 4: G7
    pretty_midi.Note(velocity=100, pitch=78, start=2.5, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=81, start=2.5, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=83, start=2.5, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=86, start=2.5, end=3.0),  # F
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F - Bb - D - F
sax_notes = [
    # First note: F (65)
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),
    # Second note: Bb (72)
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.25),
    # Leave it hanging
    # Come back and finish it
    # F (65)
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),
    # Bb (72)
    pretty_midi.Note(velocity=110, pitch=72, start=3.375, end=3.75),
    # D (76)
    pretty_midi.Note(velocity=110, pitch=76, start=3.75, end=4.125),
    # F (65)
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Bar 2
for start in [1.5, 1.875, 2.25, 2.625]:
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)  # Kick on 1 and 3
for start in [2.0, 2.5]:
    pretty_midi.Note(velocity=110, pitch=38, start=start, end=start + 0.125)  # Snare on 2 and 4
for start in [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]:
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)  # Hihat on every eighth

# Bar 3
for start in [3.0, 3.375, 3.75, 4.125]:
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)  # Kick on 1 and 3
for start in [3.5, 4.0]:
    pretty_midi.Note(velocity=110, pitch=38, start=start, end=start + 0.125)  # Snare on 2 and 4
# Hihat
for start in [3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]:
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)

# Bar 4
for start in [4.5, 4.875, 5.25, 5.625]:
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)  # Kick on 1 and 3
for start in [5.0, 5.5]:
    pretty_midi.Note(velocity=110, pitch=38, start=start, end=start + 0.125)  # Snare on 2 and 4
# Hihat
for start in [4.5, 4.875, 5.25, 5.625, 6.0, 6.375, 6.75, 7.125]:
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
