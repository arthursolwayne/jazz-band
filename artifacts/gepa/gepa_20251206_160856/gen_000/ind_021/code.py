
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

# Bar 2: Everyone in. Sax takes the melody
# Bb7 - E7 - A7 - D7
# F major key, but the chords are F7, Bb7, E7, A7

# Bass: walking line starting on D2 (MIDI 38)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625),  # F#2
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, each bar a different chord
# Bar 2: F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # C5
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=2.0),  # Eb4
]
piano.notes.extend(piano_notes)

# Sax: One short motif in F, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=110, pitch=66, start=2.0, end=2.25),  # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=70, start=2.0, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.5),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # Ab4
]
piano.notes.extend(piano_notes)

# Bass: walking line starting on Bb2 (MIDI 41)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=2.0, end=2.375),  # Bb2
    pretty_midi.Note(velocity=100, pitch=43, start=2.375, end=2.75),  # D2
    pretty_midi.Note(velocity=100, pitch=44, start=2.75, end=3.125),  # D#2
    pretty_midi.Note(velocity=100, pitch=46, start=3.125, end=3.5),  # F2
]
bass.notes.extend(bass_notes)

# Sax: Continue the motif, answer the question
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # Bb3
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.5),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # Bb3
]
sax.notes.extend(sax_notes)

# Bar 4: E7 (E, G#, B, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0),  # E4
    pretty_midi.Note(velocity=100, pitch=68, start=2.5, end=3.0),  # G#4
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # D4
]
piano.notes.extend(piano_notes)

# Bass: walking line starting on E2 (MIDI 45)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=2.5, end=2.875),  # E2
    pretty_midi.Note(velocity=100, pitch=47, start=2.875, end=3.25),  # G2
    pretty_midi.Note(velocity=100, pitch=48, start=3.25, end=3.625),  # G#2
    pretty_midi.Note(velocity=100, pitch=50, start=3.625, end=4.0),  # B2
]
bass.notes.extend(bass_notes)

# Sax: Finish the motif, resolve
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.75),  # E4
    pretty_midi.Note(velocity=110, pitch=66, start=2.75, end=3.0),  # F4
]
sax.notes.extend(sax_notes)

# Drums: Same pattern as bar 1, offset by 1.5 seconds
for note in drum_notes:
    new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 1.5, note.end + 1.5)
    drums.notes.append(new_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
