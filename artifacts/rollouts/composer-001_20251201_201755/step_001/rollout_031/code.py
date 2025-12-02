
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass (Walking line, roots and fifths with chromatic approaches)
# F7: F, C, Bb, E, D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25), # C (fifth)
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625), # Bb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: E7 (E, G#, B, D)
piano_notes = [
    # Bar 2 (1.5 - 2.25s)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.25), # E

    # Bar 3 (2.25 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0), # D
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=3.0), # Ab

    # Bar 4 (3.0 - 3.75s)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75), # E
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75), # G#
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.75), # B
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.75), # D

    # Bar 4 (3.75 - 6.0s) - Diane plays the same chord but with resolution
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.5), # E
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.5), # G#
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.5), # B
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.5), # D
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.25), # F (resolve)
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=5.25), # E
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=6.0), # F
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=6.0), # A
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=6.0), # C
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=6.0), # E
]
piano.notes.extend(piano_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Bb, C, B (start bar 2), then repeat with resolution in bar 4
sax_notes = [
    # Bar 2 (1.5 - 2.25s)
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.25), # Bb

    # Bar 3 (2.25 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=76, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=110, pitch=77, start=2.625, end=3.0),  # B

    # Bar 4 (3.0 - 3.75s)
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.75), # Bb

    # Bar 4 (3.75 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=76, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=110, pitch=77, start=4.125, end=4.5),  # B

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=5.25), # F
    pretty_midi.Note(velocity=110, pitch=74, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=110, pitch=76, start=5.625, end=6.0),  # C
]
sax.notes.extend(sax_notes)

# Drums: fill the bar with kicks on 1 and 3, snares on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 2.25s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),  # Hihat on every eighth
]
drums.notes.extend(drum_notes)

# Bar 3 (2.25 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),   # Hihat on every eighth
]
drums.notes.extend(drum_notes)

# Bar 4 (3.0 - 3.75s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),   # Hihat on every eighth
]
drums.notes.extend(drum_notes)

# Bar 4 (3.75 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),   # Hihat on every eighth
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 5.25s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),   # Hihat on every eighth
]
drums.notes.extend(drum_notes)

# Bar 4 (5.25 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),   # Hihat on every eighth
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
