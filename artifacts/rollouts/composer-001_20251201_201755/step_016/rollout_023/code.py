
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (F2, C3, G3, D3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=81, start=1.875, end=2.25),  # C3
    pretty_midi.Note(velocity=90, pitch=84, start=2.25, end=2.625),  # G3
    pretty_midi.Note(velocity=90, pitch=86, start=2.625, end=3.0),   # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=91, start=1.5, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=76, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=110, pitch=76, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=110, pitch=72, start=2.75, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (Bb2, F3, C3, G3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=90, pitch=81, start=3.375, end=3.75),  # F3
    pretty_midi.Note(velocity=90, pitch=81, start=3.75, end=4.125),  # C3
    pretty_midi.Note(velocity=90, pitch=84, start=4.125, end=4.5),   # G3
]
bass.notes.extend(bass_notes)

# Piano: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=89, start=3.0, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, avoid scale runs
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=76, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=72, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=110, pitch=76, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=110, pitch=76, start=4.0, end=4.5),   # G
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (Eb2, Bb2, F3, C3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=90, pitch=73, start=4.875, end=5.25),  # Bb2
    pretty_midi.Note(velocity=90, pitch=81, start=5.25, end=5.625),  # F3
    pretty_midi.Note(velocity=90, pitch=81, start=5.625, end=6.0),   # C3
]
bass.notes.extend(bass_notes)

# Piano: Eb7 (Eb, G, Bb, Db)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=85, start=4.5, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif and end on a strong note
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=110, pitch=76, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=110, pitch=72, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=110, pitch=72, start=5.5, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
