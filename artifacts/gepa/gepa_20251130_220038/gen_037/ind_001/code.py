
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=50, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    (1.5, 46, 100, 0.25),  # F
    (1.75, 47, 100, 0.25), # Gb
    (2.0, 48, 100, 0.25),  # G
    (2.25, 45, 100, 0.25), # E
    (2.5, 46, 100, 0.25),  # F
    (2.75, 47, 100, 0.25), # Gb
    (3.0, 48, 100, 0.25),  # G
    (3.25, 45, 100, 0.25), # E
    (3.5, 46, 100, 0.25),  # F
    (3.75, 47, 100, 0.25), # Gb
    (4.0, 48, 100, 0.25),  # G
    (4.25, 45, 100, 0.25), # E
    (4.5, 46, 100, 0.25),  # F
    (4.75, 47, 100, 0.25), # Gb
    (5.0, 48, 100, 0.25),  # G
    (5.25, 45, 100, 0.25)  # E
]
for time, pitch, velocity, duration in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (2.0, 66, 100, 0.25),  # F7 (F, A, C, Eb)
    (2.0, 69, 100, 0.25),
    (2.0, 60, 100, 0.25),
    (2.0, 62, 100, 0.25),

    (3.0, 66, 100, 0.25),
    (3.0, 69, 100, 0.25),
    (3.0, 60, 100, 0.25),
    (3.0, 62, 100, 0.25),

    (4.0, 66, 100, 0.25),
    (4.0, 69, 100, 0.25),
    (4.0, 60, 100, 0.25),
    (4.0, 62, 100, 0.25)
]
for time, pitch, velocity, duration in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=50, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Sax: 1 short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Whisper
note = pretty_midi.Note(velocity=80, pitch=66, start=1.5, end=1.75)
sax.notes.append(note)

note = pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0)
sax.notes.append(note)

# Bar 3: Build
note = pretty_midi.Note(velocity=90, pitch=72, start=2.0, end=2.25)
sax.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5)
sax.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=2.75)
sax.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=66, start=2.75, end=3.0)
sax.notes.append(note)

# Bar 4: Cry
note = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25)
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5)
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75)
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0)
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.25)
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5)
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75)
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0)
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25)
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5)
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=5.75)
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0)
sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI
midi.write("dante_intro.mid")
