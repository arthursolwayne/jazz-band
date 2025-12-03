
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Roots and fifths with chromatic approaches (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=2.0),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=2.0, end=2.5),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=3.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=2.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Motif - start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Roots and fifths with chromatic approaches (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.5),  # E2
    pretty_midi.Note(velocity=90, pitch=43, start=3.5, end=4.0),  # G2
    pretty_midi.Note(velocity=90, pitch=38, start=4.0, end=4.5),  # D2
]
bass.notes.extend(bass_notes)

# Piano: G7 (G-B-D-F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.5),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.5),  # D5
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.5),  # F5
]
piano.notes.extend(piano_notes)

# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # F4
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Roots and fifths with chromatic approaches (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=5.0),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=5.0, end=5.5),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=5.5, end=6.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Cmaj7 (C-E-G-B)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=5.0),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.0),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.0),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.0),  # B4
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D4
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
