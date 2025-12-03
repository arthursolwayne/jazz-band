
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
# Bass: walking line, roots and fifths, chromatic approaches
bass_notes = [
    # D2 (root of Dm)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # F2 (fifth of Dm)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),
    # Eb2 (chromatic approach to D)
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625),
    # D2 again
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F Ab C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4 (D)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # F4 (F)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),  # Ab4 (Ab)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C5 (C)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging
# Motif: D4 (D), Eb4 (Eb), F4 (F), Eb4 (Eb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line, roots and fifths, chromatic approaches
bass_notes = [
    # D2 (root of Dm)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    # F2 (fifth of Dm)
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75),
    # Eb2 (chromatic approach to D)
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125),
    # D2 again
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Bbmaj7 (Bb D F A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # A4
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif on top of the new chord
# Motif: Bb4 (Bb), C4 (C), D4 (D), C4 (C)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=59, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=60, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.0),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line, roots and fifths, chromatic approaches
bass_notes = [
    # D2 (root of Dm)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    # F2 (fifth of Dm)
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25),
    # Eb2 (chromatic approach to D)
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625),
    # D2 again
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: G7 (G B D F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # F5
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif, resolve back to D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.5),
]
sax.notes.extend(sax_notes)

# Drums: same pattern for bar 2-4
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
