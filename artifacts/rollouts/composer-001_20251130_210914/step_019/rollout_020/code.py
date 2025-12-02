
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    time = bar * 1.5
    # Kick on beat 1
    midi_note = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.0, end=time + 0.375)
    drums.notes.append(midi_note)
    # Snare on beat 2
    midi_note = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.75, end=time + 1.125)
    drums.notes.append(midi_note)
    # Kick on beat 3
    midi_note = pretty_midi.Note(velocity=100, pitch=36, start=time + 1.125, end=time + 1.5)
    drums.notes.append(midi_note)
    # Hihat on every eighth
    for i in range(8):
        midi_note = pretty_midi.Note(velocity=60, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(midi_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Start with sax melody
# Motif: D (D4), F# (F#4), G (G4), A (A4) - short and singable
# Start on beat 1, leave it hanging on beat 3

# Bar 2 (1.5 - 3.0s)
# Sax
note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0)
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line with chromatic approaches
# D (D2), Eb (Eb2), E (E2), F (F2), F# (F#2), G (G2), G# (G#2), A (A2)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=54, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=55, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=56, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=57, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: D7 (D, F#, A, C)
chord_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=2.25),
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=2.25),
    pretty_midi.Note(velocity=80, pitch=57, start=1.5, end=2.25),
    pretty_midi.Note(velocity=80, pitch=59, start=1.5, end=2.25)
]
piano.notes.extend(chord_notes)

# Bar 3 (3.0 - 4.5s)
# Sax: Repeat motif with slight variation
note1 = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375)
note2 = pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75)
note3 = pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125)
note4 = pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5)
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=58, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=61, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 3: D7 (D, F#, A, C)
chord_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.75),
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.75),
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.75),
    pretty_midi.Note(velocity=80, pitch=59, start=3.0, end=3.75)
]
piano.notes.extend(chord_notes)

# Bar 4 (4.5 - 6.0s)
# Sax: Finish the motif
note1 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875)
note2 = pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25)
note3 = pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625)
note4 = pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0)
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=66, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 4: D7 (D, F#, A, C)
chord_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=5.25),
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=5.25),
    pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=5.25),
    pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=5.25)
]
piano.notes.extend(chord_notes)

# Drums for bars 2-4
for bar in range(2, 4):
    time = bar * 1.5
    # Kick on beat 1
    midi_note = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.0, end=time + 0.375)
    drums.notes.append(midi_note)
    # Snare on beat 2
    midi_note = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.75, end=time + 1.125)
    drums.notes.append(midi_note)
    # Kick on beat 3
    midi_note = pretty_midi.Note(velocity=100, pitch=36, start=time + 1.125, end=time + 1.5)
    drums.notes.append(midi_note)
    # Hihat on every eighth
    for i in range(8):
        midi_note = pretty_midi.Note(velocity=60, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(midi_note)

midi.instruments.extend([sax, bass, piano, drums])
