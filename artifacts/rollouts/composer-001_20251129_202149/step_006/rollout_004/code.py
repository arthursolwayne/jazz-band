
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.05)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line with chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.5 + 0.375)),  # C
    (pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=1.875 + 0.375)),  # C#
    (pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.25 + 0.375)),  # D
    (pretty_midi.Note(velocity=100, pitch=63, start=2.625, end=2.625 + 0.375)),  # D#
    (pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.0 + 0.375)),  # E
    (pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.375 + 0.375)),  # F
    (pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=3.75 + 0.375)),  # F#
    (pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.125 + 0.375)),  # G
    (pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.5 + 0.375)),  # G#
    (pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=4.875 + 0.375)),  # A
    (pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.25 + 0.375)),  # A#
    (pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=5.625 + 0.375)),  # B
    (pretty_midi.Note(velocity=100, pitch=72, start=6.0, end=6.0 + 0.375)),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4, comping
# Bar 2: C7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=1.875 + 0.1),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=1.875 + 0.1),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=1.875 + 0.1),
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=1.875 + 0.1),
    # Bar 3: C7 on beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.375 + 0.1),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.375 + 0.1),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.375 + 0.1),
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.375 + 0.1),
    # Bar 4: C7 on beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=4.875 + 0.1),
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=4.875 + 0.1),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=4.875 + 0.1),
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=4.875 + 0.1),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax - short motif, start it, leave it hanging, come back and finish it
# Motif: C (60) -> E (64) -> B (71) -> E (64)
# Start on bar 2, beat 1 (1.5s)
note1 = pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.5 + 0.15)
note2 = pretty_midi.Note(velocity=110, pitch=64, start=1.65, end=1.65 + 0.15)
note3 = pretty_midi.Note(velocity=110, pitch=71, start=1.8, end=1.8 + 0.15)
note4 = pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.0 + 0.15)
sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)
sax.notes.append(note4)

# Drums for bars 2-4
for bar in range(2, 4):
    start_time = bar * 1.5
    for beat in range(4):
        time = start_time + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.05)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
