
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full band starts
# Bass: walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F2 (root), F#2 (chromatic), G2 (fifth), F2 (root)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=78, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=80, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=90, start=1.5, end=1.875),
]
piano.notes.extend(piano_notes)

# Sax: Melody - short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),   # F
]
sax.notes.extend(sax_notes)

# Bar 3
# Bass: walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 3: F2 (root), F#2 (chromatic), G2 (fifth), F2 (root)
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=78, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=80, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=77, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: F7 (F, A, C, E flat)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=89, start=3.0, end=3.375),
]
piano.notes.extend(piano_notes)

# Sax: Repeat motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),   # F
]
sax.notes.extend(sax_notes)

# Bar 4
# Bass: walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 4: F2 (root), F#2 (chromatic), G2 (fifth), F2 (root)
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=78, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=80, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=77, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=90, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Sax: End on F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
